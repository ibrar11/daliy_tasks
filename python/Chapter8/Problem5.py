for x in range(3, 0 ,-1):
    for y in range(x, 0, -1):
        print('*', end='')
    for z in range(3 - x):
        print(' ', end='')
    print()