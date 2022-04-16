import sys

month, day = map(int, sys.stdin.readline().split())

# 1월 1일과 차이나는 일수 저장을 위한 변수
total_day = 0

# 31일인 달 리스트에 저장
day_31_list = [1, 3, 5, 7, 8, 10, 12]

# 요일 출력을 위한 dictionary
day_of_week = {0:'MON', 1:'TUE', 2:'WED', 3:'THU', 4:'FRI', 5:'SAT', 6:'SUN'}

for i in range(1, month):
    # print(f'{i}월 더 함')
    
    # 2 월
    if i == 2:
        total_day += 28

    # 1, 3, 5, 7, 8, 10, 12 월
    elif i in day_31_list:
        total_day += 31
    
    # 2, 4, 6, 9, 11 월
    else:
        total_day += 30

# 차이나는 일 수 만큼 더함
total_day += (day - 1)
total_day = total_day % 7

print(day_of_week[total_day])
