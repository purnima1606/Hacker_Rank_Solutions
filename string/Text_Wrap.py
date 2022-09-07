"""
Check Tutorial tab to know how to to solve.

You are given a string S and width W.
Your task is to wrap the string into a paragraph of width .

Function Description

Complete the wrap function in the editor below.

wrap has the following parameters:

* string string: a long string
* int max_width: the width to wrap to

Returns
* string: a single string with newline characters ('\n') where the breaks should be

Input Format
The first line contains a string,string .
The second line contains the width,maxwidth .

Constraints
0 < len(string) < 1000
0 < max_width < len(string)

Sample Input 0

ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
Sample Output 0

ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
"""

import textwrap

def wrap(string, max_width):
    # res =""
    # l = 0
    # for i in string:
    #     if l <= max_width:
    #         res += i
    #         l += 1
    #     else:
    #         res +=  "\n" + i
    #         l = 0
    return textwrap.fill(string, max_width)
    #  return textwrap.fill(string, max_width)       # return list()

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
