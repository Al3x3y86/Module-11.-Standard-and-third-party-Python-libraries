import matplotlib.pyplot as plt

# Matplotlib позволяет создавать разнообразные графики, включая линейные, столбчатые диаграммы,
# круговые диаграммы и другие. Библиотека обладает широкими функциональными возможностями для настройки
# внешнего вида графиков, добавления меток, легенд и т.д.


# 1. Создание простого графика линии
plt.figure(figsize=(8, 6))
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
plt.plot(x, y, marker='o', color='b', linestyle='--')
plt.title('График линии')
plt.xlabel('X ось')
plt.ylabel('Y ось')
plt.grid(True)
plt.show()

# 2. Создание столбчатой диаграммы
plt.figure(figsize=(8, 6))
languages = ['Python', 'Java', 'C++', 'JavaScript', 'PHP']
popularity = [70, 60, 50, 80, 40]
plt.bar(languages, popularity, color='skyblue')
plt.title('Популярность языков программирования')
plt.xlabel('Язык программирования')
plt.ylabel('Популярность (%)')
plt.xticks(rotation=45)
plt.show()

# 3. Создание круговой диаграммы
plt.figure(figsize=(8, 6))
sizes = [25, 30, 20, 25]
labels = ['A', 'B', 'C', 'D']
explode = (0.1, 0, 0, 0)
plt.pie(sizes, labels=labels, explode=explode, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Распределение данных')
plt.show()
