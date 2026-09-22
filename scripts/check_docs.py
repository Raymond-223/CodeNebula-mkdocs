#!/usr/bin/env python3
from pathlib import Path
import ast
import re
import sys
import xml.etree.ElementTree as ET
import yaml

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / 'docs'
errors = []

EXPECTED_SECTIONS = [
    'mathematics', 'reinforcement-learning', 'game-theory', 'multi-agent-systems',
    'control-theory', 'robotics', 'perception', 'distributed-systems',
    'software-engineering', 'simulation-sim2real', 'robustness-safety',
    'human-ai-interaction',
]
EXPECTED_DOMAINS = [
    'Foundations', 'Decision & Learning', 'Robotics & Perception',
    'Systems & Simulation', 'Safety & Human Factors',
]
ENGINEERING_SECTIONS = {
    'robotics', 'perception', 'distributed-systems', 'software-engineering',
    'simulation-sim2real',
}
THEORY_SECTIONS = {
    'mathematics', 'game-theory', 'reinforcement-learning',
    'multi-agent-systems', 'control-theory',
}


def strip_fences(text: str) -> str:
    out, inside, marker = [], False, None
    for line in text.splitlines():
        m = re.match(r'\s*(```+|~~~+)', line)
        if m:
            c = m.group(1)[0]
            if not inside:
                inside, marker = True, c
            elif c == marker:
                inside, marker = False, None
            out.append('')
            continue
        out.append('' if inside else line)
    return '\n'.join(out)


def walk_nav(node, labels, targets):
    if isinstance(node, list):
        for item in node:
            walk_nav(item, labels, targets)
    elif isinstance(node, dict):
        for k, v in node.items():
            labels.append(str(k))
            walk_nav(v, labels, targets)
    elif isinstance(node, str):
        targets.append(node)


cfg = yaml.safe_load((ROOT / 'mkdocs.yml').read_text(encoding='utf-8'))
nav = cfg.get('nav', [])
labels, targets = [], []
walk_nav(nav, labels, targets)

# Navigation.
top_keys = [next(iter(x)) for x in nav if isinstance(x, dict)]
for domain in EXPECTED_DOMAINS:
    if domain not in top_keys:
        errors.append(f'Missing top navigation domain: {domain}')
for label in labels:
    if re.search(r'[\u4e00-\u9fff]', label):
        errors.append(f'Navigation label is not English-only: {label}')

# Curriculum size: guard both bloat and accidental over-compression.
section_dirs = [p for p in DOCS.iterdir() if p.is_dir() and p.name not in {'stylesheets', 'javascripts', 'assets', 'img', 'css'}]
actual_sections = sorted(p.name for p in section_dirs)
if actual_sections != sorted(EXPECTED_SECTIONS):
    errors.append(f'Section directories mismatch: {actual_sections}')

chapter_total = 0
chapter_counts = {}
for name in EXPECTED_SECTIONS:
    d = DOCS / name
    if not (d / 'index.md').is_file():
        errors.append(f'Missing section overview: {name}/index.md')
        continue
    chapters = sorted(p for p in d.glob('*.md') if p.name != 'index.md')
    chapter_counts[name] = len(chapters)
    chapter_total += len(chapters)
    if not 4 <= len(chapters) <= 7:
        errors.append(f'{name}: expected a compact 4-7 chapter core, found {len(chapters)}')
if not 55 <= chapter_total <= 65:
    errors.append(f'Curriculum bloat/compression guard failed: {chapter_total} core chapters')

# Navigation targets and orphan Markdown pages.
for target in targets:
    if not (DOCS / target).is_file():
        errors.append(f'NAV missing: {target}')
nav_paths = {Path(t).as_posix() for t in targets}
all_md = {p.relative_to(DOCS).as_posix() for p in DOCS.rglob('*.md')}
orphans = sorted(all_md - nav_paths)
if orphans:
    errors.append('Markdown pages missing from nav: ' + ', '.join(orphans))

link_re = re.compile(r'(!?)\[[^\]]*\]\(([^)]+)\)')
forbidden_headings = [
    '## Why it matters', '## Core ideas', '## Key theory',
    '## Representative methods', '## Worked example', '## Connections',
    '## Further Reading', '## Further Study', '## Learning path',
    '## 基本概念', '## 核心原理', '## 常用方法', '## 一个简单例子',
]

python_blocks = []
section_code_counts = {s: 0 for s in EXPECTED_SECTIONS}
section_image_counts = {s: 0 for s in EXPECTED_SECTIONS}

