# Вводим новое число
print("Введите число:")
number = int(input())

# Определяем условия четности числа
if number % 2 == 0:
    answer1 = f"Число {number} - четное"
else:
    answer1 = f"Число {number} - нечетное"


# Дополнительное задание

# Делимость числа на 3
if number % 3 == 0:
    answer2 = "делится на 3"
else:
    answer2 = "не делится на 3"

# Положительность/ отрицательность/ равность нулю
if number > 0:
    answer3 = "положительное"
elif number < 0:
    answer3 = "орицательное"
else:
    answer3 = "равно нулю"

# Вывод ответа
print(f"{answer1}, {answer2}, {answer3}")
