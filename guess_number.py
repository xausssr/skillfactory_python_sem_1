"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

from typing import Callable, Tuple

import numpy as np


def random_predict(number:int=np.random.randint(1, 101)) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. По умолчанию рандомно загадывается компьютером в диапазоне 1-100.

    Returns:
        int: Число попыток 
    """

    count = 0
    lst_num = list(range(1, 101))

    while True:
        count += 1
        predict_number = lst_num[len(lst_num) // 2]
        half = len(lst_num) // 2
        if number == predict_number:
            return count # выход из цикла, если угадали
        elif predict_number > number:
            lst_num = lst_num[:half]
        else:
            lst_num = lst_num[half:]


def evaluate_predict(predictor: Callable[[int], int], rounds:int=1000) -> Tuple[float, float]:
    """Производит оценку эффективности функции-угадывателя

    Args:
        predictor (Callable[[int], int]): функция угадывания
        rounds (int, optional): Количество раундов (итераций) оценки эффективности. Defaults to 1000.

    Returns:
        Typle[float, float]: кортеж с матожиданием и дисперсией числа попыток по всем раундам (итерациям).
    """

    results = np.zeros((rounds,)) # массив для сохранения результатов
    inputs_values = np.random.randint(1, 101, size=(rounds))
    for idx in range(rounds):
        results[idx] = predictor(inputs_values[idx])

    return (results.mean(), results.std())

print(f"Один запуск {random_predict()} попыток на угадывание.")
mean_attempts, std_attempts = evaluate_predict(random_predict)
print(f"Среднее число попыток: {mean_attempts:.1f}±{std_attempts:.2f}")
