def recursive(lst):
    if not lst:  
        return 0
    k = 0
    for i in lst:
        if isinstance(i, list):
           k += recursive(i) + 1
        else:
            k += 1
    return k
print(recursive([]))                    # 0
print(recursive([1, 2, 3]))             # 3
print(recursive(["x", "y", ["z"]]))     # 4
print(recursive([1, 2, [3, 4, [5]]]))   # 7