n_list = [ int(input()) for _ in range(9) ]

print( max( n_list ) )
print( n_list.index( max( n_list ) ) + 1 )

"""
n_list = []

max = 0
index = 0

for i in range(9):
    n_list.append( int(input()) )
    if n_list[i] > max:
        max =n_list[i]
        index = i + 1

print(max)
print(index)
"""
