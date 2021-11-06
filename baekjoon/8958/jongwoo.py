n = int(input())

for i in range(n):
    current_score = 1
    total_score = 0
    q = input()
    for i in q:
        if i == 'O':
            total_score += current_score
            current_score += 1
        else:
            current_score = 1
    print(total_score)
