문제 주소
=====================
<https://www.acmicpc.net/problem/9498>

문제 접근 방법
=====================
변수를 입력받아 정수형으로 저장한다.  

if, elif, else 문을 통해 조건에 맞게 시험 성적을 출력한다.
## 코드

```
score = int(input())

if score  >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('F')
```
