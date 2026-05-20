def repeat_decorator(times=None):
    """
    Декоратор, который запускает функцию указанное число раз с указанными параметрами
    и возвращает последовательность результатов.
    """
    def decorator(func):
        in_recursion = False
        
        def wrapper(*args, **kwargs):
            nonlocal in_recursion
            
            if in_recursion:
                return func(*args, **kwargs)
            
            actual_times = times if times is not None else 1
            
            results = []
            for _ in range(actual_times):
                in_recursion = True
                result = func(*args, **kwargs)
                in_recursion = False
                results.append(result)
            
            return results
        
        return wrapper
    return decorator


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