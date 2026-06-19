import numpy as np
from scipy.stats import norm

# Параметры нормального распределения
mean1, std_dev1 = 0, 1  # первый компонент смеси, mean - сренее значение компонента
mean2, std_dev2 = 3, 2  # второй компонент смеси, std_dev - станарнтные отклонения

# Генерация выборки из смеси двух нормальных распределений
np.random.seed(0)
samples1 = np.random.normal(mean1, std_dev1, 1000)
samples2 = np.random.normal(mean2, std_dev2, 1000)

def likelihood_mixture(data, weights, means, std_devs):
    likelihood = 0
    num_components = len(weights)

    # Для каждой точки данных вычисляю сумму вероятностей из каждого компонента смеси
    for i in range(len(data)):
        prob = 0
        for j in range(num_components):
            prob += weights[j] * norm.pdf(data[i], means[j], std_devs[j])
        likelihood += np.log(prob)
    
    return likelihood

data = np.concatenate([samples1, samples2])  # смесь из предыдущего задания
weights = [0.5, 0.5]  # Веса компонента смеси
means = [0, 3]  # Средние значения компонента
std_devs = [1, 2]  # Стандартные отклонения компонента

# Вычисляем функцию правдоподобия для смеси
likelihood = likelihood_mixture(data, weights, means, std_devs)
print(f"Функция правдоподобия для смеси: {likelihood}")