# Иван Васильевич пришел на рынок и решил купить два арбуза: 
# один для себя, а другой для тещи. Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. 
# Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!

import random

quantity_watermelon = int(input("Введите кол-во арбузов: "))

watermelons = [0] * quantity_watermelon # СПИСОК арбузов)

# заполнение СПИСКА арбузов
for i in range(quantity_watermelon):
    watermelons[i] = random.randint(4, 7) + round(random.random(), 2)

print(watermelons)

max = watermelons[i]
min = watermelons[i]

# нахождение арбуза с минимальным и с максимальным весом
for i in range(quantity_watermelon - 1):
    if watermelons[i + 1] > max:
        max = watermelons[i + 1]
    if watermelons[i + 1] < min:
        min = watermelons[i + 1]

print(f"Арбуз для тещи: {min} кг, арбуз для Ивана Васильевича: {max} кг")