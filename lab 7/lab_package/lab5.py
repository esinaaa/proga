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


def collect_results(func):
    def wrapper():
        n = int(input("Сколько раз запустить? "))
        results = []
        for i in range(n):
            x = float(input(f"Введите число {i+1}: "))
            results.append(func(x))
        return results
    return wrapper