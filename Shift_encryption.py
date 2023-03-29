alpha = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
alphaUp = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
number = int(input("Введите число, на которое нужно сдвинуть текст: "))

summary = ""

def changeChar(char):
    if char in alpha:
        return alpha[(alpha.index(char) + number) % len(alpha)]
    elif char in alphaUp:
        return alphaUp[(alphaUp.index(char) + number) % len(alphaUp)]
    else:
        return char

with open("filename.txt", encoding="utf8") as myFile:
    for line in myFile:
        for char in line:
            summary += changeChar(char)

with open("output.txt", "w", encoding="utf8") as myFile:
    myFile.write(summary)
