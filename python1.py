import time
import random

print("Перед началом игры выберите конверт:")
print("1) Зелёный конверт")
print("2) Красный конверт")
rand = random.randint(1, 2)
c = int(input())
if c == rand:
    print("Вы открыли конверт. В нём ничего не оказалось")
else:
    print("Вы открыли конверт и прочли текст:")
    print("Отныне и навсегда вас зовут Minecraft_Fan_2015")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
time.sleep(3)
print("Вы заспавнились в странном месте")
time.sleep(2)
print("Перед вами вырастает здание, похожее на школу. Хотите войти?")
print("1) Да")
print("2) Нет")
a = int(input())
if a == 1:
    print("Вы вошли. Это действительно школа. Третий этаж выглядит неестественно современным")
else:
    print("Что-ж. У вас в любом случае нет выбора")
    time.sleep(1)
    print("Вы вошли. Это действительно школа. Третий этаж выглядит неестественно современным")
time.sleep(3)
print("Вас встречает человек. Вроде... Вдруг это робот?")
time.sleep(3)
print(" - Привет! Меня зовут Ростислав. Я преподаю здесь доп. образование. Как тебя зовут?")
print("Введите имя:")
name = input()
if c == rand:
    print(" - Приятно познакомиться,", name)
else:
    print(" - Кого ты обманываешь, Minecraft_Fan_2015?")
time.sleep(2)
print('Не обращай внимания на звуки из кабинетов. Это мы пытаемся решить "Звёздный путь"')
time.sleep(4)
print(" - Не хочешь присоединиться?")
print("1) Хочу")
print("2) Не хочу")
b = int(input())
if b == 1:
    print("Вы зашли в кабинет, сели за ноутбук и открыли задание. Ближайшую вечность вы проведёте за решением задач")
else:
    print("Ростиславу не понравился ваш ответ. Ближайшую вечность вы проведёте за подбором тем для индивидуального проекта")
