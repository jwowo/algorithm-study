import sys

k = int(sys.stdin.readline().strip())
money = []

for _ in range(k):
    call = int(sys.stdin.readline().strip())
    if call == 0:
        money.pop()
    else: 
        money.append(call)

sum = 0
for i in money:
    sum += i

print(sum)