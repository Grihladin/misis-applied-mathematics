import numpy as np
from sklearn.mixture import GaussianMixture

# Параметры нормального распределения
mean1, std_dev1 = 0, 1  # первый компонент смеси, mean - сренее значение компонента
mean2, std_dev2 = 3, 2  # второй компонент смеси, std_dev - станарнтные отклонения

# Генерация выборки из смеси двух нормальных распределений
np.random.seed(0)  # Для воспроизводимости результатов
samples1 = np.random.normal(mean1, std_dev1, 1000)
samples2 = np.random.normal(mean2, std_dev2, 1000)

# Пример данных из предыдущего запроса
data = np.concatenate([samples1, samples2]).reshape(-1, 1)

# Применение EM-алгоритма для разделения смеси на две компоненты
gmm = GaussianMixture(n_components=2, random_state=0)
gmm.fit(data)

# Получение предсказаний (кластеров) для каждой точки данных
predicted_labels = gmm.predict(data)

# Вывод результатов
print("Параметры компонентов смеси:")
for i in range(2):
    print(f"Компонент {i+1}: Среднее = {gmm.means_[i][0]}, Стандартное отклонение = {np.sqrt(gmm.covariances_[i][0][0])}")

# Вывод кластеров
print("\n Предсказанные кластеры (0 и 1):")
print(predicted_labels)