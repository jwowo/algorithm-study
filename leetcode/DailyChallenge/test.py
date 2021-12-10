a = 10
b = 5
b += 5

print(f'variable a address: {id(a)}')
print(f'variable b address:'{id(b)}')

if a is b:
    print('yes')
else:
    print('no')