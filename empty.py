from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления'
           ' квадратного корня из заданного числа')


def calculate_square_root(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number):
    """Проверяет введённое число и выводит результат."""
    if your_number <= 0:
        return 'Нельзя брать квадратный корень из числа <= 0'
    num = calculate_square_root(your_number)
    print(f'Мы вычислили квадратный корень из введённого вами числа. '
          f'Это будет: {num}')
    return 'Ошибка'


print(message)
calc(25.5)
