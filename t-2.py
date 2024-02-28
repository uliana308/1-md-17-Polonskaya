string = []
word = ''
print('Введите любое слово или "stop", чтобы закончить программу', sep="/n")

while True:
    word = str(input())
    if word != "stop":
        string.append(word)
    else:
        break

print(*string)