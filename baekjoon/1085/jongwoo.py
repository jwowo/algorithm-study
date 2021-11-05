x, y, w, h = map( int, input().split() )

if x < ( w -x ):
    x_min = x
else:
    x_min = w - x

if y < ( h - y ):
    y_min = y
else:
    y_min = h - y

if x_min < y_min:
    print(x_min)
else:
    print(y_min)

#if x < ( w / 2 ):
#    a = x
#else:
#    a = w - x

#if y < ( h / 2 ):
#    b = y
#else:
#    b = h - y

#if a < b:
#    print(a)
#else:
#    print(b)
