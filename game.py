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
import random
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
while True:
    try:
        health = int(input())
        strength = int(input())
        agility = int(input())
        reading = int(input())
        if health <= 0:
            raise ValueError(
                f"Здоровье должно быть больше 0, а введено {health}"
            )
        if strength > 20 or strength < 0:
            raise ValueError(
                f"Сила должна быть от 0 до 20, а введено {strength}"
            )
        if agility < 0 or reading < 0:
            raise ValueError(
                "Ловкость и начитанность не могут быть отрицательными"
            )
        break
    except ValueError as e:
        print(f"Ошибка: {e}. Введите все четыре характеристики заново:")
# --- Расчёт урона ----------------------------------
base_attack = 10
damage = base_attack + strength * 1.5
crit_damage = damage * 2
stamina = health * 0.3
max_stamina = stamina
# --- Формуляр героя --------------------------------
print("Характеристики героя:")
print(f"Здоровье: {health}")
print(f"Сила: {strength}")
print(f"Ловкость: {agility}")
print(f"Начитанность: {reading}")
print()
print(f"Урон героя: {damage:.1f}")
print(f"Критический урон: {crit_damage:.1f}")
print(f"Стамина: {stamina:.1f}")
# --- Главный цикл игры ---------------------------
running = True
actions = 0
menu_last = 8
enemies = ["химичка", "биологичка", "олипиадник", "сирота"]
log = []
outcome = "прерывание"
try:
    while running:
        # --- Меню действий ---------------------------------
        print("Что делаешь?")
        print("1 - осмотреться")
        print("2 - идти вперёд")
        print("3 - отдохнуть")
        print("4 - заняться химией")
        print("5 - заняться биологией")
        print("6 - тренировка")
        print("7 - зайти глубже")
        print("8 - таблица лидеров")
        print("0 - выйти из подземелья")
        print()
    # --- Выбор героя -----------------------------------
        while True:
            choice = input()
            try:
                menu_number = int(choice)
            except ValueError:
                print("Ошибка ввода! Введи номер пункта из меню:")
                continue
            if 0 <= menu_number <= menu_last:
                choice = str(menu_number)
                break
            print("Такого пункта нет. Введи номер пункта из меню:")
        match choice:
            case "1":
                print("Вы осмотрелись. В комнате полно людей, много книг на полу.")
            case "2":
                cost = 2
                if stamina >= cost:
                    stamina -= cost
                    print("Вы осторожно идёте вперёд. Пол скрипит под ногами.")
                else:
                    health -= cost - stamina
                    stamina = 0
                    print("Сил больше нет — вы идёте на одном упорстве.")
            case "3":
                stamina = min(stamina + 1, 10)
                print("Вы садитесь на стул, отдыхаете и восстанавливаете силы.")
            case "4":
                reading = reading + 2
                stamina = stamina - 4
                print("Вы читаете учебник по химии и проводите реакции")
            case "5":
                reading = reading + 2
                stamina = stamina - 4
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
                stamina = stamina - 5
                print()
                print(f"Итог: ударов: {strikes}, критических: {crit_count}")
                print(f"Всего нанесено урона: {total_damage:.1f}")
                average_damage = total_damage / strikes
                print(f"Средний урон: {average_damage:.1f}")
                print("Тренировка завершена. Вы потратили 5 единиц силы.")
            case "7":
                if not enemies:
                    print("Вы заходите глубже в лабораторию, но там пусто: врагов не осталось.")
                else:
                    enemy = random.choice(enemies)
                    enemy_hp = 60
                    round_n = 0
                    print(f"Вы заходите глубже в лабораторию. Из темноты выходит {enemy}!")
                    while enemy_hp > 0 and health > 0:
                        round_n += 1
                        if round_n % 3 == 0:
                            hit_damage = crit_damage
                            hit_end = " — критический!"
                        else:
                            hit_damage = damage
                            hit_end = "."
                        enemy_hp -= hit_damage
                        enemy_damage = 0
                        if enemy_hp <= 0:
                            print(f"Раунд {round_n}: вы наносите {hit_damage:.1f} урона{hit_end} Враг падает.")
                        else:
                            enemy_damage = random.randint(2, 6)
                            health -= enemy_damage
                            print(f"Раунд {round_n}: вы наносите {hit_damage:.1f} урона{hit_end} "
                                  f"Здоровье врага: {enemy_hp:.1f}. {enemy.capitalize()} бьёт в ответ на {enemy_damage}.")
                        log.append([round_n, hit_damage, enemy_damage])
                    if enemy_hp <= 0:
                        enemies.remove(enemy)
                        print(f"{enemy.capitalize()} повержен! Врагов в лаборатории осталось: {len(enemies)}.")
                    print(f"Раундов в бою: {round_n}.")
                    print(f"Последний раунд: урон героя {log[-1][1]:.1f}, урон врага {log[-1][2]}.")
            case "8":
                if not log:
                    print("Вы ещё не дрались.")
                else:
                    top = sorted(log, key=lambda r: r[1], reverse=True)[:3]
                    print("Таблица лидеров (урон героя):")
                    for i in range(len(top)):
                        print(f"{i + 1}. Раунд {top[i][0]}: {top[i][1]:.1f}")
                    worst = max(log, key=lambda r: r[2])
                    print(f"Самый сильный удар врага: {worst[2]} (раунд {worst[0]}).")
            case "0":
                print("Вы идете к двери. Лаборатория остается позади.")
                outcome = "выход"
                running = False
        print()
        print(f"Здоровье: {health} Запас сил: {stamina} Врагов осталось: {len(enemies)}")
        if running:
            actions += 1
        if health <= 0:
            outcome = "гибель"
            print(f"{hero_name} падает без сил. Лаборатория забирает нового исследователя.")
            running = False
except KeyboardInterrupt:
    print()
    print("Игрок прервал сеанс.")

finally:
    print()
    print("Состояние героя:")
    print(f"Здоровье: {health}")
    print(f"Сила: {strength}")
    print(f"Ловкость: {agility}")
    print(f"Начитанность: {reading}")
    print(f"Стамина: {stamina}")
    print()
    print(frame)

    if outcome == "гибель":
        print(f"Ты не дошёл, {hero_name}. Действий совершено: {actions}.")
    elif outcome == "выход":
        print(f"Забег окончен, {hero_name}. Действий совершено: {actions}.")
    else:
        print(f"Ты покинул лабораторию, {hero_name}. Действий совершено: {actions}.")
    total = sum(r[1] for r in log)
    rounds = len(log)
    if rounds > 0:
        print(f"Общий урон: {total:.1f}, раундов: {rounds}, средний урон: {total / rounds:.1f}.")
    else:
        print("В этом забеге боёв не было.")
    print(frame)