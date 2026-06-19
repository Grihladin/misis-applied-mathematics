import numpy as np
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

# ARIMA модель и временной ряд data случайно сгенерированный 
np.random.seed(0)
data = pd.Series(np.random.randn(1000), index=pd.date_range('2022-01-01', periods=1000))
model = ARIMA(data, order=(1, 1, 1))  # Где p, d, q - параметры модели

# Подгонка ARIMA модели
result = model.fit()

# Получение предсказанных значений
predicted_values = result.predict()

# Фактические значения временного ряда
actual_values = data  # data - мой временной ряд

# Определение функции правдоподобия (NLL)
def negative_log_likelihood(y_true, y_pred):
    sigma = np.std(y_true - y_pred)  # Оценка стандартного отклонения ошибок
    log_likelihood = -0.5 * np.log(2 * np.pi * sigma**2) - 0.5 * ((y_true - y_pred) / sigma)**2
    return -log_likelihood.mean()

# Рассчитываем функцию правдоподобия для ARIMA модели
nll = negative_log_likelihood(actual_values, predicted_values)

print(f"Функция правдоподобия (NLL) для ARIMA: {nll}")