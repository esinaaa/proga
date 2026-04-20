def recursive(i):
    if i == 1:
        return 1
    if i == 2:
        return -1/8
    return ((i-1) * recursive(i-1)) / 3 + ((i-2) * recursive(i-2)) / 4
for i in range (1,8):
    print(recursive(i))