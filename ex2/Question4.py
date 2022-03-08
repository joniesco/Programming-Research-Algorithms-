import sys
import math
"""A question named horse race - toked from https://www.codingame.com/  """
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
answer= math.inf
list=[]
n = int(input())
for i in range(n):
    pi = int(input())
    list.append(pi)

list =sorted(list)
for i in range(len(list) - 1):
    if list[i + 1] - list[i] < answer:
        answer = list[i + 1] - list[i]

print(answer)
