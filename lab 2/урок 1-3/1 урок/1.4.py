import numpy as np
import matplotlib.pyplot as plt

x = np.linspace (0, 10, 50)
y1 = x

y2 = [i**2 for i in x]
plt.title('Линейная зависимость y = x')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.plot(x, y1, x, y2)
plt.show()