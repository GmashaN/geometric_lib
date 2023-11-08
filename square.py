
def area(a):
    '''
        Возвращает площадь квадрата, рассчитанную по формуле S = a².
        a - длина стороны квадрата

        Параметры:
            a (int, float): число

        Возвращаемое значение:
            a_squared (int, float): квадрат числа a

        Пример вызова:
            input >> area(2)
            output >> 4
    '''
    if (type(a) not in [int, float]):
        return TypeError
    if (a < 0):
        return Exception

    return a * a


def perimeter(a):
    '''
        Возвращает периметр квадрата, рассчитанную по формуле P = 4a.
        a - длина стороны квадрата

        Параметры:
            a (int, float): число

        Возвращаемое значение:
            sum_quadrupled_a (int, float): учетверенное число a

        Пример вызова:
            input >> area(2)
            output >> 8
    '''
    if (type(a) not in [int, float]):
        return TypeError
    if (a < 0):
        return Exception

    return 4 * a
