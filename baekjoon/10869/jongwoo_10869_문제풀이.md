문제 주소
=====================
<https://www.acmicpc.net/problem/10869>

문제 접근 방법
=====================
두 개의 input을 int형으로 변환하여 각각 A, B에 저장한 뒤 사칙연산을 수행했다.

## 코드

```
A, B = map(int, input().split())

print(A+B)
print(A-B)
print(A*B)
print(A//B)
print(A%B)
```
