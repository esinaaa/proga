def iterative(n):
    if n == 1:
        return 1
    if n == 2:
        return -1/8
    
    x1 = 1      
    x2 = -1/8   
    
    for i in range(3, n + 1):
        x3 = ((i-1) * x2) / 3 + ((i-2) * x1) / 4
        x1, x2 = x2, x3   
    
    return x2
for i in range (1,8):
    print(iterative(i))