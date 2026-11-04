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
# --- Прейскурант, рюкзак, характеристики врагов ---
prices = {"Зелье": 10, "Споры": 15, "Жидкий уран": 40}
inventory = {}
enemy_stats = {
    "химичка": {"hp": 45, "damage": 6, "loot": 25},
    "биологичка": {"hp": 30, "damage": 4, "loot": 15},
    "олимпиадник": {"hp": 20, "damage": 3, "loot": 10},
    "сирота": {"hp": 12, "damage": 2, "loot": 5},
}
log = []
gold_total = 0
ability_bonus = 0
# --- Команды (этап 12) -----------------------------
num_to_verb = {"1": "look", "2": "go", "3": "rest", "4": "chem",
               "5": "bio", "6": "train", "7": "descend", "8": "leaders",
               "9": "shop", "10": "backpack", "11": "drink", "0": "exit"}

aliases = {"осмотреться": "look", "идти": "go", "отдых": "rest",
           "химия": "chem", "биология": "bio", "тренировка": "train",
           "глубже": "descend", "лидеры": "leaders", "магазин": "shop",
           "рюкзак": "backpack", "выпить": "drink", "купить": "buy",
           "помощь": "help", "выход": "exit"}

commands = ["look", "go", "rest", "chem", "bio", "train", "descend",
            "leaders", "shop", "backpack", "drink зелье",
            "buy <товар> [кол-во]", "exit"]

MENU = ["Что делаешь? (номер или команда; help - справка)",
        "1 - осмотреться (look)",
        "2 - идти вперёд (go)",
        "3 - отдохнуть (rest)",
        "4 - заняться химией (chem)",
        "5 - заняться биологией (bio)",
        "6 - тренировка (train)",
        "7 - зайти глубже (descend)",
        "8 - таблица лидеров (leaders)",
        "9 - магазин (shop)",
        "10 - рюкзак (backpack)",
        "11 - выпить зелье (drink)",
        "0 - выйти из подземелья (exit)"]
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
    Карточка врага берётся из enemy_stats по имени: нужны ключи
    hp, damage, loot.
    Возвращает раунды, победу, здоровье героя и полученное золото."""
    stats = enemy_stats[enemy]
    enemy_hp = float(stats["hp"])
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
            blow = stats["damage"]
            hero_health -= blow
            line += f" Здоровье врага: {enemy_hp:.1f}. {enemy.capitalize()} бьёт в ответ на {blow}."
            rounds.append([round_n, hit, blow])
        print(line)
    won = enemy_hp <= 0
    loot = stats["loot"] if won else 0
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
outcome = "прерывание"
try:
    while running:
        print("\n".join(MENU))
        print()

        line = input()
        cmd = line.strip().lower()
        while cmd == "":
            print("Пустая команда. Введите команду или номер.")
            line = input()
            cmd = line.strip().lower()

        words = cmd.split()
        verb = words[0]
        verb = aliases.get(verb, verb)
        if cmd in num_to_verb:
            verb = num_to_verb[cmd]
    # --- Выбор героя -----------------------------------
        match verb:
            case "look":
                print("Вы осмотрелись. В комнате полно людей, много книг на полу.")
            case "go":
                cost = 2
                if stamina >= cost:
                    stamina -= cost
                    print("Вы осторожно идёте вперёд. Пол скрипит под ногами.")
                else:
                    health -= cost - stamina
                    stamina = 0
                    print("Сил больше нет — вы идёте на одном упорстве.")
            case "rest":
                stamina = min(stamina + 1, max_stamina)
                print("Вы садитесь на стул, отдыхаете и восстанавливаете силы.")
            case "chem":
                reading = reading + 2
                stamina = max(0, stamina - 4)
                print("Вы читаете учебник по химии и проводите реакции")
            case "bio":
                reading = reading + 2
                stamina = max(0, stamina - 4)
                print("Вы читаете учебник по биологии и решаете задачки на генетику")
            case "train":
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
                training_cost = 5
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
            case "descend":
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
            case "leaders":
                print_leaderboard(log)
            case "shop":
                print("Магазин:")
                for name, price in prices.items():
                    print(f"{name}: {price} золота")
                print(f"Твоё золото: {gold_total}")
                print("Чтобы купить, введите: buy <товар> [кол-во]")
            case "buy":
                if len(words) > 1 and words[-1].isdigit():
                    qty = int(words[-1])
                    item = " ".join(words[1:-1]).capitalize()
                else:
                    qty = 1
                    item = " ".join(words[1:]).capitalize()
                if item == "":
                    print("Что купить? Введите: buy <товар> [кол-во].")
                    continue
                if item not in prices:
                    print("Такого товара нет в магазине.")
                    continue
                if qty == 0:
                    print("Количество должно быть больше нуля.")
                    continue
                price = prices[item]
                gold_total, ok = buy(price, gold_total, quantity=qty)
                if ok:
                    if item == "Зелье":
                        inventory[item] = inventory.get(item, 0) + qty
                    elif item == "Споры":
                        stamina = min(stamina + 6 * qty, max_stamina)
                    else:
                        ability_bonus += 4 * qty
                    print(f"Куплено: {item} × {qty} за {price * qty} золота.")
                    print(f"Осталось золота: {gold_total}")
                else:
                    print(f"Недостаточно золота: нужно {price * qty}, есть {gold_total}.")
                    continue
            case "backpack":
                if not inventory:
                    print("Рюкзак пуст.")
                else:
                    print("Рюкзак:")
                    for name, qty in inventory.items():
                        print(f"{name}: {qty} шт.")
            case "drink":
                item = " ".join(words[1:]).capitalize() or "Зелье"
                if item != "Зелье":
                    print(f"Предмет «{item}» нельзя выпить.")
                    continue
                if inventory.get("Зелье", 0) == 0:
                    print("В рюкзаке нет зелий.")
                    continue
                health = min(health + 10, max_health)
                inventory["Зелье"] -= 1
                if inventory["Зелье"] == 0:
                    del inventory["Зелье"]
                print(f"Вы пьёте зелье. Здоровье: {health}. Зелий осталось: {inventory.get('Зелье', 0)}.")
            case "exit":
                print("Вы идете к двери. Лаборатория остается позади.")
                outcome = "выход"
                running = False
            case "help":
                print("Команды: " + ", ".join(commands) + ".")
                print("Номера 0-11 работают как раньше.")
            case _:
                print(f"Команды: '{line.strip()}' нет. Введите 'help'.")
                continue
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
    if inventory:
        print("В рюкзаке осталось:")
        for name, qty in inventory.items():
            print(f"{name}: {qty} шт.")
    else:
        print("В рюкзаке осталось: ничего.")
    print()
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