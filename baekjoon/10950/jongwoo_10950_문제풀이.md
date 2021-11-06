문제 주소
=====================
<https://www.acmicpc.net/problem/10950>

문제 접근 방법
=====================
첫째 줄에 테스트 케이스의 개수가 입력되므로  
테스트 케이스의 수만큼 반복문을 돌면서  
두 수를 입력받아  
두 수의 합을 출력한다.  

## 코드

```
t = int(input())

for i in range(t):
    a, b = map(int, input().split() )
    print( a + b)
```
