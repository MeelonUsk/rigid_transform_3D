from numpy import *
from math import sqrt

from rigid_transform_3D import rigid_transform_3D

# Test with random data

# Random rotation and translation
R = array([[0, 1, 0], [0, 0, 1], [1, 0, 0]]) 
t = array([[0], [0], [10]])

# make R a proper rotation matrix, force orthonormal
U, S, Vt = linalg.svd(R)
R = dot(U, Vt)

# remove reflection
if linalg.det(R) < 0:
   print('adjusting for reflection')
   Vt[2,:] *= -1
   R = dot(U, Vt)

# number of points
n = 3

# A = mat(random.rand(3, n));
A = transpose(array([[0, 0, 0], [0, 1, 0], [0, 2, 0], [0, 3, 0]]))
B = transpose(array([[0, 0, 10], [0, 1, 10], [0, 2, 10], [0, 3, 10]]))

# Recover R and t
ret_R, ret_t = rigid_transform_3D(A, B)

# Compare the recovered R and t with the original
B2 = dot(ret_R, A) + ret_t

# Find the root mean squared error
err = B2 - B
err = multiply(err, err)
err = sum(err)
rmse = sqrt(err/n);

print("Points A")
print(A)
print("")

print("Points B")
print(B)
print("")

print("Ground truth rotation")
print(R)

print("Recovered rotation")
print(ret_R)
print("")

print("Ground truth translation")
print(t)

print("Recovered translation")
print(ret_t)
print("")

print("RMSE:", rmse)

if rmse < 1e-5:
    print("Everything looks good!\n");
else:
    print("Hmm something doesn't look right ...\n");
