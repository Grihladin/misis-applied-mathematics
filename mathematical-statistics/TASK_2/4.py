import numpy as np
import random
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

# данные
random.seed(0)
X = np.array([random.random() * 100 for i in range(15)]).reshape(-1, 1)
y = np.array([random.random() * 100 for i in range(15)])

# Создание и обучение моделей
linear_regressor = LinearRegression()
linear_regressor.fit(X, y)

knn_regressor = KNeighborsRegressor(n_neighbors=3)  # Например, количество соседей = 3
knn_regressor.fit(X, y)

# Прогнозы для оценки качества моделей
y_pred_linear = linear_regressor.predict(X)
y_pred_knn = knn_regressor.predict(X)

# Рассчет среднеквадратичной ошибки для каждой модели
mse_linear = mean_squared_error(y, y_pred_linear)
mse_knn = mean_squared_error(y, y_pred_knn)

# Вывод результатов
print(f"Среднеквадратичная ошибка для линейной регрессии: {mse_linear}")
print(f"Среднеквадратичная ошибка для непараметрической регрессии (KNN): {mse_knn}")