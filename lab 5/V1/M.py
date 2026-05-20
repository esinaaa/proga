def repeat_decorator(times=None):
    """
    Декоратор, который запускает функцию указанное число раз с указанными параметрами
    и возвращает последовательность результатов.
    
    Аргументы:
        times: количество запусков функции (по умолчанию None - 1 запуск)
    
    Поддерживает рекурсивные функции.
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
    """
    Фабрика калькуляторов. Создает функцию, которая выполняет арифметические операции
    с накоплением результата.
    
    Аргументы:
        operation: арифметическая операция ('+', '-', '*', '/')
        initial: начальное значение (по умолчанию 1)
    
    Возвращает:
        функцию, которая принимает число x и возвращает результат операции
    """
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


print("=== Тест 1: Многократный запуск обычной функции ===\n")

@repeat_decorator(5)
def greet(name):
    return f"Привет, {name}!"

result = greet("Анна")
print(f"Результаты: {result}")


print("\n=== Тест 2: Работа с калькулятором ===\n")

mult = make_calc('*')

@repeat_decorator(4)
def mult_with_repeat(x):
    return mult(x)

results = mult_with_repeat(2)
print(f"Результаты 4 запусков mult(2): {results}")


print("\n=== Тест 3: Рекурсивная функция ===\n")

@repeat_decorator(3)
def factorial(n):
    print(f"  внутри factorial({n})")
    if n <= 1:
        return 1
    return n * factorial(n - 1)

results = factorial(5)
print(f"\nРезультаты 3 запусков factorial(5): {results}")


print("\n=== Тест 4: Функция с разными параметрами ===\n")

@repeat_decorator(3)
def power(a, b):
    return a ** b

results = power(2, 3)
print(f"Результаты 3 запусков power(2, 3): {results}")


print("\n=== Тест 5: Без указания times ===\n")

@repeat_decorator()
def single_execution():
    return "Выполнено!"

result = single_execution()
print(f"Результат: {result}")


print("\n=== Тест 6: Проверка, что рекурсия не умножается ===\n")

@repeat_decorator(2)
def count_down(n):
    print(f"  count_down({n})")
    if n <= 0:
        return "Старт!"
    return count_down(n - 1)

results = count_down(3)
print(f"\nРезультаты 2 запусков: {results}")


print("\n=== Тест 7: Пример с калькулятором и разными операциями ===\n")

mult_calc = make_calc('*', initial=1)

@repeat_decorator(5)
def multiply(x):
    return mult_calc(x)

results = multiply(2)
print(f"Умножение на 2 (5 раз): {results}")

add_calc = make_calc('+', initial=0)

@repeat_decorator(3)
def addition(x):
    return add_calc(x)

results = addition(5)
print(f"Сложение 5 (3 раза): {results}")