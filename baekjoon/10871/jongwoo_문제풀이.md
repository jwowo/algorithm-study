< 알고리즘 문제풀이.md 양식 >

문제 주소
=====================
<https://www.acmicpc.net/problem/10871>

문제 접근 방법
=====================
첫째 줄에 입력된 n만큼 반복문을 돌면서  
정수x와 수열a의 값을 차례로 비교하여  
x보다 작으면 출력한다.

## 코드

```
n, x = map(int, input().split())

a = list(map(int, input().split()))

for i in range(n):
    if a[i] < x:
        print(a[i], end=' ')

```
