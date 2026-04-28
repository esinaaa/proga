def collect_results(func):
    def wrapper():
        n = int(input())
        results = []
        for i in range(n):
            result = func(int(input()))
            results.append(result)
        return results
    return wrapper


def make_calc(operation, initial=1):
    @collect_results
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
print(mult())
