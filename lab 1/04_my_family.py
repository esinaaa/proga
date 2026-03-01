# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ["Мама", "Папа", "Я"]

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# список списков приблизителного роста членов вашей семьи
my_family_height = [
    ["Мама", 164],
    ["Папа", 187],
    ["Я", 162]
]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
Post_papa = my_family_height[1][1]
print("Рост отца", Post_papa, "см")
# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
Post= my_family_height[0][1]+my_family_height[1][1]+my_family_height[2][1]
print("Рост семьи", Post, "см")