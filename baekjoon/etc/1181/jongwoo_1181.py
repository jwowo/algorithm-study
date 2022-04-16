# 문제 접근 방법
# 1. 첫째줄에 단어의 개수 N
# 2. 소문자로 이루어진 N개의 단어
#   2-1. 길이가 짧은 것 부터
#   2-2. 길이가 같으면 사전 순으로 
# 3. 주어지는 문자열의 길이는 50 넘지 않는다.
# 4. 단어의 개수 1 <= N <= 20,000
# 5. 같은 단어 여러번 입력된 경우 한번만 출력

# 문제 이해 시간 : 2021-11-09 2:25pm - 2:30pm
# 풀이 생각 시간 : 2021-11-09 2:30pm - 2:45pm
# 코딩 시간 : 2021-11-09 2:30pm - 2:45pm - 3:36pm
# 디버깅 시간 : 

# 단어의 길이가 같을 시, 사전순으로 배치 -> sort() 내장 함수
# 중복 단어 허용 X -> set
# 단어를 입력받았을 시 짧은 것이 우선 -> sort key 및 lambda 이용

import sys

num = int(sys.stdin.readline())
arr = []

for _ in range(num):
    arr.append(sys.stdin.readline().strip())

arr = list(set(arr))

arr.sort(key=lambda x : (len(x), x))

for i in range(len(arr)):
    print(arr[i])