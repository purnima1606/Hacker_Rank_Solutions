"""

"""
import numpy
N = int(input())
A = []
for _ in range(N):
    A.append(list(map(float, input().split())))
det_ = numpy.linalg.det(A)
print(round(det_, 2))
# print(round(numpy.linalg.det(A)), 2)  # Error
