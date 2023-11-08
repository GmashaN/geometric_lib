def area(a, h):
    '''
        Возвращает площадь треугольника, рассчитанную по формуле S = ah.
        a - длина стороны треугольника, к которой проведена высота
        h - длина высоты треугольника

        Параметры:
            a (int, float): первое число
            h (int, float): второе число

        Возвращаемое значение:
            multiplication_a_h_half (int, float): полупроизведение числел a и h

        Пример вызова:
            input >> area(3, 8)
            output >> 12
    '''
    if (type(a) not in [int, float] or type(h) not in [int, float]):
        return TypeError
    if (a < 0 or h < 0):
        return Exception

    return a * h / 2


def perimeter(a, b, c):
    '''
        Возвращает периметр треугольника, рассчитанную по формуле P = a + b + c.
        a - длина первой стороны треугольника
        b - длина второй стороны треугольника
        c - длина третьей стороны треугольника

        Параметры:
            a (int, float): первое число
            b (int, float): второе число
            c (int, float): третье число

        Возвращаемое значение:
            sum_a_b_c (int, float): сумма чисел a, b и c

        Пример вызова:
            input >> perimeter(3, 4, 5)
            output >> 12
    '''
    if (type(a) not in [int, float] or type(b) not in [int, float] or type(c) not in [int, float]):
        return TypeError
    if (a < 0 or b < 0 or c < 0):
        return Exception

    return a + b + c
