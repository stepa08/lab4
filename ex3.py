age = int(input("Введите возраст: "))

if age < 0:
    print("Некорректный возраст")
elif age <= 12:
    print("Вы ребенок")
elif age <= 17:
    print("Вы подросток")
elif age <= 64:
    print("Вы взрослый")
else: 
    print("Вы пожилой")