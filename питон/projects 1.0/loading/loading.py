import time
import pygame

percentages = 0

print(f"Loading...")
time.sleep(1)
while True:
    print(f"Loading {percentages}%")
    percentages += 1
    time.sleep(0.06)
    if percentages == 100:
        break
print("Complete!")
time.sleep(0.3)
print(":)")
time.sleep(0.2)
print(":)")
time.sleep(0.1)
print(":)")
time.sleep(0.05)
print(":)")

pygame.display.init()

IMAGE_FILE = "image.jpg"
img = pygame.image.load(IMAGE_FILE)

info = pygame.display.Info()
screen = pygame.display.set_mode((info.current_w, info.current_h), pygame.FULLSCREEN)

img_scaled = pygame.transform.scale(img, (info.current_w, info.current_h))

screen.blit(img_scaled, (0, 0))
pygame.display.flip()

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
      running = False

pygame.quit()