for p in DOCS.rglob('*.md'):
    raw = p.read_text(encoding='utf-8')
    clean = strip_fences(raw)
    rel = p.relative_to(ROOT)

    for ch in raw:
        if ord(ch) < 32 and ch not in '\n\t':
            errors.append(f'Control character U+{ord(ch):04X}: {rel}')
            break
    if '\t' in raw:
        errors.append(f'Tab character in Markdown (possible LaTeX corruption): {rel}')

    if len(re.findall(r'^\s*```', raw, flags=re.M)) % 2:
        errors.append(f'Unbalanced code fence: {rel}')
    if clean.count('$$') % 2:
        errors.append(f'Unbalanced display math $$: {rel}')
    inline_scan = clean.replace('$$', '')
    if len(re.findall(r'(?<!\\)\$', inline_scan)) % 2:
        errors.append(f'Unbalanced inline math $: {rel}')

    if re.search(r'(?:P|p|b|\\pi|\\mathbb\{P\}|\\mathbb\{E\})\([^\n)]*\\\|', clean):
        errors.append(f'Conditional math uses \\| instead of \\mid: {rel}')
    if re.search(r'\\\\(?:alpha|beta|gamma|theta|rho|pi|mathcal|mathbb|frac|sum|prod|nabla|left|right|begin|end)', clean):
        errors.append(f'Double-escaped LaTeX command: {rel}')
    for broken in ('heta', 'ho_t', 'arepsilon'):
        if re.search(rf'(?<![A-Za-z\\]){broken}', clean):
            errors.append(f'Possible damaged LaTeX token "{broken}": {rel}')

    if p.name != 'index.md' and p.parent != DOCS:
        for h in forbidden_headings:
            if h in raw:
                errors.append(f'Forbidden template heading {h!r}: {rel}')

        # Article-style guard: enough structure to explain a topic, but not a giant outline.
        h2_count = len(re.findall(r'^##\s+', raw, flags=re.M))
        if h2_count < 4:
            errors.append(f'Chapter is too outline-thin (only {h2_count} H2 sections): {rel}')
        if h2_count > 10:
            errors.append(f'Chapter is over-sectioned ({h2_count} H2 sections): {rel}')
        line_count = len(raw.splitlines())
        if line_count < 40:
            errors.append(f'Chapter is too short to explain the topic clearly ({line_count} lines): {rel}')
        if line_count > 220:
            errors.append(f'Chapter is becoming encyclopedic ({line_count} lines): {rel}')

    # Do not repeat the same image in one article.
    local_images = [target.strip().split('#', 1)[0] for flag, target in link_re.findall(clean) if flag == '!']
    seen_images = set()
    for image in local_images:
        if image in seen_images:
            errors.append(f'Duplicate image in one article: {rel} -> {image}')
        seen_images.add(image)

    for _, target in link_re.findall(clean):
        target = target.strip().split('#', 1)[0]
        if not target or target.startswith(('http://', 'https://', 'mailto:', 'data:')):
            continue
        dest = (p.parent / target).resolve()
        if not dest.exists():
            errors.append(f'Broken local link: {rel} -> {target}')

    # Collect code/image density by section.
    try:
        section = p.relative_to(DOCS).parts[0]
    except Exception:
        section = None
    if section in section_code_counts:
        section_code_counts[section] += len(re.findall(r'^```(?:python|bash|dockerfile|yaml|json|cpp)\s*$', raw, flags=re.M))
        section_image_counts[section] += len(re.findall(r'!\[[^\]]*\]\([^)]+\)', raw))
    for m in re.finditer(r'```python\s*\n(.*?)\n```', raw, flags=re.S):
        code = m.group(1)
        nonblank = sum(1 for line in code.splitlines() if line.strip())
        if nonblank > 16:
            errors.append(f'Python example is too long for a concept page ({nonblank} lines): {rel}')
        python_blocks.append((rel, code))

# Validate Python syntax.
for rel, code in python_blocks:
    try:
        ast.parse(code)
    except SyntaxError as e:
        errors.append(f'Python syntax error in {rel}: {e.msg} line {e.lineno}')

# Visual set: rich but deliberately bounded.
diagram_files = list((DOCS / 'assets' / 'diagrams').glob('*.svg'))
diagram_refs = []
for p in DOCS.rglob('*.md'):
    diagram_refs.extend(re.findall(r'assets/diagrams/([^)]+\.svg)', p.read_text(encoding='utf-8')))
for f in diagram_files:
    try:
        ET.parse(f)
    except ET.ParseError as e:
        errors.append(f'Invalid SVG XML: {f.relative_to(ROOT)}: {e}')
if not 40 <= len(diagram_files) <= 55:
    errors.append(f'Visual density guard expected 40-55 SVGs, found {len(diagram_files)}')
if len(set(diagram_refs)) != len(diagram_files):
    errors.append(f'Not every generated diagram is used: {len(set(diagram_refs))}/{len(diagram_files)} referenced')
for section, n in section_image_counts.items():
    if not 2 <= n <= 12:
        errors.append(f'{section}: image density out of range, found {n}')

# Code ownership: theory explains with equations/pseudocode; executable examples live in engineering.
for section in THEORY_SECTIONS:
    n = section_code_counts[section]
    if n:
        errors.append(f'{section}: theory section contains {n} executable code blocks')
if not 12 <= len(python_blocks) <= 28:
    errors.append(f'Python example density guard expected 12-28 blocks, found {len(python_blocks)}')
for section in ENGINEERING_SECTIONS:
    n = section_code_counts[section]
    if not 2 <= n <= 12:
        errors.append(f'{section}: engineering implementation-code density out of range, found {n} blocks')

if errors:
    print('Documentation checks failed:')
    for e in errors:
        print(' -', e)
    sys.exit(1)

print(
    f'Documentation checks passed: 12 sections, {chapter_total} core chapters, '
    f'{len(all_md)} Markdown pages, {len(diagram_files)} diagrams, '
    f'{len(python_blocks)} Python examples; theory sections contain no executable code.'
)
