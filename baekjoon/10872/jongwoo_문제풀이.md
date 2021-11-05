문제 주소
=====================
<https://www.acmicpc.net/problem/10872>

문제 접근 방법
=====================
1. 정수 n을 입력받는다.
2. 2부터 n까지 차례로 곱한 뒤 그 값을 출력한다.

## 코드

```python
n = int(input())

result = 1
for i in range(2, n + 1):
    result *= i

print(result)
```
