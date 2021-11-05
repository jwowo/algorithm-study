문제 주소
=====================
<https://www.acmicpc.net/problem/2739>

문제 접근 방법
=====================
숫자를 입력받고 1~9까지 반복문을 돌면서 구구단 값 출력

## 코드

```
n = int( input() )

for i in range(1, 10):
    print(f'{n} * {i} = { n * i }')
```
