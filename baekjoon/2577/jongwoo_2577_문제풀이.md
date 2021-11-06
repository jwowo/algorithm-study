문제 주소
=====================
<https://www.acmicpc.net/problem/2577>

문제 접근 방법
=====================
세 개의 자연수를 각각 A, B, C 에 저장한다.  
세 자연수를 곱한뒤 string 타입으로 변경한다.  
반복문을 0부터 9까지 돌면서  
python의 count()메서드를 통해 해당 숫자가 몇 번 사용되었는지 개수를 출력한다.


## 코드

```
A = int(input())
B = int(input())
C = int(input())

result = str(A * B * C)

for i in range(10):
    print( result.count(str(i)) )
```
