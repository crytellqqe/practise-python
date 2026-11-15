print("Введите два числа:")

a = int(input())
b = int(input())

while b == 0:
    print("На ноль делить нельзя!!! Перепиши второе число:")
    b = int(input())

sum = a + b
difference = a - b
product = a * b
division = a // b

print(f"Сумма твоих чисел: {sum}")
print(f"Разность твоих чисел: {difference}")
print(f"Произведение твоих чисел: {product}")
print(f"Частное твоих чисел: {division}")