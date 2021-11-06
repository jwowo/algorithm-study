# 문제 접근 방법
# 1. 10,000 까지 에라테라토스: 배열 생성
# 2. 2부터 입력받은 테스트케이스 수 까지 에타토스테네스의 체 배열돈다.
# 2-1. x(해당 수)가 소수일때, t - x (테스트케이스 - 해당 수)도 소수인지 확인한다.
# 3. ( ? ) t의 골드바흐 파티션이 여러가지인 경우는 어떻게 해야할까? 
# 3-1. t / 2 부터 t까지 에타테라토스의 체 배열 확인하면 될 것 같음

n = int(input())

# 에라테라토스의 체 생성
eratos = [ True for _ in range(10001) ]

# 에라테라토스의 체 초기화
for i in range(2, 10001):
    if eratos[i] == False:
        continue
    for j in range(i+i, 10001, i):
        eratos[j] = False

for _ in range(n):
    # 테스트 케이스
    t = int(input())

    # t의 가능한 골드바흐 파티션이 여러 가지일 경우, 
    # 두 소수의 차이가가장 작은 것을 출력하기 위해 반으로 나눈다.
    start = t // 2

    for num1 in range(start, t):
        num2 = t - num1
        if eratos[num1] == True and eratos[num2] == True:
            print(num2, num1)
            break
