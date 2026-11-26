balance = 0
target = 1000
print(f"Твоя цель накопить {target}, сколько хочешь отложить сейчас?")
while balance < target:
    plus_money = input()
    try:
        plus_money = int(plus_money)
    except ValueError:
        print("Введите еще раз")
        plus_money = input()
    balance += plus_money
    if balance < target:
        print(f"Сейчас в копилке: {balance}")
        print("Сколько еще отложишь?")
print(f"Все, накопил! В твоей копилке {balance}. Можешь идти за своей резиновой... Ну ты понял, рад за тебя!")