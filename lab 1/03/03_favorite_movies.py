# Есть строка с перечислением фильмов

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Запятая не должна выводиться.  Переопределять my_favorite_movies нельзя
# Использовать .split() или .find()или другие методы строки нельзя - пользуйтесь только срезами,
# как указано в задании!

# TODO здесь ваш код

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# первый фильм
print(my_favorite_movies[0:10])

# последний фильм
print(my_favorite_movies[42:])

# второй фильм
print(my_favorite_movies[12:25])

# второй с конца
print(my_favorite_movies[35:40])