def solution(numbers, target):
    answer = 0
    result = [0]
    
    for n in numbers:
        temp = []
        for r in result:
            temp.append(r + n)
            temp.append(r - n)
        result = temp;
        print(temp)
        

    answer = result.count(target)
    return answer