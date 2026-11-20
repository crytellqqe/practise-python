import keyboard

# Переменная отвечающая за нажимаемую кнопку
button = "space"
tittle = "WoW"

# Менюшка
def menu():
    print("*****Clicker Terminal*****")
    print("")
    print("Play (Write: play)")
    print("")
    print("Change button for click (Write: change)")
    print("Change text when click (Write: text)")
    print("")
    print(f"button: {button}")
    print(f"Text on click: {tittle}")
    print("")
    print("For leave write: exit")
    global choice
    while True:
        choice = input().lower()
        if choice == "play":
            game()
            break
        elif choice == "change":
            change_button()
            break
        elif choice == "text":
            tittle_d()
            break
        elif choice == "exit":
            break

# Изменение кнопки
def change_button():
    print("Write button for clicking or ESC for leave to menu")
    global button
    button = input().lower()

    if button == "esc":
        menu()
    
    menu()

# Смена надписи от клика
def tittle_d():
    print("Write your text, what you want to see when clicked:")
    global tittle
    tittle = input()

    menu()

# Игра
def click():
    print(tittle)

def game():
    print("Click for effect")

    click_hotkey = keyboard.add_hotkey(button, click)

    keyboard.wait("esc")

    keyboard.remove_hotkey(click_hotkey)

    menu()

# Запуск
menu()