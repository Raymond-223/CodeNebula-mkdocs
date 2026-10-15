from pathlib import Path
import re
from bs4 import BeautifulSoup
root=Path(__file__).resolve().parents[1]/'site'
issues=[];count=0
for p in root.rglob('index.html'):
    soup=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
    article=soup.select_one('.md-content__inner')
    if not article:continue
    count+=1
    for el in article.select('pre,code,.arithmatex,script,style'):el.decompose()
    for t in article.stripped_strings:
        if '$$' in t or re.search(r'\\(?:begin|end)\{',t):issues.append((str(p.relative_to(root)),t[:180]))
print('Built-page TeX delimiter audit:',count,'pages; issues:',issues)
assert not issues
