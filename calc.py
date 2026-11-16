def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    if b == 0:
        return None
    return a / b
while True:
    print("Выберите операцию:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Выход")

    choice = input("Введите номер операции (1/2/3/4/5): ")
    if choice == '5':
        print("Выход из программы.")
        break
    elif choice in ("1", "2", "3", "4"):
        num1 = float(input("Первое число: "))
        num2 = float(input("Второе число: "))
        if choice == "1":
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == "2":
            print(f"{num1} - {num2} = {sub(num1, num2)}")
        elif choice == "3":
            print(f"{num1} * {num2} = {mul(num1, num2)}")
        elif choice == "4":
            result = div(num1, num2)
            if result is None:
                print("Ошибка: Деление на ноль!")
            else:
                print(f"{num1} / {num2} = {result}")
    else:
        print("Неверный ввод. Пожалуйста, выберите правильную операцию.")


    