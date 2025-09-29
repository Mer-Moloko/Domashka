a = int(input("Число 1: "))
b = int(input("Число 2: "))
c = int(input("Число 3: "))
operation = input("Выберите операцию (Min / Ave / Max): ")
numbers = [a, b, c]
if operation == "Min".lower():
    print(min(numbers))
elif operation == "Ave".lower():
    print((a+b+c)/3)
elif operation == "Max".lower():
    print(max(numbers))