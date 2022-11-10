number = float(input("Введите число:\n"))

print("1) {0:.2f}".format(number))  # Округляем до сотых
print(f"2) {round(number)}")    # Округляем до целых
print("3) {0:=011}".format(number))     # Дополняем число нулями до 11 знаков
