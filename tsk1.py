def tsk1():
    a = int(input("Введите любое число: "))
    if a % 7 == 0:
        print(f"Число {a} кратно 7")
    else:
        print(f"Число {a} не кратно 7")

def tsk2():
    try:
        a = int(input("Введите любое число: "))
        otvet = 200/a
        print(f'200 / {a} = {otvet}')
    except ValueError:
        print("Ошибка! ValueError!")
    except ZeroDivisionError:
        print("Ошибка! ZeroDivisionError!")

def tsk3():
    day, month, year = map(int, input("Введите день, месяц, год через точку: ").split("."))
    if day*month != year % 100:
        print("True") #return True
    else:
        print("False") #return False

def tsk4():
    num = str(input("Введите номер билета: "))
    if len(num) % 2 != 0 or int(num) <= 0:
        print("Ошибка!")
    else:
        half = len(num)//2
        num1 = list(map(int, num[:half]))
        num2 = list(map(int, num[half:]))
        if sum(num1) == sum(num2):
            print(f"Поздравляем! Билет №{num} счастливый!")
        else:
            print(f"К сожалению, билет №{num} несчастливый:(")