문제 주소
=====================
<https://www.acmicpc.net/problem/8958>

문제 접근 방법
=====================
연속으로 문제를 맞출때마다 문제의 점수가 1 씩 증가하므로  
문제를 맞췄을때는 전체 점수에 현재 문제의 점수를 더하고, 다음 문제를 위해 현재 문제 점수를 + 1 한다.  
문제를 틀렸을때는 현재 문제의 점수를 다시 1 로 변경한다.  

## 코드

```
n = int(input())

for i in range(n):
    current_score = 1
    total_score = 0
    q = input()
    for i in q:
        if i == 'O':
            total_score += current_score
            current_score += 1
        else:
            current_score = 1
    print(total_score)
```
