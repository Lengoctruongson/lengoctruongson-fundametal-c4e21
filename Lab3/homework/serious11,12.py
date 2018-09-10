def is_inside(a, b):
    for i, item in enumerate(a):
        if item < 0:
            a[i] = -item
    for j, item1 in enumerate(b):
        if item1 < 0:
            b[j] = -item1
    if b[0] <= a[0] <= b[0] + b[2] and b[1] <= a[1] <= b[1] + b[3]:
        print('True')
    else:
        print('False')

is_inside([100, 120], [140, 60, 100, 200])
is_inside([200, 120], [140, 60, 100, 200])