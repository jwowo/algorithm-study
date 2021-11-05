문제 주소
=====================
<https://www.acmicpc.net/problem/1085>

문제 접근 방법
=====================
대각선의 경우 무조건 x축, y축 직선거리보다 거리가 멀기 때문에  
x축과 y축의 거리를 비교한다.  

x축의 경우  
	입력받은 x의 위치를 기준으로 0, w 와의 거리를 비교하여 작은 값을 찾아낸다.
y축의 경우도 
	동일하게 입력받은 y위치를 기준으로 0, h와의 거리를 비교하여 작은 값을 찾아낸다.

마지막으로 x축의 최단거리와 y축의 최단거리를 비교한다.

## 코드

```
x, y, w, h = map( int, input().split() )

if x < ( w -x ):
    x_min = x
else:
    x_min = w - x

if y < ( h - y ):
    y_min = y
else:
    y_min = h - y

if x_min < y_min:
    print(x_min)
else:
    print(y_min)
```
