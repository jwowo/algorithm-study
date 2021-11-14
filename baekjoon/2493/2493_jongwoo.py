
import sys

# 탑의 개수
n = int(sys.stdin.readline().strip())
towers = list(map(int, sys.stdin.readline().split()))

stack = []
ans = []

"""
문제에서 주어진 왼쪽부터 읽는 것이 아니라 왼쪽부터 읽는 방법이 없을까 생각!?
빈 리스트 선언 후, 왼쪽부터 값을 삽입하면서 의미 없는 탑들은 제거하는 방식은 어떨까?
의미 없는 탑 : 나보다 높이가 낮은 탑들 (어짜피 나보다 낮은 탑에서 레이저에 걸릴 탑은 내가 대신 레이저 맞는다)

stack = [] :  최댓값을 저장할 스택 
(인덱스와 값 을 스택에 push -> ans배열에 인덱스를 저장해야하고, 최댓값 비교를 위해서는 높이도 저장되어 있어야한다.)
answer = [] : 수신탑 인덱스 저장

첫 인덱스부터 돌면서 
만약 stack의 마지막 원소와 자기 자신의 타워 비교
    자기 자신의 높이가 stack 마지막 원소보다 높다면
        0 될 때까지 pop()
        중간에 자기보다 높은 타워 만나면 ans[] 배열에 해당 타워 인덱스 넣기

    stack의 높이가 더 높다면
        해당 타워 인덱스 ans[]배열에 넣고 현재 타워 stack에 넣기
"""
for i in range(n):
    while stack:
        if stack[-1][1] > towers[i]:
            ans.append(stack[-1][0] + 1)
            break
        else:
            stack.pop()
    
    if not stack:
        ans.append(0)

    stack.append( [i, towers[i] ] )

print(" ".join(map(str, ans)))