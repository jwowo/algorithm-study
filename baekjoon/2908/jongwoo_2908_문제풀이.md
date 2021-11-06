<https://www.acmicpc.net/problem/2908>

문제 접근 방법
=====================
입력을 문자열로 저장하고,  
문자열을 역순으로 재배치한 후,  
대소비교를 통해 더 큰 수를 출력한다.  

## 코드

```python
a, b = input().split()

a_reverse = a[::-1]
b_reverse = b[::-1]

if a_reverse > b_reverse:
    print(a_reverse)
else:
    print(b_reverse)
```
