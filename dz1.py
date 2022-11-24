def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Не является числом")
    return number


def checkNumber(num):
    if 6 <= num <= 7:
        print("Выходной")
    elif 0 < num < 6:
        print("Рабочий")
    else:
        print("число вне пределов 7 дней")


num = InputNumbers("Введите число: ")
checkNumber(num)