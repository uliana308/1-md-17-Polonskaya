import random
#"Правильно!"
#"Ответ неверный"
#f"Игра окончена. Правильных ответов: {}"
popytka = 0
prav = 0

print("Добро пожаловать в игру 'Математика для детей'. Решите пример")

while popytka < 3:
    a = random.randint(0,10)
    b = random.randint(0, 10)
    print(f"{a} + {b} = ", end="")
    if a+b == int(input()):
        print("Правильно!")
        prav += 1
    else:
        print("Ответ неверный")
        popytka += 1
else:
    print(f"Игра окончена. Правильных ответов: {prav}")