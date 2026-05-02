import time

a = 1664525      
c = 1013904223   
m = 2**32        

seed = int(time.time())

def next_random():                   
    global seed
    seed = (a * seed + c) % m     
    return seed                     

def random_in_range(min_val=1, max_val=67):
    rand_num = next_random()        
    return min_val + (rand_num % (max_val - min_val + 1))

def generate(count=1, min_val=1, max_val=67):
    results = []
    for _ in range(count):
        results.append(random_in_range(min_val, max_val))
    return results

def init_rng(new_seed):
    global seed
    seed = new_seed