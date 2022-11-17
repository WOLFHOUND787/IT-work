number = float(input("Введите число:\n"))
if (number % 3 == 0) and (number % 5 == 0):  # Если число делится на 3 и на 5
    print("Fizz Buzz")
elif number % 3 == 0:  # Если число делится на 3
    print("Fizz")
elif number % 5 == 0:  # Если число делится на 5
    print("Buzz")
else:  # Если не выполняются условия
    print(number)
