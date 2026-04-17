from itertools import product

def t():
    cl = 'ТИМОФЕЙ'
    k = 0

    for code in product(cl , repeat=5):
        if code.count('Й') == 1:
            pos = code.index('Й')
            if (pos != 0 and pos != 4) and (code[pos - 1] != 'И' and code[pos + 1] != 'И'):
                k += 1
        if code.count('Й') == 0:
            k += 1
    return k
print (t())


