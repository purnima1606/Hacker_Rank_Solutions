"""

"""
n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
avg_sc = sum(student_marks[query_name])/ len(student_marks[query_name])
print(format(avg_sc, ".2f"))
