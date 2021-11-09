import sys
from itertools import permutations

num = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))
result = 0

p = list(permutations(arr, num))

for i in p:
    temp = 0
    # print(i)
    list_i = list(i)

    for j in range(num-1):
        temp += abs(list_i[j] - list_i[j+1])

    if temp > result:
        result = temp

print(result)
