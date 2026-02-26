# Словарь с координатами городов
cities = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Словарь для расстояний
distances = {}

# Список городов
names = list(cities.keys())

# Считаем расстояния между городами
for i in range(len(names)):
    for j in range(len(names)):
        if i != j:
            x1, y1 = cities[names[i]]
            x2, y2 = cities[names[j]]
            
            dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
            
            pair = f"{names[i]} - {names[j]}"
            distances[pair] = dist

# Выводим результат
print("Distances between towns:")
for pair, dist in distances.items():
    print(f"{pair}: {dist:.2f}")