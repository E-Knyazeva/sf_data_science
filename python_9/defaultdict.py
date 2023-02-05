#список из кортежей с фамилиями студентов и их учебными группами
students = [('Ivanov',1),('Smirnov',4),('Petrov',3),('Kuznetsova',1),('Nikitina',2),('Markov',3),('Pavlov',2)]

# сохранить данные в словаре, в котором ключами будут номера групп, а элементами — списки студентов
groups1 = dict()
for student, group in students:
    if group not in groups1: # Проверяем, есть ли уже эта группа в словаре
        groups1[group] = list() # Если группы ещё нет в словаре, создаём для неё пустой список
    groups1[group].append(student)
print(groups1)




students = [('Ivanov',1),('Smirnov',4),('Petrov',3),('Kuznetsova',1),('Nikitina',2),('Markov',3),('Pavlov',2)]
from collections import defaultdict
groups = defaultdict(list)
for student, group in students:
    groups[group].append(student)
print(groups)
print(groups[4])



dict_object = dict() # словарь
defaultdict_object = defaultdict() # defaultdict 
print(type(dict_object)) # определение типа данных
print(type(defaultdict_object))
print(dict_object)
print(defaultdict_object)