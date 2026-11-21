from mechanism import menu, text_w, typer, typer_scr
import keyboard

# Запуск скрипта
menu()

# Горячие клавиши
keyboard.add_hotkey('f9', text_w)
keyboard.add_hotkey('f7', typer)
keyboard.add_hotkey('f8', typer_scr)
    
keyboard.wait('alt+del')