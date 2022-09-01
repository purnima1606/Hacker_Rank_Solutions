"""

"""
cube = lambda x: x ** 3 # complete the lambda function

def fibonacci(n):
    a, b, c = 0, 1, 0
    res = []
    for _ in range(n):
        res.append(a)
        c = a + b
        a = b
        b = c
    return res
    # return a list of fibonacci numbers

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
