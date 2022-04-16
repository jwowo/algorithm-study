# import sys
# from itertools import combinations

# while True:
#     arr = list(map(int,sys.stdin.readline().split()))
#     n = arr[0]
#     arr = arr[1:]

#     if n == 0:
#         break

#     combination_list = (list(combinations(arr, 6)))

#     for c  in combination_list:
#         print(' '.join(map(str, c)))
    
#     print()


import sys

def recursion(start, k):
    if k == 7:
        print(' '.join(map(str, result)))

    else:
        for i in range(start, len(arr)):
            flag = True

            if arr[i] in result:
                
                flag = False

            if flag:
                result.append(arr[i])
                recursion(i, k + 1)
                result.pop()

while True:
    arr = list(map(int,sys.stdin.readline().split()))
    n = arr[0]
    arr = arr[1:]

    result = []

    if n == 0:
        break

    # print(n)
    # print(arr)

    recursion(0, 1)
    print()
        

    