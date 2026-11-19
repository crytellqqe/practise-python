import os
import random
import tkinter as tk
from playsound3 import playsound


class SafePrankApp:

  def __init__(self, sound_path):
    self.root = tk.Tk()
    self.root.withdraw()  # Скрываем главное техническое окно
    self.running = True
    self.windows = []
    self.sound = None

    # Запускаем звук, если файл существует
    if os.path.exists(sound_path):
      self.sound = playsound(sound_path, block=False)

    # Назначаем бинд (горячую клавишу) на остановку — клавиша Escape
    self.root.bind_all("<Escape>", self.stop_all)

    # Запускаем цикл появления безопасных окон
    self.spawn_window()
    self.root.mainloop()

  def spawn_window(self):
    if not self.running:
      return

    # Ограничиваем максимум до 30 окон на экране для полной безопасности системы
    if len(self.windows) < 1000:
      win = tk.Toplevel(self.root)
      win.title("SDFasfFdsafasfe")

      # Случайные координаты на экране
      x = random.randint(100, 1500)
      y = random.randint(100, 1500)
      win.geometry(f"400x200+{x}+{y}")

      label = tk.Label(
          win, text="dsjkghiasdhgigeiogwaighiopadklfsklf", font=("Arial", 10)
      )
      label.pack(expand=True)

      # Привязываем бинд остановки к каждому новому окну
      win.bind("<Escape>", self.stop_all)
      self.windows.append(win)

    # Повторяем каждые 300 миллисекунд (0.3 секунды)
    self.root.after(5, self.spawn_window)

  def stop_all(self, event=None):
    self.running = False
    # Останавливаем звук, если он ещё играет
    if self.sound and self.sound.is_alive():
      self.sound.stop()
    # Мгновенно закрываем все окна и завершаем программу
    self.root.destroy()


if __name__ == "__main__":
  my_sound = "laugh.mp3"
  SafePrankApp(my_sound)