import random
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KernelDensity


random.seed(0)
X = np.array([random.random() * 100 for i in range(15)]).reshape(-1, 1)

# Создание и обучение модели Kernel Density Estimation (KDE)
kde = KernelDensity(bandwidth=0.1, kernel='gaussian')  # Выбор ядра и ширины окна
kde.fit(X)

# Генерация точек для оценки плотности регрессора
X_plot = np.linspace(0, 1, 1000)[:, np.newaxis]  # Генерация точек для построения графика

# Рассчитываем плотность регрессора для этих точек
log_dens = kde.score_samples(X_plot)  # Логарифм плотности для каждой точки

# Построение графика непараметрической функции плотности регрессора
plt.fill(X_plot[:, 0], np.exp(log_dens), fc='#AAAAFF')  # Заполнение площади под кривой
plt.xlabel('X')
plt.ylabel('Плотность регрессора')
plt.title('Непараметрическая функция плотности регрессора')
plt.show()