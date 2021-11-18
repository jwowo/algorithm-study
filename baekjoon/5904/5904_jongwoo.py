"""Moo 게임
이 문제는 입력 n이 10억(10^9)이므로 시간복잡도가 O(N)이어도 10초
S(n)를 구할때,
n이 0 ~ S(n-1) (처음 구간) 인지?
    S(n-1) ~ S(n-1) + 1 + (n + 2) (중간 구간) 인지?
    마지막 구간인지?
확인하고, 해당 구간만 재귀적으로 문제를 푼다.
그러려면 일단 S(n-1)의 길이를 알아야한다.
"""



import sys

n = int(sys.stdin.readline())

def get_index(n):
    if n == 0:
        return 3

    else:
        return get_index(n - 1) + 1 + (n + 2) + get_index(n - 1)

def divide_conquer(n, k):
    pre_length = get_index(n - 1)

    if n <= 3:
        if n == 1:
            return 'm'
        else:
            return 'o'

    # 처음 구간
    elif n <= pre_length:
        divide_conquer(n - 1, k)
    # 중간 구간
    elif pre_length < n and n <= pre_length + 1 + (n + 2):
        if n == pre_length + 1:
            return 'm'
        else:
            return 'o'
    
    # 끝 구간
    else: 
        divide_conquer()
