def recursive(lst):
    if not lst:
        return 0
    
    stack = [lst] 
    k = 0           
    
    while stack:                     
        cur = stack.pop()       
        for i in cur:           
            k += 1                   
            if isinstance(i, list): 
                stack.append(i)   
    
    return k

print(recursive([]))                    # 0
print(recursive([1, 2, 3]))             # 3
print(recursive(["x", "y", ["z"]]))     # 4
print(recursive([1, 2, [3, 4, [5]]]))   # 7