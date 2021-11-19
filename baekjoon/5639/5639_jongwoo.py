import sys
sys.setrecursionlimit(10 ** 6)

preorder_list = []

while True:
    try:
        preorder_list.append(int(sys.stdin.readline()))
    except:
        break

def postorder(start, end):
    # 종료 조건
    if start > end:
        return

    # 변수 초기화
    # root : 해당 트리의 루트 노드 값
    # right_idx  해당 트리의 오른족 서브 트리 인덱스
    root = preorder_list[start]
    right_idx = start + 1

    # 루트보다 큰 값의 인덱스 찾기 (오른쪽 서브트리)
    for i in range(start + 1, end + 1):
        right_idx = i
        if preorder_list[i] > root:
            break

    # print(f'root : {root}, right_idx : {right_idx}, right_val : {preorder_list[right_idx]}')

    # 왼쪽, 오른쪽 서브트리에 대해서 재귀적으로 다시 트리를 타고 들어감
    # 후위순회 (왼쪽, 오른쪽, 루트)
    postorder(start + 1, right_idx - 1)
    postorder(right_idx, end)

    print(root)

postorder(0, len(preorder_list) - 1)

# print(preorder_list)