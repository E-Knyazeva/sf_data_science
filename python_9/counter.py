from collections import Counter #импорт объекта Counter  из модуля Collection
c = Counter() # создание пустого объекта counter
c['red'] += 1
print(c)


cars = ['red', 'blue', 'black', 'black', 'black', 'red', 'white']
v = Counter()
for car in cars: # цикл для подсчета цветов проехавших машин
    v[car] += 1
print(v)

x = Counter(cars) # подсчет цветов проехавших машин
print(x)

print(v['black']) # подсчет конкретного цвета проехавших машин (3)
print(v['yellow']) # подсчет конкретного цвета проехавших машин (0)
print(sum(v.values())) # подсчет суммы всех значений
print(v.values()) # подсчет числа раз, когда встретился ключ


cars_moscow = ['black', 'black', 'white', 'black', 'black', 'white', 'yellow', 'yellow', 'yellow']
cars_spb = ['red', 'black', 'black', 'white', 'white', 'yellow', 'yellow', 'red', 'white']
counter_moscow = Counter(cars_moscow) # счетчики для списков
counter_spb = Counter(cars_spb)
print(counter_moscow) # исходный счетчик 
print(counter_spb)
print(counter_moscow + counter_spb) # сколько машин разных цветов встретилось в двух городах, можно сложить два исходных счётчика

counter_moscow.subtract(counter_spb) # разницу между объектами Counter, необходимо воспользоваться функцией subtract, которая меняет тот объект, к которому применяется.
print(counter_moscow)

counter_moscow = Counter(cars_moscow) # Пересоздаём счётчики, потому что объект counter_moscow поменял свои значения после функции subtract.
counter_spb = Counter(cars_spb)
print(counter_moscow - counter_spb) #вычитание

print(*counter_moscow.elements()) # список всех элементов, которые содержатся в Counter
print(list(counter_moscow)) # список уникальных элементов
print(dict(counter_moscow)) #превратить Counter в обычный словарь
print(counter_moscow.most_common()) # получить список из кортежей элемента в порядке убывания их встречаемости
print(counter_moscow.most_common(2)) # передать значение, которое задаёт желаемое число первых наиболее частых элементов, например, 2

counter_moscow.clear() # полностью обнулить счетчик
print(counter_moscow)
