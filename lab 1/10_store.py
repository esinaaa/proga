# Есть словарь кодов товаров
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
# или проще (/сложнее ?)
lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')

# Вывести стоимость каждого вида товара на складе:
# один раз распечать сколько всего столов и их общая стоимость,
# один раз распечать сколько всего стульев и их общая стоимость,
#   и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.
#;(
# TODO здесь ваш код

# ========== ЛАМПА ==========
code = goods['Лампа']
items = store[code]  # список партий

# Считаем общее количество и стоимость
total_quantity = items[0]['quantity']
total_cost = items[0]['quantity'] * items[0]['price']

print(f'Лампа - {total_quantity} шт, стоимость {total_cost} руб')

# ========== СТОЛ ==========
code = goods['Стол']
items = store[code]

total_quantity = items[0]['quantity'] + items[1]['quantity']
total_cost = items[0]['quantity'] * items[0]['price'] + items[1]['quantity'] * items[1]['price']

print(f'Стол - {total_quantity} шт, стоимость {total_cost} руб')

# ========== ДИВАН ==========
code = goods['Диван']
items = store[code]

total_quantity = items[0]['quantity'] + items[1]['quantity']
total_cost = items[0]['quantity'] * items[0]['price'] + items[1]['quantity'] * items[1]['price']

print(f'Диван - {total_quantity} шт, стоимость {total_cost} руб')

# ========== СТУЛ ==========
code = goods['Стул']
items = store[code]

total_quantity = items[0]['quantity'] + items[1]['quantity'] + items[2]['quantity']
total_cost = items[0]['quantity'] * items[0]['price'] + items[1]['quantity'] * items[1]['price'] + items[2]['quantity'] * items[2]['price']

print(f'Стул - {total_quantity} шт, стоимость {total_cost} руб')