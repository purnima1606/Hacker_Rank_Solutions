"""

"""
s = input()
l,u,e,o = "", "", "", ""
for i in s:
    if i.isalpha():
        if i.islower():
            l += i
        else:
            u += i
    elif i.isdigit():
        if int(i) % 2 == 0:
            e += i
        else:
            o += i
print("{}{}{}{}".format("".join(sorted(l)), "".join(sorted(u)), "".join(sorted(o)), "".join(sorted(e))))
