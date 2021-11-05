문제 주소
=====================
<https://www.acmicpc.net/problem/4344>

문제 접근 방법
=====================
각 케이스를 하나의 배열에 저장하나
배열의 첫번째 인덱스는 학생의 수이고  
두번째 인덱스부터 마지막 인덱스까지는 각 학생의 점수이다.
두번째 인덱스부터 마지막 인덱스까지 합하여 첫번째 인덱스인 학생의 수로 나눠서  
학생들의 점수의 평균 값을 구하고

그 평균값을 이용하여 평균을 높는 학생의 비율을 반올림하여 출력한다.  
출력시에 파이썬의 f-string 표기법을 이용하여 소수점 자리수를 지정한다.

## 코드

```
n = int(input())

for i in range(n):
    scores = list(map(int, input().split()))

    avg_score = sum(scores[1:]) / scores[0]
    count = 0

    for score in scores[1:]:
        if score > avg_score:
            count += 1

    avg_rate = (count / scores[0]) * 100

    print(f'{avg_rate:.3f}%')
```
