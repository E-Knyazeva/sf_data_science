"""Игра угадай число
Компьютер сам загадывает число и сам угадывает число
"""

import numpy as np

def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число
    
    Args:
        number (int, optional): Загаданное число . Defaults to 1.
    
    Returns:
        int: Число попыток
    """
    
    count = 0 #переменная счетчикаа
    max_number = 100 # максимально возможное загадываемое число
    min_number = 1 # минимально возможное загадываемое число
    predict_number = np.random.randint(min_number,101) # загаданное число
    
    while True:
        count += 1
        
        if number < predict_number:
            max_number = predict_number - 1
            predict_number = (max_number + min_number) // 2
        elif number > predict_number:
            min_number = predict_number + 1
            predict_number = (max_number + min_number) // 2
        else:
            #print(f"Алгоритм рассчитал число {number} за {count} попыток.")
            break # выход из цикла если угадали
    return count


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм
    
    Args:
        random_predict ([type]): функция угадывания
    Returns:
        int: среднее количество попыток
    """
    
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроиводимости
    random_array = np.random.randint(1,101,size=(1000)) # загадали список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score

if __name__ == "__main__":
    score_game(random_predict) # RUN
                
    
    