def arithmetic(number_1, number_2, operation):
    if operation == "+":
        return number_1 + number_2
    elif operation == "-":
        return number_1 - number_2
    elif operation == "*":
        return number_1 * number_2
    elif operation == "/":
        return number_1 / number_2
    else:
        print("Неизвестная операция!")

number_1 = int(input("Введите первое число: "))

number_2 = int(input("Введите второе число: "))

operation = input("Введите операцию, которая будет произведена над числами (+, -, *, /): ")

print(arithmetic(number_1, number_2, operation))

