import sys
from sys import stdin
INF = sys.maxsize

sys.setrecursionlimit(10**8)
# 다 풀고나서 주의사항 생각해보기
# 같은 여러점

def getDistance(a, b):
    return ((a[0] - b[0])**2) + ((a[1] - b[1])**2)
    

def divide_conquer(start, end):
    if end - start == 1:
        return getDistance(li[start],li[end])
        
    mid = (start + end)//2
    min_value = min(divide_conquer(start,mid), divide_conquer(mid, end))
    
    
    # 여기서 이제 min_value보다 작은 것들을 찾아야 한다.
    final = []
    for i in range(start, end+1):
        if (li[mid][0] - li[i][0])**2 <min_value:
            final.append(li[i])
            
    # y축 기준으로 sort
    final.sort(key=lambda x : x[1])
    len_ = len(final)
    
    for i in range(len_-1):
        for j in range(i+1, len_):
            yDistance = final[i][1] - final[j][1]
            
            if yDistance*yDistance <min_value:
                pointDistance = getDistance(final[i], final[j])
                min_value = min(min_value, pointDistance)
            else: # 이거 없으면 시간초과 메모리 초과 뜨는 듯
                break
                
                
    return min_value



# 실행 파트
n = int(input())
li = []
for _ in range(n):
    # a, b = map(int, stdin.readline().split())
    # li.append([a,b]) # 여기서 tuple보다 리스트가 빠르다.
    # 리스트에 append할 때 리스트 형식보다는 tuple이 훨씬 빠르다.
    # 리스트는 항상 여분의 메모리를 남겨두기 때문에 !
    
    li.append(tuple(map(int, stdin.readline().split())))
    
li.sort()


ans = divide_conquer(0, n-1)
print(ans)