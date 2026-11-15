from mechanism import type, text, typer, typer_scr
import keyboard

keyboard.add_hotkey('f7', typer)
keyboard.add_hotkey('f8', typer_scr)
    
keyboard.wait('alt+del')