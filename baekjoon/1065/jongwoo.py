# 문제 접근 방법

# 천의 자리수 : 1000으로 나눈 목
# 백의 자리수 : ( 1000으로 나눈 나머지  ) / 100으로 나눈 몫
# 십의 자리수 : ( 100으로 나눈 나머지 ) / 10으로 나눈 몫
# 일의 자리수 : 10으로 나눈 나머지
# 몇자리 수 인지 어떻게 확인? 
# -> str로 받아서 len ( x ) 
# 10 보다 작으면 일의 자리수, 10보다 크고 100보다 작으면 백의 자리수, ... ( O )

nums = int(input())

count = 0

for n in range(1, nums + 1):

    thousand_idx = n // 1000
    hundred_idx = ( n % 1000 ) // 100
    ten_idx = ( n % 100 ) // 10
    one_idx = n % 10

    if n < 100:
        count += 1

    elif n < 1000:
        if one_idx - ten_idx == ten_idx - hundred_idx:
            count += 1

    else:
        if one_idx - ten_idx == ten_idx - hundred_idx and ten_idx - hundred_idx == hundred_idx - thousand_idx:
            count += 1

print(count)
