# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# создайте множество цветов, произрастающих в саду и на лугу
# garden_set =
# meadow_set =
# TODO здесь ваш код

# выведите на консоль все виды цветов
# TODO здесь ваш код

# выведите на консоль те, которые растут и там и там
# TODO здесь ваш код

# выведите на консоль те, которые растут в саду, но не растут на лугу
# TODO здесь ваш код

# выведите на консоль те, которые растут на лугу, но не растут в саду
# TODO здесь ваш код

garden_set = set(garden)
meadow_set = set(meadow)

all = garden_set | meadow_set  
print("Все виды цветов:", all)

both = garden_set & meadow_set 
print("Растут и в саду, и на лугу:", both)

only_garden = garden_set - meadow_set
print("Растут в саду, но не на лугу:", only_garden)

only_meadow = meadow_set - garden_set
print("Растут на лугу, но не в саду:", only_meadow)