# есть список животных в зоопарке

zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль
# TODO здесь ваш код

Zoo = zoo[0],"bear",zoo[1],zoo[2],zoo[3]
print(Zoo)

# добавьте птиц из списка birds в последние клетки зоопарка
b = ['rooster', 'ostrich', 'lark', ]
#  и выведите список на консоль
# TODO здесь ваш код

ZoO = Zoo[0],Zoo[1],Zoo[2],Zoo[3],Zoo[4],b[0],b[1],b[2]
print(ZoO)
# уберите слона
#  и выведите список на консоль
# TODO здесь ваш код
ZOO = Zoo[0],Zoo[1],Zoo[2],Zoo[4],b[0],b[1],b[2]
print(ZOO)
# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.
# TODO здесь ваш код
nomber= [
    ["lion", 1],
    ["bear", 2],
    ["kangaroo", 3],
    ["monkey", 4],
    ["rooster", 5],
    ["ostrich", 6],
    ["lark", 7]
]
print("Лев сидит в", nomber[0][1], "клетке")
print("Жаворонок сидит в", nomber[6][1], "клетке")