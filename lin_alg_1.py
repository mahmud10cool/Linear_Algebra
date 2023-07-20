# Proving the Cauchy-Schwarz inequality.
# Condition for equality is that the two vectors are exactly equal (identical).

import numpy as np

# create three vectors, one of which is dependent on another
a = np.random.randn(5)
b = np.random.randn(5)
c = np.random.randn(1) * a

# computer their dot products
aTb = np.dot(a,b)
aTc = np.dot(a,c)

# demonstrate the (in)equalities
print(f'{np.abs(aTb):.4f}, {np.linalg.norm(a)*np.linalg.norm(b):.4f}')
print(f'{np.abs(aTc):.4f}, {np.linalg.norm(a)*np.linalg.norm(c):.4f}')

