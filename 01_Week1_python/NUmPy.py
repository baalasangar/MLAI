# -*- coding: utf-8 -*-

import numpy as np
mat = np.arange(0, 15).reshape((3, 5))
print(mat)

# Will return the dimension of the matrix
mat.shape

# Dimesion of the matrix
mat.ndim

# size of the matrix ( rows * columns)
mat.size

# Different way of creating Vector / matrix

vector = np.array([1, 2, 3, 4])
vector

matrix = np.array([(1, 2, 3), (2, 3, 4)])
matrix


# arang(start->inclusion,stop->exclusion,step,dtype)
# in the below case 15 is not counted out
np.arange(0, 15)

# Create the matrix of zero value
np.zeros((2, 3))

# zeros_like() returns the  matrix of zero with the same size of input matrix
inputmat = np.arange(0, 15).reshape((3, 5))
np.zeros_like(inputmat)
# Create the matrix of Ones
np.ones((3, 2))
np.ones_like(inputmat)
# Create a matrix with the random values
np.empty((3, 5), dtype=int)
np.empty_like(inputmat)
# Return evenly spaced numbers over a specified interval.
np.linspace(2, 3, 10)


# Matrix / Vector  - created using random variable
np.random.rand(4)  # Vector
np.random.rand(2, 3)  # Matrix

np.random.randn(4)  # standard normal random variable

np.mean(np.random.rand(2, 3))
np.std(np.random.rand(2, 3))
# min / max


# access entries in a numpy vector
rand_vector = np.random.rand(10)
rand_vector
rand_vector[5]  # return the 5th element
rand_vector[1:4]  # return 1 to 3rd element
rand_vector[:]  # return all the elements in array
rand_vector[rand_vector > 0.5]  # return the element which are created than 0.5
rand_vector > 0.5
rand_vector[[1, 2, 5]]  # return 1,2,5 th element

rand_mat = np.random.rand(5, 6)
rand_mat
rand_mat[4]  # retuns the fifth row of matrix
rand_mat[4, :]  # reurns the fourth row
rand_mat[:, 3]  # returns the 3 row
rand_mat[1:2, 2:4]  # will return the first row second and third element
rand_mat[rand_mat > 0.5]  # result will be vector

# let's change some values in an array!

rand_mat[1:2, 2:4] = 0  # first row second and third element is set to zero
rand_mat[1:2, 2:4] = [1, 2]
sub_mat = rand_mat[1:3, 2:4]
sub_mat
sub_mat[:] = 0  # rand_mat is also updated with the change to avoid it use copy()
sub_mat2 = rand_mat[1:3, 2:4].copy()
sub_mat2[:] = 0

# Saving the Matrix
np.save('mat_file', rand_mat)
np.load('mat_file.npy')

np.savez("mat_zip_file", sub_mat_var = sub_mat,
         rand_mat_var = rand_mat ,
         sub_mat2_var = sub_mat)

zip_mat = np.load("mat_zip_file.npz")
zip_mat["rand_mat_var"]

np.savetxt("text_mat_file.txt", rand_mat, delimiter=',')
text_mat = np.loadtxt("text_mat_file.txt", delimiter=',')
text_mat


# Linear Algebra Basic

# Matrix - Vector operation

mat1 = np.arange(0, 5).reshape(1, 5)
mat2 = np.arange(0, 5).reshape(5, 1)
result = np.matmul(mat2, mat1)

#np.linalg.solve(mat1, result)

mat3 = np.random.randint(1, 5, (3, 2))
vec1 = np.random.randint(0, 10, (2, 1))
np.matmul(mat3, vec1)

mat4 = np.random.randint(1, 5, (2, 3))

np.matmul(mat3, mat4)
np.matmul(mat4, mat3)

mat5 = np.random.randint(1, 5, (3, 2))

mat3 + mat5

# Transpose of Matrix
matrix.T

# method to create Identity Matrix  
np.eye(3)

np.dot(mat3, mat4)


A = np.random.random((10000, 101))
A.shape
B = np.random.random((100, 1001))
np.matmul(A, B).shape





