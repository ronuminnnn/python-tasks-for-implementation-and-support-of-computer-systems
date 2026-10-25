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
max_health = health
# --- Враги -----------------------------------
enemies = ["химичка", "биологичка", "олимпиадник", "сирота"]
log = []
gold_total = 0
ability_bonus = 0
# --- Функции ---------------------------------------
def hero_hit(strike_n):
    """Урон героя в удар номер strike_n.
    Возвращает пару (hit, crit): урон и признак критического удара.
    Читает глобальные правила damage и crit_damage, не меняет ничего.
    """
    if strike_n % 3 == 0:
        return crit_damage, True
    return damage, False
def fight(enemy, hero_health, bonus = 0):
    """Бой с enemy до гибели одного из двоих.
    Возвращает раунды, победу, здоровье героя и полученное золото."""
    enemy_hp = 45.0
    rounds = []
    round_n = 0
    print(f"Вы заходите глубже в лабораторию. Из темноты выходит {enemy}!")
    while enemy_hp > 0 and hero_health > 0:
        round_n += 1
        hit, crit = hero_hit(round_n)
        hit += bonus
        enemy_hp -= hit
        line = f"Раунд {round_n}: вы наносите {hit:.1f} урона"
        if crit:
            line += " — критический!"
        else:
            line += "."
        if enemy_hp <= 0:
            line += " Враг падает."
            rounds.append([round_n, hit, 0])
        else:
            blow = random.randint(2, 6)
            hero_health -= blow
            line += f" Здоровье врага: {enemy_hp:.1f}. {enemy.capitalize()} бьёт в ответ на {blow}."
            rounds.append([round_n, hit, blow])
        print(line)
    won = enemy_hp <= 0
    if won:
        loot = 10 + 5 * round_n
    else:
        loot = 0
    return rounds, won, hero_health, loot

def buy(price, gold, quantity=1):
    cost = price * quantity
    if gold >= cost:
        return gold - cost, True
    return gold, False

def print_leaderboard(log):
    """Печатает топ-3 раундов по урону героя и рекорд врага.
    Возвращает None: контракт функции — печать, а не данные.
    """
    if not log:
        print("Вы ещё не дрались.")
        return
    top = sorted(log, key=lambda r: r[1], reverse=True)[:3]
    print("Таблица лидеров (урон героя):")
    for i in range(len(top)):
        print(f"{i + 1}. Раунд {top[i][0]}: {top[i][1]:.1f}")
    worst = max(log, key=lambda r: r[2])
    print(f"Самый сильный удар врага: {worst[2]} (раунд {worst[0]}).")


def print_run_summary(log):
    """Печатает итог забега: суммарный и средний урон героя.
    Возвращает None. Безопасна на пустом журнале.
    """
    total = sum(r[1] for r in log)
    rounds = len(log)
    if rounds > 0:
        print(f"Общий урон: {total:.1f}, раундов: {rounds}, средний урон: {total / rounds:.1f}.")
    else:
        print("В этом забеге боёв не было.")
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
menu_last = 9
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
        print("9 - магазин")
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
                stamina = min(stamina + 1, max_stamina)
                print("Вы садитесь на стул, отдыхаете и восстанавливаете силы.")
            case "4":
                reading = reading + 2
                stamina = max(0, stamina - 4)
                print("Вы читаете учебник по химии и проводите реакции")
            case "5":
                reading = reading + 2
                stamina = max(0, stamina - 4)
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
                training_cost = 8
                if stamina >= training_cost:
                    stamina -= training_cost
                else:
                    health -= training_cost - stamina
                    stamina = 0
                    print("Сил не хватает — тренировка идёт за счёт здоровья.")
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
                    rounds, won, health, loot = fight(enemy, health, bonus=ability_bonus)
                    for r in rounds:
                        log.append(r)
                    if won:
                        gold_total += loot
                        enemies.remove(enemy)   
                        print(
                            f"{enemy.capitalize()} повержен! "
                            f"{len(enemies)} врагов осталось в лаборатории.")
                        print(f"Получено золота: {loot}")
                        print(f"Раундов в бою: {len(rounds)}.")
            case "8":
                print_leaderboard(log)
            case "9":
                print("Магазин:")
                print("1 - зелье (+10 здоровья): 10 золота")
                print("2 - споры грибов (+6 запаса сил): 15 золота")
                print("3 - жидкий уран (+4 к урону): 40 золота")
                print("0 - назад")
                print(f"Твоё золото: {gold_total}")

                item = input("Выбери товар: ")

                if item in ("1", "2", "3"):
                    prices = (10, 15, 40)
                    names = ("зелье", "споры грибов", "жидкий уран")

                    price = prices[int(item) - 1]
                    name = names[int(item) - 1]

                    qty_line = input("Количество (Enter — 1): ")

                    if qty_line == "":
                        qty = 1
                    elif qty_line.isdigit() and int(qty_line) > 0:
                        qty = int(qty_line)
                    else:
                        qty = 0

                    if qty == 0:
                        print("Введите целое число больше нуля.")
                    else:
                        gold_left, ok = buy(price, gold_total, qty)

                        if not ok:
                            print("Недостаточно золота!")
                        else:
                            gold_total = gold_left

                            if item == "1":
                                health = min(health + 10 * qty, max_health)
                            elif item == "2":
                                stamina = min(stamina + 6 * qty, max_stamina)
                            else:
                                ability_bonus += 4 * qty

                            print(f"Куплено: {name} × {qty}.")
                            print(f"Осталось золота: {gold_total}")

                elif item != "0":
                    print("Такого товара нет.")
            case "0":
                print("Вы идете к двери. Лаборатория остается позади.")
                outcome = "выход"
                running = False
        print()
        print(f"Здоровье: {health} Запас сил: {stamina} Врагов осталось: {len(enemies)} Золото: {gold_total}")
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
    print(f"Бонус к урону: {ability_bonus}")
    print(f"Золото: {gold_total}")
    print()
    print(frame)

    if outcome == "гибель":
        print(f"Ты не дошёл, {hero_name}. Действий совершено: {actions}.")
    elif outcome == "выход":
        print(f"Забег окончен, {hero_name}. Действий совершено: {actions}.")
    else:
        print(f"Ты покинул лабораторию, {hero_name}. Действий совершено: {actions}.")
    print_run_summary(log)
    print(frame)