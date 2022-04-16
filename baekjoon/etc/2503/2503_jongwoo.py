# import sys
# from itertools import permutations

# # 모든 경우의 수를 구한 후 
# # 영수의 답을 보고 소거해나가는 방식으로 풀어보자
# permutation_list = list(permutations(range(1, 10), 3))
# # print(permutation_list[0])
# # print(permutation_list[0][0])
# # print(f'type : {type(permutation_list[0])}')
# # print(f'조합의 개수 : {len(permutation_list)}')

# n = int(sys.stdin.readline())

# # 504 가지 경우에 대해서 number와 비교하여
# # strike와 ball의 경우가 같은 경우에만 남기고 아닌 경우 요소 삭제
# def check_validation(permutation_list, number, strike, ball):
#     """
#         permutation_list (tuple) : 가능한 경우의 수 조합
#         number (tuple) : 민혁이가 물어본 3자리 숫자 조합
#         strike (int) : 자리수와 값이 완전 동일한 경우의 수
#         ball (int) : 값은 있지만 자리수가 다른 경우의 수
#     """

#     # 남아 있는 모든 경우의 수에 대하여 
#     # 입력받은 수와 비교하여 strike와 ball의 개수 센다.    
#     # is_valid = [0] * len(permutation_list)
    
#     for case in permutation_list:
        
#         for case_idx, case_val in enumerate(case):
#             current_strike = 0
#             current_ball = 0

#             for n_idx, n_val in enumerate(number):
#                 # count strike & ball
#                 if case_val == n_val:
#                     # count strike
#                     if n_idx == case_idx:
#                         current_strike += 1
#                     # count ball
#                     else:
#                         current_ball += 1

#             # print(f'case : {case}, current_strike : {current_strike}, current_ball : {current_ball}')

#         if case in permutation_list:
#             if not current_ball == ball or not current_strike == strike:
#                 permutation_list.remove(case)


# for _ in range(n):
#     number, strike, ball = map(int, sys.stdin.readline().split())

#     number = tuple(map(int, str(number)))

#     print(f'tuple number : {number}')
#     check_validation(permutation_list, number, strike, ball)


# print(f'결과 : {len(permutation_list)}')

# print(permutation_list)

import sys
from itertools import permutations

possible_list = list(permutations(range(1, 10), 3))
n = int(sys.stdin.readline())

is_valid = [ True ] * len(possible_list)

def check_validation(possible_list, question, strike, ball):
    
    for i in range(len(possible_list)):
        possible_case = possible_list[i]
        
        current_strike = 0
        current_ball = 0

        for j in range(3):
            if str(possible_case[j]) == str(question[j]):
                current_strike += 1
            elif possible_case[j] in question:
                current_ball += 1

        if current_strike != strike or current_ball != ball:
            is_valid[i] = False

for _ in range(n):
    number, strike, ball = map(int, sys.stdin.readline().split())
    question = tuple(map(int, str(number)))

    # print(f'tuple number : {number}')
    check_validation(possible_list, question, strike, ball)

print(sum(is_valid))