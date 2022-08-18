"""

"""
# Method 1
x, k = list(map(int, input().split()))
def polinomial_(x, k):
    res = 0
    for i in range(k, 0,-1):
        res += x ** i
    if res == k:
        return "True"

print(polinomial_(x, k))
# 2 fail

# Method 2
x, k = list(map(int, input().split()))
p = input()
res = eval(p)
if res == k:
    print("True")
else:
    print("False")

# all test case pass
