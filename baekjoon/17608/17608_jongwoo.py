import sys

n = int(sys.stdin.readline().strip())
stick = []

sum = 0
current_height = 0

for _ in range(n):
    stick.append(int(sys.stdin.readline().strip()))

while len(stick) > 0:
    # print(f'current stick : {stick}')
    out = stick.pop()
    # print(f'current out : ', out)
    
    if current_height < out:
        current_height = out
        sum += 1
    
print(sum)