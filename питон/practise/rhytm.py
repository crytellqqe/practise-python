import keyboard

# Переменная отвечающая за нажимаемую кнопку
button = "space"

# Менюшка
def menu():
    print("*****Clicker Terminal*****")
    print("")
    print("Play (Write: play)")
    print("Change button for click (Write: change)")
    print(f"button: {button}")
    global choice
    while True:
        choice = input().lower()
        if choice == "play":
            game()
            break
        elif choice == "change":
            change_button()
            break

# Изменение кнопки
def change_button():
    print("Write button for clicking or ESC for leave to menu")
    global button
    button = input().lower()

    if button == "esc":
        menu()
    
    menu()

# Игра
def click():
    print("WoW")

def game():
    print("Click for effect")

    click_hotkey = keyboard.add_hotkey(button, click)

    keyboard.wait("esc")

    keyboard.remove_hotkey(click_hotkey)

    menu()

# Запуск
menu()