# ГЕНЕРАЦИЯ FLOAT

import numpy as np
print(np.random.rand()) #генерирует число с плавающей точкой между 0 (включительно) и 1 (не включительно)
print(np.random.rand()*100) # случайное число в диапазоне, например, от 0 до 100
print(np.random.rand(5)) # массив из пяти случайных чисел
print(np.random.rand(2, 3)) # Массив из двух случайных строк и трёх столбцов
np.random.rand(2,3,4,10,12,23) # шестимерный массив


shape = (3, 4)
print(np.random.rand(*shape)) # распаковка кортежа, с целью избежания ошибки

shape = (2,3)
print(np.random.sample(shape)) # функция, генерирующая массивы случайных чисел от 0 до 1, которая принимает в качестве аргумента именно кортеж без распаковки


print(np.random.uniform()) # Запуск без аргументов эквивалентен работе функций rand или sample
print(np.random.uniform(-30, 50)) # Задали границы диапазона от -30 до 50
print(np.random.uniform(0.5, 0.75, size=5)) # пять чисел в интервале от 0.5 до 0.75
print(np.random.uniform(-1000, 500, size=(2,3))) #  массив из двух строк и трёх столбцов из чисел в интервале от -1000 до 500

# ГЕНЕРАЦИЯ INT

print(np.random.randint(4,size=(2,3))) #таблицу 2x3 от 0 до 3 включительно
print(np.random.randint(6,12,size=(3,3)))


# ГЕНЕРАЦИЯ ВЫБОРОК

arr = np.arange(6)
print(arr)
print(np.random.shuffle(arr)) # Просто перемешать все числа в массиве
print(arr)

playlist = ['The Beatles', 'Pink Floyd', 'ACDC', 'Deep Purple']
shuffled = np.random.permutation(playlist) # получить новый перемешанный массив, а исходный оставить без изменений
print(shuffled)
print(playlist)

print(np.random.permutation(10)) # Перемешать набор чисел от 0 до n-1 

workers = ['Ivan', 'Nikita', 'Kate', 'John', 'Helen']
choice = np.random.choice(workers, size=2, replace=False)
print(choice)


# SEED ГЕНЕРАТОРА ПСЕВДОСЛУЧАЙНЫХ ЧИСЕЛ

print(np.random.seed(23))
print(np.random.randint(10, size=(3,4)))

np.random.seed(100)
print(np.random.randint(10, size=3))
print(np.random.randint(10, size=3))
print(np.random.randint(10, size=3))

