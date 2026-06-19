import numpy as np
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

# ARIMA модель и временной ряд data случайно сгенерированный 
np.random.seed(0)
data = pd.Series(np.random.randn(1000), index=pd.date_range('2022-01-01', periods=1000))

# Создание и обучение ARIMA модели с statsmodels для получения начальных значений
model = ARIMA(data, order=(1, 1, 1))  # p=1, d=1, q=1
result = model.fit()

# Пример алгоритма Метрополиса-Хастингса для оценки коэффициентов ARIMA
current_params = result.params  # Начальные значения параметров
proposal_std = 0.1  # Стандартное отклонение для случайного блуждания

num_iterations = 10000  # Количество итераций алгоритма

accepted_params = []  # Хранение принятых параметров
for i in range(num_iterations):
    proposed_params = current_params + np.random.normal(0, proposal_std, len(current_params))
    
    # Оценка правдоподобия для старых и новых параметров
    old_likelihood = model.loglike(current_params)
    new_likelihood = model.loglike(proposed_params)
    
    # Вычисление отношения правдоподобия и вероятности перехода
    acceptance_ratio = np.exp(new_likelihood - old_likelihood)
    
    # Принятие или отвержение предложенных параметров в соответствии с правилами Метрополиса-Хастингса
    if acceptance_ratio > np.random.uniform(0, 1):
        current_params = proposed_params
        accepted_params.append(current_params)

# Оценка коэффициентов на основе принятых параметров
estimated_params = np.mean(accepted_params, axis=0)
print("Оценка коэффициентов ARIMA:", estimated_params)