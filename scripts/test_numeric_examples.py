#!/usr/bin/env python3
"""Numerical regressions for claims whose syntax-only checks cannot validate."""
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import math
import re
import warnings

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

# Source regressions for typographical mistakes that still produce valid MathJax.
workbook_text = (DOCS / "yau-contest" / "06-stage-one-workbook.md").read_text(encoding="utf-8")
assert "|a_{ii}|,|x_i|" not in workbook_text
assert "\\frac23,4^{-n}" not in workbook_text

fixed_point_text = (DOCS / "yau-contest" / "04-fixed-points-contractions.md").read_text(encoding="utf-8")
assert "x_k=1/k" not in fixed_point_text

inverse_text = (DOCS / "yau-contest" / "03-linear-iterations-power.md").read_text(encoding="utf-8")
assert "\\mu\\notin\\sigma(A)" in inverse_text


def code_blocks(path: Path) -> list[str]:
    raw = path.read_text(encoding="utf-8")
    return re.findall(r"```python\s*\n(.*?)\n```", raw, flags=re.S)


def run_block(code: str) -> str:
    output = StringIO()
    with warnings.catch_warnings():
        warnings.simplefilter("error")
        with redirect_stdout(output):
            exec(compile(code, "<documentation-example>", "exec"), {})
    return output.getvalue()


markov = DOCS / "foundations" / "mathematics" / "06-markov-processes.md"
blocks = code_blocks(markov)
spectral_demo = next(code for code in blocks if "lam2 =" in code)
comparison_demo = next(code for code in blocks if '"晴雨链' in code and "chains =" in code)

spectral_output = run_block(spectral_demo)
assert "|lam2|=0.5000" in spectral_output
assert "inf" not in spectral_output.lower()

comparison_output = run_block(comparison_demo)
for expected in ("晴雨链       |lam2|=0.500", "慢链(0.99)  |lam2|=0.980"):
    assert expected in comparison_output

# Independent mathematical regressions for corrected teaching claims.
assert math.isclose(math.sqrt(2) - 1, 0.4142135623730951)

A = np.zeros((2, 2))
B = np.array([[1.0], [1.0]])
controllability = np.hstack([B, A @ B])
assert np.linalg.matrix_rank(controllability) == 1

# A stable non-normal matrix can enlarge the Euclidean norm transiently.
N = np.array([[0.0, 10.0], [0.0, 0.0]])
assert max(abs(np.linalg.eigvals(N))) == 0
assert np.linalg.norm(N @ np.array([0.0, 1.0])) > 1

# Derivative modulus one is inconclusive: x -> x - x^3 still attracts nearby points.
x = 0.1
for _ in range(2000):
    x = x - x**3
assert abs(x) < 0.02

# The corrected Fibonacci expansion satisfies s[k+1] = s[k] + s[k-1] + d[k].
def fibonacci(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


s0, s1 = 2.0, 3.0
d = [None, 0.25, -0.5, 0.75, 0.1, -0.2]
s = [s0, s1]
for k in range(1, len(d)):
    s.append(s[k] + s[k - 1] + d[k])
for k in range(2, len(s)):
    expanded = (
        fibonacci(k) * s1
        + fibonacci(k - 1) * s0
        + sum(fibonacci(k - j) * d[j] for j in range(1, k))
    )
    assert math.isclose(s[k], expanded)

# Least-squares residual is orthogonal to columns of A, not to scalar x.
A_ls = np.array([[1.0], [2.0], [3.0]])
b_ls = np.array([1.0, 2.0, 4.0])
x_ls, *_ = np.linalg.lstsq(A_ls, b_ls, rcond=None)
r_ls = A_ls @ x_ls - b_ls
assert np.allclose(A_ls.T @ r_ls, 0.0)

# Workbook contraction example: exact error reaches 1e-6 first at n=10.
errors = [(2.0 / 3.0) * 4.0**(-n) for n in range(11)]
assert errors[9] >= 1e-6 and errors[10] < 1e-6

# The two-layer backprop example matches finite differences.
x_ml, y_ml = 2.0, 4.0
W1 = np.array([1.0, -0.5])
b1 = np.array([0.0, 2.0])
W2 = np.array([3.0, -1.0])

def ml_loss(w1: np.ndarray) -> float:
    h = np.maximum(w1 * x_ml + b1, 0.0)
    y_hat = W2 @ h
    return 0.5 * float((y_hat - y_ml) ** 2)


analytic = np.array([6.0, -2.0])
eps = 1e-6
numeric = np.empty_like(W1)
for i in range(W1.size):
    step = np.zeros_like(W1)
    step[i] = eps
    numeric[i] = (ml_loss(W1 + step) - ml_loss(W1 - step)) / (2 * eps)
assert np.allclose(analytic, numeric, atol=1e-6)

print("Numerical documentation regressions passed.")
