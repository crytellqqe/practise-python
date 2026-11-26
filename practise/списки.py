passengers = ["Анна", "Борис", "Виктор"]
print("В очереди на посадку стоят:")
for i in passengers:
    print(i)

print("")
passengers.append("Дмитрий")
print(f"Пришел {passengers[3]} и занял последнее место в очереди")
print("")

print(f"Елена купила вип билет и заняла место после {passengers[0]}")
passengers.insert(1, "Елена")
print("")

cancelled_passengers = []
cancelled_passengers.append(passengers.pop(3))
print(f"От полета отказался {cancelled_passengers[0]}")
print("")

print("В итоге полетели:")
for i in passengers:
    print(i)
print("")
print("Отказались от полета:")
for i in cancelled_passengers:
    print(i)