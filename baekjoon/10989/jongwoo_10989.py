"""
import sys

num = int(sys.stdin.readline())
arr = []

def counting_sort(arr):
    # count = [ 0 for _ in range(max(arr) + 1)]
    count = [0] * (max(arr) + 1)
    print(sys.getsizeof(count))
    for i in range(len(arr)):
        count[arr[i]] += 1
        
    # for i in range(len(count)):
    #     print((str(i) + '\n') * count[i])

#    for idx, val in enumerate(count):


for _ in range(num):
    arr.append(int(sys.stdin.readline()))
    
counting_sort(arr)
"""

import sys

num = int(sys.stdin.readline())
count = [0] * 10001

for _ in range(num):
    count[int(sys.stdin.readline())] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i)

print(sys.getsizeof(count[0]))
print(sys.getsizeof(count))
