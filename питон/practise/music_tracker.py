# Переменные для треков
track_1 = 0
track_2 = 0
track_3 = 0
track_4 = 0
track_5 = 0

# Начальный текст
print("Привет! Это трекер прослушанных треков.")
print("Пока что работает только с пятью треками, потому что я не изучил списки")
print("Просто пиши в секундах длительность трека и я в конце выведу сколько треков ты прослушал, сколько всего они длились")
print("и сколько я пропустил")
print("Ах, да! Забыл! Пропущенными треками считаются треки меньше 30 секунд длительности.")
print("Так же, не вписывай 0! Если конечно не хочешь сразу вывести статистику не после 5 треков :)")

# Цикл для вписывания длительности треков и обрывания в случае вписывания 0 и меньше
while True:
    track_1 = int(input("Введи длительность трека в секундах: "))
    if track_1 <= 0:
        break
    track_2 = int(input("Введи длительность трека в секундах: "))
    if track_2 <= 0:
            break
    track_3 = int(input("Введи длительность трека в секундах: "))
    if track_3 <= 0:
            break
    track_4 = int(input("Введи длительность трека в секундах: "))
    if track_4 <= 0:
            break
    track_5 = int(input("Введи длительность трека в секундах: "))
    if track_5 <= 0:
            break
    break

# Переменные прослушанных треков и переменные скипнутых треков. Проверка на длительность треков.
listened = 0
skipped = 0

if track_1 <= 30 and track_1 > 0:
     skipped += 1
elif track_1 > 30:
     listened += 1

if track_2 <= 30 and track_2 > 0:
    skipped += 1
elif track_2 > 30:
    listened += 1

if track_3 <= 30 and track_3 > 0:
    skipped += 1
elif track_3 > 30:
    listened += 1

if track_4 <= 30 and track_4 > 0:
    skipped += 1
elif track_4 > 30:
    listened += 1

if track_5 <= 30 and track_5 > 0:
    skipped += 1
elif track_5 > 30:
    listened += 1

# Высчитывание времени прослушанных треков (строго больше 30 секнуд)
total = 0
if track_1 > 30:
   total += track_1
if track_2 > 30:
    total += track_2
if track_3 > 30:
    total += track_3
if track_4 > 30:
    total += track_4
if track_5 > 30:
    total += track_5

total_min = total // 60
total_sec = total % 60

# Статистика
print("***Статистика***")
print(f"Прослушано треков: {listened}")
print(f"Пропущено треков: {skipped}")
print(f"Всего времени прослушано (без пропущенных треков): {total_min} минут {total_sec} секунд")