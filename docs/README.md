# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = ah

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c

## General description of solution
> Finding area or perimeter of geometric figure (circle, rectangle, square, triangle)

# Description of functions
## 1. Circle
 ### area
    Returns the area of the circle calculated by the formula S = πR².
    R - the radius of the circle

    Parameters:
        r (int, float): number

    Return value:
        multiplication_pi_r_r (int, float): product of the numbers π and R²

    Example of a function call:
        input >> area(1)
        output << 3.141592653589793
 ### perimeter
    Returns the perimeter of the circle calculated by the formula P = 2nR.
    R - the radius of the circle

    Parameters:
        r (int, float): number

    Return value:
        multiplication_pi_r_r_doubled (int, float): the doubled product of the numbers π and R

    Example of a function call:
        input >> perimeter(1)
        output << 6.283185307179586

## 2. Rectangle
 ### area
    Returns the area of the rectangle calculated by the formula S = ab.
    a - the length of the first line of the rectangle
    b - the length of the second line of the rectangle

    Parameters:
        a (int, float): first number
        b (int, float): second number

    Return value:
        multiplication_a_b (int, float): product of numbers a and b

    Example of a call:
        input >> area(2, 5)
        output >> 10
 ### perimeter
    Returns the perimeter of the rectangle calculated by the formula P = 2a + 2b.
    a - the length of the first line of the rectangle
    b - the length of the second line of the rectangle

    Parameters:
        a (int, float): first number
        b (int, float): second number

    Return value:
        sum_a_b_doubled (int, float): double the sum of the numbers a and b

    Example of a call:
         input >> perimeter(2, 5)
        output >> 14

## 3. Square
 ### area
    Returns the square area calculated by the formula S = a².
    a - the length of the side of the square

    Parameters:
        a (int, float): number

    Return value:
        a_squared (int, float): the square of the number a

    Example of a call:
        input >> area(2)
        output >> 4
 ### perimeter
    Returns the perimeter of the square calculated by the formula P = 4a.
    a - the length of the side of the square

    Parameters:
        a (int, float): number

    Return value:
        sum_quadrupled_a (int, float): quadruple a

    Example of a call:
        input >> area(2)
        output >> 8

## 4. Triangle
 ### area
    Returns the area of the triangle calculated by the formula S = ah.
    a - the length of the side of the triangle to which the height is drawn
    h - the length of the height of the triangle

    Parameters:
        a (int, float): first number
        h (int, float): second number

    Return value:
        multiplication_a_h_half (int, float): semi-reproduction of numbers a and h

    Example of a call:
        input >> area(3, 8)
        output >> 12
 ### perimeter
    Returns the perimeter of the triangle calculated by the formula P = a + b + c.
    a - the length of the first side of the triangle
    b - the length of the second side of the triangle
    c - the length of the third side of the triangle

    Parameters:
        a (int, float): first number
        b (int, float): second number
        c (int, float): third number

    Return value:
        sum_a_b_c (int, float): sum of numbers a, b and c

    Example of a call:
        input >> perimeter(3, 4, 5)
        output >> 12

## History of project
    commit 8c6b4ed3df4294e13a3b1cb90b5062f5d4e7bd6d (HEAD -> main, origin/main, origin/HEAD, new_feat_408440)
    Author: Maria Gerilovich <maria@3105.ru>
    Date:   Sun Sep 17 21:29:50 2023 +0300

        rectangle.py fixed, triangle.py added

    commit 50a0d73c6dde4cf24496dc821cc95010d59b6768
    Author: Maria Gerilovich <maria@3105.ru>
    Date:   Sun Sep 17 21:24:31 2023 +0300

        new file added: rectangle.py

    commit d078c8d9ee6155f3cb0e577d28d337b791de28e2
    Author: smartiqa <info@smartiqa.ru>
    Date:   Thu Mar 4 14:55:29 2021 +0300

        L-03: Docs added

    commit 8ba9aeb3cea847b63a91ac378a2a6db758682460
    Author: smartiqa <info@smartiqa.ru>
    Date:   Thu Mar 4 14:54:08 2021 +0300

