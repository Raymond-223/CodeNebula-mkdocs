"""Cross-check source provenance, folds, and representative new formulas."""
from pathlib import Path
import json,hashlib
import numpy as np
import sympy as s
from numpy.testing import assert_allclose
ROOT=Path(__file__).resolve().parents[1]
manifest=json.loads((ROOT/'SOURCE_PAPERS.json').read_text(encoding='utf8'))
items=json.loads((ROOT/'scripts/yau_selection.json').read_text(encoding='utf8'))
page=(ROOT/'docs/yau-contest/06-stage-one-workbook.md').read_text(encoding='utf8')
assert len(items)==manifest['problem_groups']==page.count('??? proof "答案"')
assert '???+' not in page and page.count('\n## ')==len(items)
assert not any(x in page for x in ('先修章节','学习建议','本章不选'))
for record in manifest['papers']:
 p=ROOT/'docs/assets/yau-papers'/record['asset']
 assert hashlib.sha256(p.read_bytes()).hexdigest()==record['local_sha256']
# Weighted logarithmic moments and the published four-node Jacobi coefficients.
x=s.symbols('x')
ip=lambda p,q:sum(c/s.Integer(m[0]+1)**2 for m,c in s.Poly(s.expand(p*q),x).terms())
ps=[s.Integer(1)];hs=[s.Integer(1)];aa=[];bb=[]
for n in range(4):
 a=ip(x*ps[n],ps[n])/hs[n];b=hs[n]/hs[n-1] if n else 0
 aa.append(a);bb.append(b)
 p=s.expand((x-a)*ps[n]-(b*ps[n-1] if n else 0));ps.append(p);hs.append(ip(p,p))
assert aa==[s.Rational(1,4),s.Rational(13,28),s.Rational(8795,18116),s.Rational(124351943,252694908)]
assert bb[1:]==[s.Rational(7,144),s.Rational(647,11025),s.Rational(71180289,1172105200)]
# Exact rational counterexample to the generalized relaxation determinant claim.
A=np.array([[1,-.84,-.04],[-.41,1,-.30],[.55,-.37,1]])
O=np.diag([1.71,2.70,1.83]);L=np.tril(A,-1);U=np.triu(A,1)
M=np.linalg.solve(np.eye(3)+.54*O@L,np.eye(3)-O-.46*O@L-O@U)
assert max(abs(np.linalg.eigvals(M)))<1
assert np.prod(abs(1-np.diag(O)))>1
# Multi-rate method and its actual first-order global accuracy.
for k in [.1,.5,1.9]:
 B=np.array([[(1-k/2)**2,k*(1-k/4)],[0,1-k]])
 assert max(abs(np.linalg.eigvals(B)))<1
# Five-point advection amplification: CFL and actual norm stability differ.
t=np.linspace(-np.pi,np.pi,10001)
for nu in [.2,.6]:
 g=np.cos(t)-1j*nu/3*np.sin(t)*(4-np.cos(t))
 assert max(abs(g))<=1+1e-12
g=np.cos(t)-1j*.7/3*np.sin(t)*(4-np.cos(t))
assert max(abs(g))>1.001
# Steepest-descent quadratic energy bound.
rng=np.random.default_rng(20261015)
for _ in range(20):
 Z=rng.normal(size=(5,5));A=Z.T@Z+np.eye(5);v=rng.normal(size=5)
 alpha=(v@A@A@v)/(2*(v@A@A@A@v));w=v-2*alpha*A@v
 eig=np.linalg.eigvalsh(A);q=((eig[-1]-eig[0])/(eig[-1]+eig[0]))**2
 assert w@A@w<=q*(v@A@v)+1e-10
# Original GMRES orthogonality ambiguity, checked using an independent LS solve.
A=np.diag([2.,2.,2.])+np.diag([1.,1.],1)+np.diag([1.,1.],-1)
b=np.array([1.,0.,0.]);Q=np.eye(3)[:,:2]
y=np.linalg.lstsq(A@Q,b,rcond=None)[0];r=b-A@Q@y
assert_allclose(r,[1/14,-1/7,3/14],atol=1e-14)
assert_allclose((A@Q).T@r,0,atol=1e-14)
# Tridiagonal generalized eigenvalues, circle-plane identity, similarity profile.
n=7;A=np.diag([2.]*n)+np.diag([-1.]*(n-1),1)+np.diag([-1.]*(n-1),-1)
B=np.diag([4.]*n)+np.diag([1.]*(n-1),1)+np.diag([1.]*(n-1),-1)
c=np.cos(np.arange(1,n+1)*np.pi/(n+1))
assert_allclose(np.sort(np.linalg.eigvals(np.linalg.solve(B,A))),np.sort((2-2*c)/(4+2*c)))
u,v=s.symbols('u v');z=-u-v
assert s.expand(u**4+v**4+z**4-(u*u+v*v+z*z)**2/2)==0
phi=(1-x*x)/16
assert s.simplify(-phi/2-x*s.diff(phi,x)/4-s.diff(phi**2,x,2)-s.diff(phi**2,x)/x)==0
assert s.integrate(phi*x,(x,0,1))==s.Rational(1,64)
print(f'Archive checks passed: {len(items)} folds, {len(manifest["papers"])} original source records, representative independent algebra/numerics.')
