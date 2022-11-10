from random import randint

# number1 = float(input("Введите первое число:\n"))  # Задание переменных в формате float
# number2 = float(input("Введите второе число:\n"))
# number3 = float(input("Введите третее число:\n"))

number1 = randint(0, 100)
number2 = randint(0, 100)
number3 = randint(0, 100)

average = (number1 + number2 + number3) / 3  # Формула среднего значения
print("Среднее значение: {0:.2f}".format(average))  # Вывод среднего значения с округлением до сотых
