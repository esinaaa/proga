import pytest
from itertools import product

def test_code1():
    x = 4**2020 + 2**2017 - 15
    k = 0
    while x > 0:
        if x % 2 == 1:
            k += 1
        x = x // 2
    assert k == 2015

def test_code2():
    results = []
    for x in range(174457, 174506):
        a = []
        for d in range(2, x):
            if x % d == 0:
                a.append(d)
        if len(a) == 2:
            results.append((min(a), max(a)))
    assert len(results) == 8

def test_code3():
    cl = 'ТИМОФЕЙ'
    k = 0
    for code in product(cl, repeat=5):
        if code.count('Й') == 1:
            pos = code.index('Й')
            if (pos != 0 and pos != 4) and (code[pos - 1] != 'И' and code[pos + 1] != 'И'):
                k += 1
        if code.count('Й') == 0:
            k += 1
    assert k == 10476