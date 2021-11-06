문제 주소
=====================
<https://www.acmicpc.net/problem/1978>

문제 접근 방법
=====================
# 에라토스테네스의 체 ( 소수 찾기 ) 공부하기
# 1. 이차원 배열 생성하여 값 초기화
# 2. 2부터 시작해서 특정 숫자의 배수에 해당하는 숫자들을 모두 지운다.
# 3. 이미 지워진 숫자의 경우 건너뛴다.
# 4. 2부터 시작하여 남아있는 숫자들 출력한다.


## 코드

```python
n = int(input())
nums = list(map(int, input().split()))

count = 0

primeSeive = [ True for _ in range(1001) ]
primeSeive[1] = False

for i in range(2, 1001):
    if primeSeive[i] == False:
        continue
    for j in range(i+i, 1001, i):
        primeSeive[j] = False

for num in nums:
    if primeSeive[num] == True:
        count += 1

print(count)
```

