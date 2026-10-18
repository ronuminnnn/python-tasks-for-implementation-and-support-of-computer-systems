# ================================================
    # ИГРА «ШКОЛЬНАЯ ЛАБОРАТОРИЯ»
# Автор: Александра Фоминых
# Дата: сентябрь 2026
#
# Пункт 4 — «заняться химией»: герой проходит в лабораторию
# и начинает изучать химию. Пока
# пункт только выводится в меню — обрабатывать
# его будем на третьем занятии.
# ================================================
# --- Заголовок ------------------------------------
title = "ШКОЛЬНАЯ ЛАБОРАТОРИЯ"
frame = "=" * 26
print(frame)
print(" " + title + " ")
print(frame)
print()
# --- Знакомство с героем --------------------------
print("Как зовут героя?")
hero_name = input()
print(f"Добро пожаловать, {hero_name}!")
print("Ты заходишь в лабораторию. Здесь много людей и пахнет книгами.")
print()
# --- Настройка героя -------------------------------
print("Настройка героя.")
print("Здоровье, сила, ловкость, начитанность — по одному числу в строке:")
health = int(input())
strength = int(input())
agility = int(input())
reading = int(input())
# --- Расчёт урона ----------------------------------
base_attack = 10
damage = base_attack + strength * 1.5
crit_damage = damage * 2
# --- Формуляр героя --------------------------------
print("Характеристики героя:")
print(f"Здоровье: {health}")
print(f"Сила: {strength}")
print(f"Ловкость: {agility}")
print(f"Начитанность: {reading}")
print()
print(f"Урон героя: {damage:.1f}")
print(f"Критический урон: {crit_damage:.1f}")
# --- Меню действий ---------------------------------
# --- Главный цикл игры ---------------------------
running = True
actions = 0
while running:
    print("Что делаешь?")
    print("1 - осмотреться")
    print("2 - идти вперёд")
    print("3 - отдохнуть")
    print("4 - заняться химией")
    print("5 - заняться биологией")
    print("6 - тренировка")
    print("0 - выйти из подземелья")
    print()
    # --- Выбор героя -----------------------------------
    valid = ("0", "1", "2", "3", "4", "5", "6")
    choice = input()
    while choice not in valid:
        print("Такого пункта нет. Введи номер пункта из меню.")
        choice = input()
    match choice:
        case "1":
            print("Вы осмотрелись. В комнате полно людей, много книг на полу.")
        case "2":
            cost = 2
            if strength >= cost:
                strength -= cost
                print("Вы осторожно идёте вперёд. Пол скрипит под ногами.")
            else:
                health -= cost - strength
                strength = 0
                print("Сил больше нет — вы идёте на одном упорстве.")
        case "3":
            strength = min(strength + 1, 10)
            print("Вы садитесь на стул, отдыхаете и восстанавливаете силы.")
        case "4":
            reading = reading + 2
            strength = strength - 4
            print("Вы читаете учебник по химии и проводите реакции")
        case "5":
            reading = reading + 2
            strength = strength - 4
            print("Вы читаете учебник по биологии и решаете задачки на генетику")
        case "6":
            strikes = 9
            total_damage = 0
            crit_count = 0
            print("Вы подходите к столу, на котором лежит тренировочный вариант ЕГЭ.")
            print("Он лежит тут, с тех пор, как последний школьник не сдал ЕГЭ на проходной балл.")
            print()
            print(f"Наносите {strikes} ударов.")
            for i in range(1, strikes + 1):
                if i % 3 == 0:
                    hit_damage = crit_damage
                    crit_count += 1
                    print(f"Удар {i}: {hit_damage:.1f} урона — критический!")
                else:
                    hit_damage = damage
                    print(f"Удар {i}: {hit_damage:.1f} урона")
                total_damage += hit_damage
            strength = strength - 5
            print()
            print(f"Итог: ударов: {strikes}, критических: {crit_count}")
            print(f"Всего нанесено урона: {total_damage:.1f}")
            average_damage = total_damage / strikes
            print(f"Средний урон: {average_damage:.1f}")
            print("Тренировка завершена. Вы потратили 5 единиц силы.")
        case "0":
            print("Вы идете к двери. Лаборатория остается позади.")
            running = False
    print()
    print(f"Здоровье: {health} Запас сил: {strength}")
    if running:
        actions += 1
    if health <= 0:
        print(f"{hero_name} падает без сил. Лаборатория забирает нового исследователя.")
        running = False
print("Состояние героя:")
print(f"Здоровье: {health}")
print(f"Сила: {strength}")
print(f"Ловкость: {agility}")
print(f"Начитанность: {reading}")
print()
# --- Прощание -----------------------------------
frame = "=" * 26
print(frame)
if health <= 0:
    print(f"Ты не дошёл, {hero_name}. Действий совершено: {actions}.")
else:
    print(f"Забег окончен, {hero_name}. Действий совершено: {actions}.")
print(frame)