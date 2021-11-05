n = int(input())

for i in range(n):
    scores = list(map(int, input().split()))

    avg_score = sum(scores[1:]) / scores[0]
    count = 0

    for score in scores[1:]:
        if score > avg_score:
            count += 1

    avg_rate = (count / scores[0]) * 100

    print(f'{avg_rate:.3f}%')

"""
n = int(input())

for i in range(n):
    student_list = list(map(int, input().split()))

    student_count = student_list[0]
    score_list = student_list[1:]

    avg_score = sum(score_list) / student_count

    lt_avg_count = 0

    for score in score_list:
        if score > avg_score:
            lt_avg_count += 1

    print('{:.3f}%'.format( round( ( lt_avg_count / student_count ) * 100 , 3)))
"""
