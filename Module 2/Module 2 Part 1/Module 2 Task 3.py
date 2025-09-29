a = int(input("Введите число (Метры): "))
operation = input("Перевод в (Мили / Дюймы / Ярды): ")
if operation == "Мили".lower():
    print(a * 0.000621371)
elif operation == "Дюймы".lower():
    print(a * 39.370066559999998)
elif operation == "Ярды".lower():
    print(a * 1.0936129599999999673)
else:
    print("Ошибка")