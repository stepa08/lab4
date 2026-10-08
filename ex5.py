# Вводим 2 числа
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
# Выбираем операцию
operation = input("Введите операцию (+, -, *, /): ")

# Блок вывода значений
match operation:
    case "+":
        print(f"Результат: {a + b}")
    case "-":
        print(f"Результат: {a - b}")
    case "*":
        print(f"Результат: {a * b}")
    case "/":
        if b == 0:
            print("Ошибка: деление на ноль")
        else:
            print(f"Результат: {a / b}")
    case _:
        print("Неизвестная операция")
