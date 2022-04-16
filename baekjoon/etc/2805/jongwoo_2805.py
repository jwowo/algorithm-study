"""
문제접근 방법

이진 탐색으로 자르는 목재절단기의 높이를 
바닥(0)에서부터 가장 높이가 큰 나무(max_height)의 
반을 나눈다.

목재절단기로 나무를 잘랐을때 상근이가 가져가는 나무의 양과
상근이가 필요한 나무의 양을 비교하여

부족하면 목재 절단기의 높이를 낮추고
남으면 목재 절단기의 높이를 높인다. 
"""

import sys

# n = 나무의 수, m = 필요한 나무의 길이, trees = 나무들의 높이
n, m = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

def get_tree(trees, start, end, target):
    """"
    Args
        trees   (list)  : 나무들의 높이가 주어진 배열
        start   (int)   : 이진 탐색의 시작 인덱스
        end     (int)   : 이진 탐색의 마지막 인덱스
        target  (int)   : 필요한 나무의 길이 
    Returns
        (int) 필요한 나무를 가져갈 수 있는 전기톱의 최대 높이
    """
    if start > end:
        return
    
    cut_height = (start + end) // 2
    amount = 0

    for tree in trees:
        if tree > cut_height:
            amount += (tree - cut_height)

    if amount == target:
        height_list.append(cut_height)
        return 
    elif amount > target:
        height_list.append(cut_height)
        return get_tree(trees, cut_height + 1, end, target)
    else:
        return get_tree(trees, start, cut_height - 1, target)

height_list = []
max_height = max(trees)

get_tree(trees, 0, max_height, m)

print(max(height_list))