"""Игра угадай число"""
# импорт библиотеки
import numpy as np 

number = np.random.randint(1, 101) # загадываем число с помощью функции random из библиотеки NumPy

count = 0 # устанавливаем количество попыток угадывания

# пишем цикл, позволяющий вводить и угадывать числа
while True:
    count += 1
    predict_number = int(input("Угадай число от 1 до 100"))
    
    # проверка соответствия числа, введенным пользователем, с загаданным
    if predict_number > number:
        print("Число должно быть меньше")
    elif predict_number < number:
        print("Число должно быть больше")
    else:
        print(f"Вы угадали число! Это число = {number}, за {count} попыток")
        break