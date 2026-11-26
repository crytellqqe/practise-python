import sys

print("Привет, давай сыграем в игру! Я тебе буду давать задачки, а ты должен посчитать ответ и написать его мне.")
print("Первый пример: x + 100 = 200")

# Первый пример
correct_1 = 100
attempt_1 = input("Какое число должно быть вместо x? ")

att = 0
while att < 3:
    try:
        attempt_1 = int(attempt_1)
        if attempt_1 == correct_1:
            print("")
            print("Правильно, идем дальше.")
            break
        else:
            print("")
            print("Неправильный ответ, попробуй еще раз.")
            attempt_1 = input()
            att += 1
    except ValueError:
        print("")
        print("Ты некорректно написал ответ.")
        attempt_1 = input()
if attempt_1 != correct_1:
    print("")
    print("У тебя не получилось, попробуй заново.")
    sys.exit()

# Второй пример
print("Второй пример: x * 5 = 125")

correct_2 = 25
attempt_2 = input("Какое число должно быть вместо x? ")

att = 0
while att < 3:
    try:
        attempt_2 = int(attempt_2)
        if attempt_2 == correct_2:
            print("")
            print("Правильно, идем дальше.")
            break
        else:
            print("")
            print("Неправильный ответ, попробуй еще раз.")
            attempt_2 = input()
            att += 1
    except ValueError:
        print("")
        print("Ты некорректно написал ответ.")
        attempt_2 = input()
if attempt_2 != correct_2:
    print("")
    print("У тебя не получилось, попробуй заново.")
    sys.exit()