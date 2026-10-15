"""Independent numerical/symbolic checks for the selected official problems."""
import numpy as np
from numpy.testing import assert_allclose
import sympy as sp

# 2025 P2: verify the closed-form spectrum and inverse spectral radius.
A=np.diag(np.ones(7),1)+np.diag(np.ones(7),-1)
expected=2*np.cos(np.arange(1,9)*np.pi/9)
assert_allclose(np.linalg.eigvalsh(A),np.sort(expected),atol=1e-14)
assert_allclose(max(abs(np.linalg.eigvals(np.linalg.inv(A)))),1/(2*np.sin(np.pi/18)))

# 2024 P1: the rank-one solver, including its singular edge case.
rng=np.random.default_rng(20261014)
A=rng.normal(size=(6,6))+6*np.eye(6)
u,v,b=rng.normal(size=(3,6))
p=np.linalg.solve(A,u);z=np.linalg.solve(A,b)
x=z-p*(v@z)/(1+v@p)
assert_allclose((A+np.outer(u,v))@x,b,atol=1e-12)
v=-p/(p@p)
assert_allclose((A+np.outer(u,v))@p,0,atol=1e-12)

# 2015 P2(a): compare block eigenvalues with the SVD formula.
A=rng.normal(size=(7,4));alpha=.7
C=np.block([[alpha*np.eye(7),A],[A.T,np.zeros((4,4))]])
s=np.linalg.svd(A,compute_uv=False)
expected=np.r_[alpha/2+np.sqrt(alpha**2/4+s*s),alpha/2-np.sqrt(alpha**2/4+s*s),[alpha]*3]
assert_allclose(np.linalg.eigvalsh(C),np.sort(expected),atol=1e-12)

# 2025 P4 and 2012 P4(3): exact residual-energy identities.
Y=rng.normal(size=(7,5));U,s,_=np.linalg.svd(Y,full_matrices=False)
W=U[:,:2]
assert_allclose(np.linalg.norm(Y-W@W.T@Y,'fro')**2,np.sum(s[2:]**2))
Yc=Y-Y.mean(axis=1,keepdims=True);U,s,_=np.linalg.svd(Yc,full_matrices=False)
W=U[:,:2];R=W.T@Yc
assert_allclose(np.linalg.norm(Y-Y.mean(axis=1,keepdims=True)-W@R,'fro')**2,np.sum(s[2:]**2))

# 2025 P1: derive the leading error coefficient independently.
e,c2,c3=sp.symbols('e c2 c3')
f=e+c2*e**2+c3*e**3
fp=sp.diff(f,e)
y=sp.series(e-sp.Rational(1,2)*f/fp,e,0,4).removeO()
error=sp.series(e-f/fp.subs(e,y),e,0,4).removeO().expand()
assert sp.simplify(error-(c2**2-c3/4)*e**3)==0

# 2017 P2(a): nondegenerate acceleration and the missing-assumption example.
a,bb=sp.symbols('a bb')
g=a*e+bb*e**2
gg=sp.expand(a*g+bb*g**2)
error=sp.series(e-(g-e)**2/(gg-2*g+e),e,0,3).removeO()
assert sp.simplify(error-a*bb/(a-1)*e**2)==0
g=e-e**3;gg=sp.expand(g-g**3)
error=sp.series(e-(g-e)**2/(gg-2*g+e),e,0,3).removeO()
assert sp.simplify(error-sp.Rational(2,3)*e)==0

print('Selected Yau problem checks passed: spectra, rank-one update, SVD, projection, convergence expansions.')
