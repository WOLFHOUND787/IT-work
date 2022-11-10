from random import randint

number1 = randint(0, 3)
number2 = randint(1, 3)  # Деление на 0

result = [number1 // number2, number1 % number2]
print(result)
