import time

a = 1664525      
c = 1013904223   
m = 2**32        

seed = int(time.time())

def next_random():
    global seed
    seed = (a * seed + c) % m
    return seed

def random_in_range():
    rand_num = next_random()
    result = (rand_num % 67) + 1
    return result

print("Генератор случайных чисел от 1 до 67")

print("\n=== ЗАПУСК ТЕСТОВ ===\n")

def test_number_in_range():
    print("Тест 1: Число от 1 до 67...")
    for _ in range(50):
        num = random_in_range()
        assert 1 <= num <= 67, f"Ошибка: число {num} не в диапазоне"
    print("  OK")

def test_returns_int():
    print("Тест 2: Возвращает целое число...")
    num = random_in_range()
    assert type(num) == int, "Ошибка: вернуло не целое число"
    print("  OK")

def test_different_values():
    print("Тест 3: Генерирует разные числа...")
    results = []
    for _ in range(10):
        results.append(random_in_range())
    print(f"  Сгенерированные числа: {results}")
    assert len(set(results)) > 1, "Ошибка: все числа одинаковые"
    print("  OK")

def test_next_random_works():
    print("Тест 4: next_random работает...")
    num = next_random()
    assert type(num) == int, "Ошибка: next_random вернул не число"
    assert num >= 0, "Ошибка: число отрицательное"
    print("  OK")

if __name__ == "__main__":
    try:
        test_number_in_range()
        test_returns_int()
        test_different_values()
        test_next_random_works()
        print("\n=== ВСЕ ТЕСТЫ ПРОЙДЕНЫ! ===")
    except AssertionError as e:
        print(f"\nОшибка: {e}")