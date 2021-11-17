import sys

n = int(sys.stdin.readline())

def check_connection(coordinates):
    stack = []
    count = 1   # 원이 없어도 공간 하나는 있음

    for circle_type, coordinate in coordinates:
        # print(f'현재 좌표 : {coordinate}')
        # 원의 시작점이면 무조건 삽입
        if circle_type == 0:
            stack.append([circle_type, coordinate])

        # ***** 스택 문제는 pop() 할 때 어떤 조건을 만족하는지 연산, 확인 하는 과정이 중요 *****
        #
        # else: 
        #   원의 시작점이 아니라면 pop 할건데
        #   pop한 요소가 원이냐? 원의 시작점이냐? 가 중요
        #       -> 내 원의 시작 좌표와 내 원의 끝 좌표 사이에 원이 있다는 말은
        #       -> 스택에 쌓여있는 원들이 내 원 안에 속해있다는 의미 
        # 
        #   원이면 원인 것들을 계속 pop 하여 
        #       지름 정보를 (inner_circle)계속 더하여 저장 (겹쳐져있지 않기 때문에 가능)
        #      
        #   내 원(new_circle)의 시작점이 나오면 
        #       (원의 끝점 좌표 - 원의 시작점 좌표) 를 통해 내 원의 지름 구함
        #   
        #   내 원의 지름 vs 스택에 저장되어 있던 이전 원(inner_circle)들의 지름의 합을 비교하여
        #       지름이 같으면 이어져있다는 의미이므로 count += 2 
        #       아니면 이어져있지 않다는 의미이므로 count += 1
        #   
        #   그럼 내 원안에 속해있는 원에 대한 연속성 조사는 끝남
        #   내 원이 다른 큰 원안에 속해있는 작은 원일 수 있으므로 ( 2 (원임을 알려줌) , 원의 지름) 정보를 스택에 저장

        else:
            inner_circle = 0
            while stack and stack[-1][0] == 2:
                inner_circle += stack.pop()[1]

            new_circle = coordinate - stack.pop()[1]
            if new_circle == inner_circle:
                count += 2
            else:
                count += 1

            stack.append([2, new_circle])
            
    return count

coordinates = []

for _ in range(n):
    x, r = map(int, sys.stdin.readline().split())
    coordinates.append([0, x - r])
    coordinates.append([1, x + r])

coordinates.sort(key = lambda x : -x[0])
coordinates.sort(key = lambda x : x[1])

answer = check_connection(coordinates)

print(answer)