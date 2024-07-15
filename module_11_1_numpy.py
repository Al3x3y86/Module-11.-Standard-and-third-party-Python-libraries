import numpy as np

# Библиотека numpy предоставляет широкие возможности для работы с многомерными массивами,
# выполнения математических операций, линейной алгебры, статистики и др.


# Создание массива чисел
array = np.array([1, 2, 3, 4, 5])

# Вывод созданного массива
print("Исходный массив чисел:")
print(array)

# Выполнение математических операций
# 1. Сумма всех элементов массива
sum_result = np.sum(array)

# 2. Умножение всех элементов на число
multiply_result = array * 2

# 3. Возведение всех элементов в квадрат
squared_result = np.square(array)

# Вывод результатов в консоль
print("Сумма всех элементов массива:", sum_result)
print("Умножение всех элементов на 2:", multiply_result)
print("Возведение всех элементов в квадрат:")
print(squared_result)
