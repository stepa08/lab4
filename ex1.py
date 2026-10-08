# Вводим новое число
print("Введите число:")
number = int(input())

# Определяем условия четности числа
if number % 2 == 0:
    print(f"Число {number} - четное")
else:
    print(f"Число {number} - нечетное")