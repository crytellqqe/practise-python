import keyboard

# Переменная отвечающая за нажимаемую кнопку
button = "space"
tittle = "WoW"

# Менюшка
def menu():
    print("*****Clicker.Terminal*****")
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
    while True:
        choice = input("$ > ").lower()
        if choice == "play":
            game()
            return
        elif choice == "change":
            change_button()
            return
        elif choice == "text":
            tittle_d()
            return
        elif choice == "exit":
            break
        else:
            print("Invalid input, try again!")

# Изменение кнопки
def change_button():
    global button

    print("Write button for clicking or ESC for leave to menu")
    while True:   
        new_button = input("$ > ").lower()

        if new_button == "esc":
            menu()
            break

        button = new_button
        print("Maybe another key? Or leave by writing ESC")


# Смена надписи от клика
def tittle_d():
    global tittle

    print("Write your text, what you want to see when clicked. Or ESC for leave")
    while True:
        new_tittle = input("$ > ")

        if new_tittle.lower() == "esc":
            menu()
            break

        tittle = new_tittle
        print("Maybe another text? Or leave by writing ESC")

# Игра
def click():
    print(tittle)

def game():
    print("Click!")

    click_hotkey = keyboard.add_hotkey(button, click)

    keyboard.wait("esc")

    keyboard.remove_hotkey(click_hotkey)

    menu()

# Запуск
menu()