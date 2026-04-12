import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib.ticker import AutoMinorLocator

def f(x):
    if 0 <= x <= 1:
        return np.cos(x + x**3)
    elif 1 < x <= 2:
        return np.e**(-x**2) - x**2 + 2*x
    else:
        return np.nan 

# Векторизуем для работы с массивами
f_vec = np.vectorize(f)

def df(x):
    return np.e**(-x**2) * -2*x - 2*x + 2  

x0 = 1.75
y0 = f(x0)
k = df(x0)

def tangent(x):
    return k * (x - x0) + y0

x_1 = np.linspace(0, 1, 200)
x_2 = np.linspace(1.00001, 2, 200)
x_k = np.linspace(1.00001, 2, 200)

y_1 = f_vec(x_1)
y_2 = f_vec(x_2)
y_k = tangent(x_k)

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x_1, y_1, '-b', linewidth=2, label='f(x) = cos(x + x^3)')
ax.plot(x_2, y_2, '-g', linewidth=2, label='e^(-x^2) - x^2 + 2x')
ax.plot(x_k, y_k, '--r', linewidth=2, label='касательная')

ax.scatter(x0, y0, color='red', zorder=5, s=80, label='Точка касания')

ax.annotate(f'Точка касания\nx₀ = {x0}\ny₀ = {y0:.3f}',
            xy=(x0, y0),
            xytext=(x0 + 0.2, y0 + 0.2),
            arrowprops=dict(arrowstyle='->', color='red'),
            fontsize=10,
            bbox=dict(boxstyle='square,pad=0.3', facecolor='yellow', alpha=0.3)
            )

ax.set_title('График функции и касательная к ней', fontsize=15)  

ax.set_xlabel('x', fontsize=15)   
ax.set_ylabel('y', fontsize=15)   

ax.legend()

ax.grid(which='major', linewidth=1.0)
ax.grid(which='minor', linestyle='--', linewidth=0.5, color='gray')
ax.xaxis.set_minor_locator(AutoMinorLocator())
ax.yaxis.set_minor_locator(AutoMinorLocator())

plt.tight_layout()
plt.show()