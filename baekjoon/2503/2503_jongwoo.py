import sys
from itertools import combinations, permutations

# 모든 경우의 수를 구한 후 
# 영수의 답을 보고 소거해나가는 방식으로 풀어보자
permutation_list = list(permutations(range(1, 10), 3))
print(permutation_list)

n = int(sys.stdin.readline())

for _ in range(n):
    number, strike, ball = map(int, sys.stdin.readline().split())

    print(number, strike, ball)

    hundred_idx = number // 100
    ten_idx = (number % 100) // 10
    one_idx = number % 10

    num_list = [ x for x in range(1, 10)]
    print(num_list)
    # 경우 1. Strike : 0, Ball : 0

    num_list.remove(hundred_idx)
    num_list.remove(ten_idx)
    num_list.remove(one_idx)

    case_1 = list(permutations(num_list, 3))

    result = set(permutation_list, case_1)

    # 경우 2. Strike : 0, Ball : 1
    # 경우 3. Strike : 0, Ball : 2
    # 경우 4. Strike : 0, Ball : 3
    # 경우 5. Strike : 1, Ball : 0
    # 경우 6. Strike : 1, Ball : 1
    # 경우 7. Strike : 1, Ball : 2
    # 경우 8. Strike : 2, Ball : 1
    # 경우 9. Strike : 3, Ball : 0
        