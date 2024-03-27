import random
def do_task1():
    lst = [3, 6, 9, 0, 2]
    number = int(input("Введите любое число: "))
    if number in lst:
        print(f'Исходный список: {lst} \nПоздравляю, Вы угадали число: {number}')
    else:
        print('Нет такого числа!')

def do_task2():
    lst_of_num = [4, 6, 3, 5, 5, 21, 6]
    same_numbers = []
    for i in lst_of_num:
        if lst_of_num.count(i) > 1 and i not in same_numbers:
            same_numbers.append(i)

    if len(same_numbers) > 0:
        print("Загаданный список:", *lst_of_num)
        print("Повторяющиеся элементы списка:", *same_numbers)
    else:
        print("В списке", lst_of_num, "нет повторяющихся элементов")

def do_task3():
    week = ("понедельник", 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье')
    number_of_days = int(input('Сколько выходных на неделе Вы хотите? '))
    weekends = week[(len(week)-number_of_days):]
    workdays = week[:(len(week)-number_of_days)]
    print("Ваши выходные дни:", *weekends)
    print("Ваши рабочие дни:", *workdays)

def do_task4():
    students1 = ["Полонская","Чиркунова",'Шутко','Крылов','Грабенко','Байрит','Васильева','Степненко','Черных']
    students2 = ['Горбачева','Игнатенко','Каширина','Жигалов','Удовкин','Пичуева','Агеечкина','Коченков','Рыков','Розина','Тимофеевна']

    team = tuple(random.sample(students1, 6) + random.sample(students2, 6))

    print("Группа МД-17: ", *students1)
    print("Группа МД-15: ", *students2)
    print("Спортивная команда: ", *team)
    print()

    print("Длина полученнного списка:", len(team))
    print()

    team_list = list(team)
    team_list.sort()
    team = tuple(team_list)
    print("Отсортированный кортеж:", *team)
    print()

    kol = 0
    for i in team:
        if "Иванов" in team:
            kol +=1
    print('Фамилия "Иванов" в списке встречается', kol, "раз")


