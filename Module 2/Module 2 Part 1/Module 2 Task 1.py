a = int(input("Число 1: "))
b = int(input("Число 2: "))
c = int(input("Число 3: "))
operation = input("Выберите операцию ( * / + ): ")
if operation == "*":
    print(a * b * c)
elif operation == "+":
    print(a + b + c)
else:
    print("Ошибка")
