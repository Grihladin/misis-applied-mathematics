import numpy as np
import random
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

random.seed(0)
X = np.array([random.random() * 100 for i in range(15)]).reshape(-1, 1)
y = np.array([random.random() * 100 for i in range(15)])
# Создание модели для непараметрической регрессии (KNeighborsRegressor)
regressor = KNeighborsRegressor(n_neighbors=2)  # Выбор количества соседей

# Подгонка модели к данным
regressor.fit(X, y)

# Предсказание значений для построения регрессионной кривой
X_test = np.linspace(0, 1, 100).reshape(-1, 1)  # Новые данные для предсказания
y_pred = regressor.predict(X_test)

# Построение графика
plt.scatter(X, y, label='Наблюдаемые значения')
plt.plot(X_test, y_pred, color='red', label='Непараметрическая регрессия')
plt.legend()
plt.xlabel('X')
plt.ylabel('y')
plt.title('Непараметрическая регрессия на двумерной плоскости')
plt.show()

# Создание и обучение линейной
linear_regressor = LinearRegression()
linear_regressor.fit(X, y)

# Прогнозы для оценки качества моделей
y_pred_linear = linear_regressor.predict(X)
y_pred_knn = regressor.predict(X)

# Рассчет среднеквадратичной ошибки для каждой модели
mse_linear = mean_squared_error(y, y_pred_linear)
mse_knn = mean_squared_error(y, y_pred_knn)

# Вывод результатов
print(f"Среднеквадратичная ошибка для линейной регрессии: {mse_linear}")
print(f"Среднеквадратичная ошибка для непараметрической регрессии (KNN): {mse_knn}")