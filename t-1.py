import random

n = random.randint(2,5)
string = []
print(f"Введите {n} слов\а", sep='/n')

for i in range(n):
    string.append(input())

print(*string)
