import time

a = 1664525      
c = 1013904223   
m = 2**32        

seed = int(time.time())


def next_random():                   
    state = (a * seed + c) % m     
    return state                     

def random_in_range():
    rand_num = next_random()        
    result = (rand_num % 67) + 1
    return result

print("Генератор случайных чисел от 1 до 67")
print("Сгенерированное число:", random_in_range())