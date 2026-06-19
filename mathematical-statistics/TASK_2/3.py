import numpy as np
import matplotlib.pyplot as plt

# Пример данных
X = np.linspace(0, 10, 100)
Y = np.sin(X) + np.random.normal(0, 0.1, 100)

# Точка, в которой будет оцениваться регрессия (исключена из оценки)
point = 5

# Определяем ширину окна по правилу Сильвермана
std_dev = np.std(Y)
bandwidth = 1.06 * std_dev * len(Y) ** (-1 / 5)

# Функция для вычисления весов с использованием ядра Гаусса
def gaussian_kernel(x, x_i, bandwidth):
    return np.exp(-((x - x_i) / bandwidth) ** 2 / 2) / (bandwidth * np.sqrt(2 * np.pi))

# Функция для оценки регрессии в точке point
def kernel_regression(x, X, Y, bandwidth):
    numerator, denominator = 0, 0
    for i in range(len(X)):
        weight = gaussian_kernel(x, X[i], bandwidth)
        numerator += weight * Y[i]
        denominator += weight
    return numerator / denominator

# Вычисляем регрессию в точке point
predicted_value = kernel_regression(point, X, Y, bandwidth)

# Строим график регрессии
plt.scatter(X, Y, label='Данные')
plt.scatter(point, predicted_value, color='red', label='Предсказание в точке')

# Вычисляем регрессионную кривую
Y_pred = [kernel_regression(x, X, Y, bandwidth) for x in X]
plt.plot(X, Y_pred, color='green', label='Регрессионная кривая')

plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.title('Непараметрическая регрессия с использованием ядерной оценки')
plt.show()
