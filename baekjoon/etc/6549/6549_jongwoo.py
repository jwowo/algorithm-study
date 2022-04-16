import sys

def using_stack(histograms):
    stack = []
    answer = 0

    for i in range(n):
        while len(stack) != 0 and stack[-1][1] > histograms[i]:
            height = stack.pop()[1]

            if len(stack) == 0:
                width = i
            else:
                width = i - stack[-1][0] - 1

            answer = max(answer, width * height)
        stack.append([i, histograms[i]])

    while len(stack) != 0:
        height = stack.pop()[1]

        if len(stack) == 0:
            width = n
        else:
            width = n - stack[-1][0] - 1
        answer = max(answer, width * height)

    return answer


"""
중간값 mid 찾고
0 ~ mid -> divide_conquer(left)
mid + 1 -> divide_conquer(right)

어짜피 한개가 최대값일 경우는 분할정복을 통해서 찾게 되므로 
중간에 겹치는 부분의 밑변 길이가 2일때부터 
왼쪽, 오른쪽 각각에 대해 최대한 움직일 수 있는 만큼 움직여서 max값 확인해본다.

마지막에 max(divide_conquer(left), mid_max_aream divide_conquer(right)) 를 하여 
각각의 값의 최댓값 확인
"""
def divide_conquer(histograms):
    if len(histograms) == 1:
        return histograms[0]

    else:
        mid_idx = len(histograms) // 2
        left = histograms[:mid_idx]
        right = histograms[mid_idx:]

        left_idx = mid_idx - 1
        right_idx = mid_idx

        mid_height = min(histograms[left_idx], histograms[right_idx])
        mid_width = 2
        mid_area = mid_height * mid_width
        
        while not (left_idx == 0 and right_idx == len(histograms) - 1):
            current_height = 0
            
            if left_idx == 0:
                right_idx += 1
                current_height = histograms[right_idx]
            
            elif right_idx == len(histograms) - 1:
                left_idx -= 1
                current_height = histograms[left_idx]
            
            elif histograms[left_idx - 1] > histograms[right_idx + 1]:
                left_idx -= 1
                current_height = histograms[left_idx]
            
            else:
                right_idx += 1
                current_height = histograms[right_idx]

            mid_height = min(mid_height, current_height)
            mid_width += 1
            mid_area = max(mid_area, mid_height * mid_width)

        return max(divide_conquer(left), mid_area, divide_conquer(right))

while True:
    histograms = list(map(int, sys.stdin.readline().split()))
    n = histograms[0]
    histograms = histograms[1:]

    if n == 0:
        break

    # answer = using_stack(histograms)
    # print(answer)

    answer2 = divide_conquer(histograms)
    print(answer2)

