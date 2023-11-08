import math


def area(r):
    '''
    Возвращает площадь окружности, рассчитанную по формуле S = πR².
        R - радиус окружности

        Параметры:
            r (int, float): число

        Возвращаемое значение:
            multiplication_pi_r_r (int, float): произведение чисел π и R²

        Пример вызова функции:
            input >> area(1)
            output << 3.141592653589793
    '''
    if (type(r) not in [int, float]):
        return TypeError
    if (r < 0):
        return Exception

    return math.pi * r * r


def perimeter(r):
    '''
        Возвращает периметр окружности, рассчитанную по формуле P = 2πR.
            R - радиус окружности

            Параметры:
                r (int, float): число

            Возвращаемое значение:
                multiplication_pi_r_r_doubled (int, float): удвоенное произведение чисел π и R

            Пример вызова функции:
                input >> perimeter(1)
                output << 6.283185307179586
        '''
    if (type(r) not in [int, float]):
        return TypeError
    if (r < 0):
        return Exception

    return 2 * math.pi * r
