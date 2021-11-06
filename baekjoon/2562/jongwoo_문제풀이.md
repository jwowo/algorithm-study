문제 주소
=====================
<https://www.acmicpc.net/problem/2562>

문제 접근 방법
=====================
list comprehension을 통해 9개의 자연수를 배열에 저장한다.  
python 내장함수 max를 이용하여 배열에서 가장 큰 값을 찾고,  
index()를 이용하여 해당 수의 인덱스를 찾는다.  

## 코드

```
n_list = [ int(input()) for _ in range(9) ]

print( max( n_list ) )
print( n_list.index( max( n_list ) ) + 1 )
```
