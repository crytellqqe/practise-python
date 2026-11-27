lap_times = [64.5, 59.2, 68.1, 61.0]

print("Твои результаты заездов:")
for i, time in enumerate(lap_times, start=1):
    print(f"{i} круг: ", time)
print("")

lap_times.append(58.7)
print(f"Ты проехал финальный круг за {lap_times[-1]} секунд")
print("")

print("Твои новые результаты заездов:")
for i, time in enumerate(lap_times, start=1):
    print(f"{i} круг: ", time)
print("")

erroneous_result = lap_times.pop(2)
print(f"Третий заезд оказался ошибочным. Удален результат: {erroneous_result}")
print("")

print(f"Лучший результат: {min(lap_times)}")
print(f"Худший результат: {max(lap_times)}")
print("")

lap_times.sort()
print("Итоговые результаты:")
print("")

print("Время за которое проехан каждый круг")
for top, time in enumerate(lap_times, start=1):
    print(f"{top} круг: {time}")
print("")

print(f"Засчитанные круги: {len(lap_times)}")