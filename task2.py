seat = int(input("Введите номер места "))
if seat < 37:
    if seat%2==0:
        print("Верхнее место в купе")
    else:
        print("Нижнее место в купе")
if seat >= 37:
    if seat % 2 == 0:
        print("Верхнее боковое место")
    else:
        print("Нижнее боковое место")