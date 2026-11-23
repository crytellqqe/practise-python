import time
import keyboard
import os

# Переменная список для шаблонов, переменная с инедксом элемента списка, переменная отвечающая за текст, который будет печататься
texts = ["По умолчанию"]
x = 0
a = 0

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Меню
def menu():
    clear()

    print("***Autotyper by crytellqqe***")
    print("                  version: not released")
    print("")
    print(f"Выбранный шаблон: {texts[x]}")
    print("")
    print("Выбрать шаблон: F9")
    print("Вывести список шаблонов: F10")
    print("Добавить/удалить шаблон: CTRL + F10")
    print("")
    print("Печатать один раз: F7")
    print("Печатать без остановки по кругу: F8. Для остановки зажмите DEL до выключения")
    print("")
    print("ALT + DEL для завершения программы")

# Функция для выбора шаблона из списка
def text_w():
    clear()

    print(f"Выберите шаблон от {1} до {10}")

    global x

    x = int(input()) - 1

    print("") # Здесь позже сделать функцию для очистки консоли
    menu()

# Вывод шаблонов
def templates():
    for i, items in enumerate(texts, start=1):
        print(i, items)

def f10_templates():
    clear()
    templates()
    print("")
    print("Чтобы вернуться в меню, введите: меню")
    while True:
        back = input()
        if back == "меню":
            menu()
            break
        else:
            clear()
            templates()
            print("")
            print("Неверный ввод, попробуйте еще раз")
            print("Чтобы вернуться в меню, введите: меню")

# Функция для добавления и удаления шаблонов
def add_or_delete():
    clear()

    global a, texts
    
    print("Добавить, удалить или переместить шаблон? Добавить/Удалить/Переместить")
    choice = input().lower()

    while True:
        clear()

        if choice == "добавить":
            print("Введите ваш шаблон:")
            text = input()
            print("На какое место его поставить?")
            print("Ваши шаблоны:")
            print("")
            templates()
            print("")
            a = int(input()) - 1
            texts.insert(a, text)

            clear()
            
            print("Ваши шаблоны:")
            print("")
            templates()
            print("")
            print("Чтобы вернуться в меню, введите: меню")
            while True:
                back = input()
                if back == "меню":
                    menu()
                    break
                else:
                    clear()
                    templates()
                    print("")
                    print("Неверный ввод, попробуйте еще раз")
                    print("Чтобы вернуться в меню, введите: меню")

            break
        elif choice == "удалить":
            print("Какой шаблон удалить?")
            print("")
            templates()
            print("")                
            a = int(input()) - 1
            while True:    
                try:
                    texts.pop(a)

                    break
                except IndexError:
                    clear()

                    print("У вас нет шаблона под этим номером! Попробуйте еще раз")
                    print("Какой шаблон удалить?")
                    print("")
                    templates()
                    print("")
                    a = int(input()) - 1
                
            clear()

            print("Ваши шаблоны:")
            print("")
            templates()
            print("")
            print("Чтобы вернуться в меню, введите: меню")
            while True:
                back = input()
                if back == "меню":
                    menu()
                    break
                else:
                    clear()
                    templates()
                    print("")
                    print("Неверный ввод, попробуйте еще раз")
                    print("Чтобы вернуться в меню, введите: меню")

            break
        elif choice == "переместить":
            print("Какой шаблон и куда вы хотите переместить?")

            break
        else:
            print("Добавить или удалить шаблон? Добавить/Удалить")
            print("")
            print("Неверный ввод, попробуйте еще раз")
            choice = input().lower()

# Функция для печати один раз
def typer():
    time.sleep(0.05)

    keyboard.write(texts[x], delay=0.025)
    keyboard.press_and_release('enter')

# Функция для печати без остановки (по кругу)
def typer_scr():
    while True:
        time.sleep(0.05)

        keyboard.write(texts[x], delay=0.025)
        keyboard.press_and_release('enter')

        if keyboard.is_pressed('del'):
            break