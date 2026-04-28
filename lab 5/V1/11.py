def make_calc(operation, initial=1):
    def calculator(x):
        nonlocal initial
        if operation == '+':
            initial = initial + x
        elif operation == '-':
            initial = initial - x
        elif operation == '*':
            initial = initial * x
        elif operation == '/':
            if x != 0:
                initial = initial / x
        return initial
    return calculator

mult = make_calc('*')
print(mult(5))   
print(mult(2))   

add = make_calc('+', initial=0)
print(add(10))   
print(add(5))    