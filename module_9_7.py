def is_prime(func):
    """
    Декоратор, проверяющий, является ли результат функции простым числом.
    """
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)  # Вызываем исходную функцию и получаем результат
        if result <= 1:
            print("Составное")
        else:
            for i in range(2, int(result ** 0.5) + 1):
                if result % i == 0:
                    print("Составное")
                    break
            else:
                print("Простое")  # Простое число
        return result  # Возвращаем результат исходной функции
    return wrapper

@is_prime
def sum_three(a, b, c):
    """
    Функция, которая складывает три числа.
    """
    return a + b + c

# Демонстрация работы
result = sum_three(2, 3, 6)
print(result)