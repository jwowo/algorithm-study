문제 주소
=====================
<https://www.acmicpc.net/problem/9020>

문제 접근 방법
=====================
1. 길이가 10,001 인 에라테라토스의 체 배열 생성  
( 소수 일 경우 값에 True, 소수가 아닐 경우 값에 False )  
2.  입력받은 테스트 케이스 ( t )의 골드바흐 파티션이 여러가지인 경우,  
두 소수의 차이가 가장 작은 것을 출력하므로,  
2-1. 입력받은 테스트 케이스(t)를 2로 나누고 2로 나눈 수(x) 부터 테스트 케이스까지 1 씩 증가하면서
2-2. x 와 ( t - x ) 모두 소수일 때 두 값을 출력하고 반복문을 종료한다.

## 코드

```python
n = int(input())

# 에라테라토스의 체 생성
eratos = [ True for _ in range(10001) ]

# 에라테라토스의 체 초기화
for i in range(2, 10001):
    if eratos[i] == False:
        continue
    for j in range(i+i, 10001, i):
        eratos[j] = False

for _ in range(n):
    # 테스트 케이스
    t = int(input())

    # t의 가능한 골드바흐 파티션이 여러 가지일 경우,
    # 두 소수의 차이가가장 작은 것을 출력하기 위해 반으로 나눈다.
    start = t // 2

    for num1 in range(start, t):
        num2 = t - num1
        if eratos[num1] == True and eratos[num2] == True:
            print(num2, num1)
            break
```
