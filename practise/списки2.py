pushups = [15, 20, 18, 25, 0]

dont_writing = pushups.pop(4)
pushups.insert(4, 30)

pushups.append(35)

print(f"Всего тренировок: {len(pushups)}")

print("План на следующую неделю:")
for i, item in enumerate(pushups, start=1):
    print(f"{i}:", item + 5)

print(f"Забыл записать в один из дней, и там было: {dont_writing}")