import numpy as np
import matplotlib.pyplot as plt

# Рандомно генерирую x and y
np.random.seed(0) 
x = np.random.rand(15) * 100  # 15 случайных чисел от 0 до 100
y = np.random.rand(15) * 100  

# Вычисление лог-приростов
log_returns_x = np.log(x) - np.log(np.roll(x, 1))
log_returns_y = np.log(y) - np.log(np.roll(y, 1))

# Рисую двумерную плоскость
plt.scatter(log_returns_x[1:], log_returns_y[1:], color='blue')
plt.title('Лог-приросты для двух показателей')
plt.xlabel('Лог-прирост x')
plt.ylabel('Лог-прирост y')
plt.grid(True)
plt.show()