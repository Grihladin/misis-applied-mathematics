import numpy as np
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

# ARIMA модель и временной ряд data случайно сгенерированный 
np.random.seed(0)
data = pd.Series(np.random.randn(1000), index=pd.date_range('2022-01-01', periods=1000))

# Разделение данных на обучающий и тестовый наборы (по 50%)
train_data = data[:500]
test_data = data[500:]

# Создание и обучение ARIMA модели на обучающем наборе данных
model = ARIMA(train_data, order=(1, 1, 1))  # Пример параметров: p=1, d=1, q=1
result = model.fit()

# Прогнозирование на тестовом наборе данных
predicted_values = result.predict(start=500, end=999)  # Прогноз для второй половины данных

# Оценка качества модели по критерию суммы квадратов отклонений
sq_error = np.sum((test_data.values - predicted_values)**2)
print("Сумма квадратов отклонений:", sq_error)