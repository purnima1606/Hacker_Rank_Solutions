"""
"""

N, X = list(map(int, input().split()))
arr = []
for _ in range(X):
    arr.append(list(map(float, input().split())))
res = zip(*arr)
for marks in res:
    avg_sc = sum(marks) / len(marks)
    print(avg_sc)
    
