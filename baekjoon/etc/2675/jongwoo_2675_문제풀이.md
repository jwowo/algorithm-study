<https://www.acmicpc.net/problem/2675>

문제 접근 방법
=====================
문자열 s를 입력받고 문자열의 각 인덱스를 돌면서 s번 출력한다.
출력시 end=''로 하여 개행되지 않도록 주의한다.

## 코드

```python
t = int(input())

for _ in range(t):
    r, s = input().split()

    for i in s:
        print(i * int(r), end='')
    print()문제 주소
```
