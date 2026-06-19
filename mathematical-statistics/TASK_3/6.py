import numpy as np
import matplotlib.pyplot as plt

# Параметры нормального распределения
mean1, std_dev1 = 0, 1  # первый компонент смеси, mean - сренее значение компонента
mean2, std_dev2 = 3, 2  # второй компонент смеси, std_dev - станарнтные отклонения

# Генерация выборки из смеси двух нормальных распределений
np.random.seed(0)
samples1 = np.random.normal(mean1, std_dev1, 1000)
samples2 = np.random.normal(mean2, std_dev2, 1000)


data = np.concatenate([samples1, samples2])

# Инициализация параметров
mu1, mu2 = 0, 3
sigma1, sigma2 = 1, 2
p = 0.5  # Вероятность выбора первой компоненты

# Функция для вычисления правдоподобия
def likelihood(data, mu1, mu2, sigma1, sigma2, p):
    component1 = p * (1 / (np.sqrt(2 * np.pi) * sigma1)) * np.exp(-0.5 * ((data - mu1) / sigma1) ** 2)
    component2 = (1 - p) * (1 / (np.sqrt(2 * np.pi) * sigma2)) * np.exp(-0.5 * ((data - mu2) / sigma2) ** 2)
    return component1 + component2

# Функция для алгоритма Метрополиса-Хастингса
def metropolis_hastings(data, iterations):
    samples = np.zeros((iterations, 5))  # Средние и стандартные отклонения для двух компонентов 
    acceptance_count = 0

    for i in range(1, iterations):
        # Генерация новых значений
        new_mu1, new_mu2, new_sigma1, new_sigma2, new_p = np.random.normal(samples[i-1], [0.1, 0.1, 0.1, 0.1, 0.1])
        
        # Вычисление нового правдоподобия
        new_likelihood = np.prod(likelihood(data, new_mu1, new_mu2, new_sigma1, new_sigma2, new_p))
        current_likelihood = np.prod(likelihood(data, samples[i-1, 0], samples[i-1, 1], samples[i-1, 2], samples[i-1, 3], samples[i-1, 4]))

        # Расчет отношения правдоподобия
        acceptance_ratio = new_likelihood / current_likelihood

        # Принятие или отклонение новых значений
        if np.random.rand() < acceptance_ratio:
            samples[i, :] = [new_mu1, new_mu2, new_sigma1, new_sigma2, new_p]
            acceptance_count += 1
        else:
            samples[i, :] = samples[i-1, :]

    acceptance_rate = acceptance_count / iterations
    print(f"Acceptance Rate: {acceptance_rate}")

    return samples

# Запуск алгоритма Метрополиса-Хастингса
iterations = 5000
samples = metropolis_hastings(data, iterations)

# Визуализация результатов
plt.figure(figsize=(12, 8))

plt.subplot(2, 3, 1)
plt.plot(samples[:, 0], label='mu1')
plt.legend()

plt.subplot(2, 3, 2)
plt.plot(samples[:, 1], label='mu2')
plt.legend()

plt.subplot(2, 3, 3)
plt.plot(samples[:, 2], label='sigma1')
plt.legend()

plt.subplot(2, 3, 4)
plt.plot(samples[:, 3], label='sigma2')
plt.legend()

plt.subplot(2, 3, 5)
plt.plot(samples[:, 4], label='p')
plt.legend()

plt.show()