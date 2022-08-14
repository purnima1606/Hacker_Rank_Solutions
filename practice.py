# *********************************** Sorting Techniques ********************************************

"""
The different implementations of sorting techniques in Python are:

1.Bubble Sort
2.Selection Sort
3.Insertion Sort : reverse check

"""


l = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
#
# # Method Bubble sort :-
#
# for i in range(len(l)-1):
#     for j in range(len(l)-1):
#         print(l[j], l[j+1])
#         if l[j] > l[j+1]:
#             l[j],l[j+1] = l[j+1], l[j]
#
#
#         # print(l)
#
# print(l)   # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


#
# # Method Selection Sort :-


# for  i in range(len(l)-1):
#     for j in range(i+1, len(l)):
#         if l[i] > l[j]:
#             l[i], l[j] = l[j], l[i]
#     print(l)

# print(l)
# # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Method Insertion Sort :-

# for i in range(len(l)-1):
#     if l[i] > l[i+1]:
#         l[i], l[i+1] = l[i+1], l[i]
#     for j in range(i, 0, -1):
#         if l[j] < l[j-1]:
#             l[j], l[j-1] = l[j-1], l[j]
#
# print(l)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


