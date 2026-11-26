inventory = ["Меч", "Зелье", "Щит", "Ключ"]
used_items = []

print("Инвентарь:")
for i, item in enumerate(inventory, start=1):
    print(f"{i}:", item)
print("")


inventory[1] = "Большое зелье"
print("Ты скрафтил Большое зелье!")

inventory.append("Факел")
print("Ты подобрал Факел!")

inventory.insert(1, "Карта")
print("Ты скрафтил Карта!")

used_items.append(inventory.pop(3))
print("Ты использовал Щит!")

inventory.pop()
print("Выкинут Ключ!")

print("")


if len(inventory) > 2:
    print("Инвентарь:")
    for i, item in enumerate(inventory, start=1):
        print(f"{i}:", item.upper())
    print("")

print("Использованы предметы:")
for i, item in enumerate(used_items, start=1):
        print(f"{i}:", item.upper())