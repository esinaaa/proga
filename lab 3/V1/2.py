x = 4**2020 + 2**2017 - 15 
k = 0 
while x > 0:
    if x%2==1:
        k+=1
    x = x//2
print(k) 