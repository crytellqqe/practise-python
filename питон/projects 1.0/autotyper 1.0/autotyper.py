from mechanism import menu, text_w, templates, f10_templates, add_or_delete, typer, typer_scr
import keyboard

# Запуск скрипта
menu()

# Горячие клавиши
keyboard.add_hotkey('f9', text_w)
keyboard.add_hotkey('f10', f10_templates)
keyboard.add_hotkey('ctrl + f10', add_or_delete)
keyboard.add_hotkey('f7', typer)
keyboard.add_hotkey('f8', typer_scr)
    
keyboard.wait('alt+del')