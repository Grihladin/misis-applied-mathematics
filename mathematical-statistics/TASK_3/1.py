import numpy as np
from scipy import stats

# Параметры нормального распределения
mean1, std_dev1 = 0, 1  # первый компонент смеси, mean - сренее значение компонента
mean2, std_dev2 = 3, 2  # второй компонент смеси, std_dev - станарнтные отклонения

# Генерация выборки из смеси двух нормальных распределений
np.random.seed(0)  # Для воспроизводимости результатов
samples1 = np.random.normal(mean1, std_dev1, 1000)
samples2 = np.random.normal(mean2, std_dev2, 1000)
mixture_samples = np.concatenate([samples1, samples2])

# Проверка нормальности каждой компоненты смеси
normality_test_result1 = stats.shapiro(samples1)
normality_test_result2 = stats.shapiro(samples2)

print(f"Тест Шапиро-Уилка для компоненты 1: p-value = {normality_test_result1[1]}")
print(f"Тест Шапиро-Уилка для компоненты 2: p-value = {normality_test_result2[1]}")

# Проверка нормальности смеси
normality_test_result_mixture = stats.shapiro(mixture_samples)
print(f"Тест Шапиро-Уилка для смеси: p-value = {normality_test_result_mixture[1]}")