red = "красный"
blue = "синий"
yellow = "желтый"
purple = "фиолетовый"
green = "зеленый"
orange = "оранжевый"
a = str(input("Введите первый цвет "))
b = str(input("Введите второй цвет "))
if a != red and a != blue and a != yellow or b != red and b != blue and b != yellow:
    print("Error")
else:
    if a == red:
        if b == blue:
            print(purple)
        if b == yellow:
            print(orange)
    if a == blue:
        if b == yellow:
            print(green)
        if b == red:
            print(purple)
    if a == yellow:
        if b == red:
            print(orange)
        if b == blue:
            print(green)

