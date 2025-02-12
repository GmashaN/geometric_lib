def area(a, b):
    '''
        Возвращает площадь прямоугольника, рассчитанную по формуле S = ab.
        a - длина первой строны прямоугольника
        b - длина второй строны прямоугольника

        Параметры:
            a (int, float): первое число
            b (int, float): второе число

        Возвращаемое значение:
            multiplication_a_b (int, float): произведение чисел a и b

        Пример вызова:
            input >> area(2, 5)
            output >> 10
    '''

    if (type(a) not in [int, float] or type(b) not in [int, float]):
        return TypeError
    if (a < 0 or b < 0):
        return Exception

    return a * b

def perimeter(a, b):
    '''
        Возвращает периметр прямоугольника, рассчитанную по формуле P = 2a + 2b.
        a - длина первой строны прямоугольника
        b - длина второй строны прямоугольника

        Параметры:
            a (int, float): первое число
            b (int, float): второе число

        Возвращаемое значение:
            sum_a_b_doubled (int, float): удвоенная сумма чисел a и b

        Пример вызова:
            input >> perimeter(2, 5)
            output >> 14
    '''
    if (type(a) not in [int, float] or type(b) not in [int, float]):
        return TypeError
    if (a < 0 or b < 0):
        return Exception

    return 2 * (a + b) 
