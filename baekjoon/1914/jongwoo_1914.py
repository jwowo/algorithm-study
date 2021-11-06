n = int(input())

def recursion_count(x):
    if x == 1:
        return 1

    return ( 2 * recursion_count(x-1) ) + 1


def recursion_course(x, start, step, target):
    if x == 1:
        print(start, target)
        return 

    recursion_course(x-1, start, target, step)
    print(start, target)
    recursion_course(x-1, step, start, target)

    return

result = recursion_count(n)
print(result)

if n <= 20 :
    recursion_course(n, 1, 2, 3)
