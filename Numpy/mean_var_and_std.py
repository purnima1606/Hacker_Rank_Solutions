"""

"""

import numpy
N, M = list(map(int, input().split()))
my_array = []
for _ in range(N):
    my_array.append(list(map(int, input().split())))
print(numpy.mean(my_array, axis = 1))
print(numpy.var(my_array, axis = 0))
std_ = numpy.std(my_array)
print(round(std_, 11))

# print(round(numpy.std(my_array)), 11)   # Error
