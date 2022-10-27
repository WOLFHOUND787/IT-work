# Hello, NAME SURNAME! You just delved into Python. Great start!
# В этой программе я пытался присвоить имя и фамилию одной переменной, но для проверки isalpha мешает пробел

while True:      # Цикл будет работать до тех пор, пока условие будет выдавать True
    first_name = input("Имя:\n")
    second_name = input("Фамилия:\n")
    if first_name.isalpha() and second_name.isalpha():      # isalpha выдаст значение True, если имя строковое
        print(f"Hello, {first_name} {second_name}! You just delved into Python. Great start!")
        break      # Остановка программы
    else:
        print("Пожалуйста, не используйте числа")
        break      # Остановка программы
