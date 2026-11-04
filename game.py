# ================================================
    # ИГРА «ШКОЛЬНАЯ ЛАБОРАТОРИЯ»
# Автор: Александра Фоминых
# Дата: сентябрь 2026
# ================================================
import random
import dungeon
import json
import os
try:
    from colorama import Fore, Style, init
    init()
    COLOR = True
except ImportError:
    COLOR = False
# --- Заголовок ------------------------------------
title = "ШКОЛЬНАЯ ЛАБОРАТОРИЯ"
frame = "=" * 26
print(frame)
print(" " + title + " ")
print(frame)
print()
# --- Сохранение -------------------------
loaded = None
if os.path.exists("save.json"):
    print("Найдено сохранение. Продолжить забег? (да/нет)")
    answer = input().strip().lower()
    if answer in ("да", "yes", "y"):
        try:
            with open("save.json", encoding="utf-8") as f:
                loaded = json.load(f)
        except (json.JSONDecodeError, OSError):
            print("Сохранение повреждено. Начинаем новый забег.")
            loaded = None
# --- Знакомство с героем --------------------------
if loaded is None:
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
else:
    hero_name = loaded["hero"]
    health = loaded["health"]
    strength = loaded["strength"]
    agility = loaded["agility"]
    reading = loaded["reading"]
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
inventory = {}
log = []
gold_total = 0
ability_bonus = 0
# --- Карта подземелья --------------------
MAP = [
    ["#", "#", "#", "#", "#"],
    ["#", ".", ".", "#", "#"],
    ["#", ".", "#", ".", "#"],
    ["#", ".", ".", ".", "#"],
    ["#", "#", "S", ".", "#"],
]
hero_r, hero_c = 4, 2
visited = {(4, 2)}

LOOT = {(1, 1): "старая колба", (2, 3): "пыльная пробирка",
        (3, 3): "микроскоп охранника"}
found_loot = set()

DIRECTIONS = {"north": (-1, 0), "south": (1, 0),
              "west": (0, -1), "east": (0, 1)}
DIR_ALIASES = {"север": "north", "юг": "south",
               "запад": "west", "восток": "east"}
DIR_NAMES = {"north": "на север", "south": "на юг",
             "west": "на запад", "east": "на восток"}
# --- Команды -----------------------------
num_to_verb = {"1": "look", "2": "go", "3": "rest", "4": "chem",
               "5": "bio", "6": "train", "7": "descend", "8": "leaders",
               "9": "shop", "10": "backpack", "11": "drink",
               "12": "map", "13": "scout", "0": "exit"}

aliases = {"осмотреться": "look", "идти": "go", "отдых": "rest",
           "химия": "chem", "биология": "bio", "тренировка": "train",
           "глубже": "descend", "лидеры": "leaders", "магазин": "shop",
           "рюкзак": "backpack", "выпить": "drink", "купить": "buy",
           "помощь": "help", "выход": "exit",
           "карта": "map", "разведка": "scout"}

commands = ["look", "go [north/south/west/east]", "rest", "chem", "bio",
            "train", "descend", "leaders", "shop", "backpack",
            "drink зелье", "buy <товар> [кол-во]", "map", "scout", "exit"]

MENU = ["Что делаешь? (номер или команда; help - справка)",
        "1 - осмотреться (look)",
        "2 - идти вперёд / по карте (go [north/south/west/east])",
        "3 - отдохнуть (rest)",
        "4 - заняться химией (chem)",
        "5 - заняться биологией (bio)",
        "6 - тренировка (train)",
        "7 - зайти глубже (descend)",
        "8 - таблица лидеров (leaders)",
        "9 - магазин (shop)",
        "10 - рюкзак (backpack)",
        "11 - выпить зелье (drink)",
        "12 - карта (map)",
        "13 - разведка (scout)",
        "0 - выйти из подземелья (exit)"]
# --- Функции ---------------------------------------
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

def scout(r, c, seen):
    """Считает доступные комнаты."""
    if r < 0 or r >= len(MAP):
        return 0
    if c < 0 or c >= len(MAP[r]):
        return 0
    if (r, c) in seen or MAP[r][c] == "#":
        return 0
    seen.add((r, c))
    total = 1
    for dr, dc in DIRECTIONS.values():
        total += scout(r + dr, c + dc, seen)
    return total
def write_save():
    """Собирает состояние забега и пишет его в save.json.
    Кортежи и множества превращает в списки: JSON их не знает.
    """
    save = {}
    save["hero"] = hero_name
    save["health"] = health
    save["stamina"] = stamina
    save["max_stamina"] = max_stamina
    save["max_health"] = max_health
    save["strength"] = strength
    save["agility"] = agility
    save["reading"] = reading
    save["gold"] = gold_total
    save["actions"] = actions
    save["ability_bonus"] = ability_bonus
    save["enemies"] = enemies
    save["inventory"] = inventory
    save["log"] = log
    save["position"] = [hero_r, hero_c]
    save["visited"] = [list(p) for p in visited]
    save["loot"] = sorted(found_loot)
    with open("save.json", "w", encoding="utf-8") as f:
        json.dump(save, f, ensure_ascii=False, indent=2)
# --- Восстановление забега ---------------
# Формуляр героя ниже печатается и при продолжении: так игрок сразу видит характеристики.
if loaded is not None:
    stamina = loaded["stamina"]
    max_stamina = loaded["max_stamina"]
    max_health = loaded["max_health"]
    gold_total = loaded["gold"]
    ability_bonus = loaded["ability_bonus"]
    enemies = loaded["enemies"]
    inventory = loaded["inventory"]
    log = loaded["log"]
    hero_r, hero_c = loaded["position"]
    visited = {tuple(p) for p in loaded["visited"]}
    found_loot = set(loaded["loot"])
    print(f"Забег продолжен: здоровье {health}, золото {gold_total}, врагов осталось {len(enemies)}.")
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
actions = 0 if loaded is None else loaded["actions"]
save_enabled = True
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
                direction = DIR_ALIASES.get(words[1], words[1]) if len(words) > 1 else ""
                if direction in DIRECTIONS:
                    dr, dc = DIRECTIONS[direction]
                    nr, nc = hero_r + dr, hero_c + dc
                    if 0 <= nr < len(MAP) and 0 <= nc < len(MAP[nr]) and MAP[nr][nc] != "#":
                        hero_r, hero_c = nr, nc
                        visited.add((hero_r, hero_c))
                        if (hero_r, hero_c) in LOOT:
                            loot_item = LOOT[(hero_r, hero_c)]
                            if loot_item not in found_loot:
                                found_loot.add(loot_item)
                                print(f"Вы нашли: {loot_item}! Уникального лута: {len(found_loot)}.")
                        print(f"Вы идёте {DIR_NAMES[direction]}. Комната ({hero_r}, {hero_c}).")
                    else:
                        print(f"Нельзя идти {DIR_NAMES[direction]}: стена или край карты.")
                else:
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
                    rounds, won, health, loot = dungeon.fight(enemy, health, ability_bonus, damage, crit_damage)
                    for r in rounds:
                        log.append(r)
                    if won:
                        gold_total += loot
                        enemies.remove(enemy)   
                        win_line = (f"{enemy.capitalize()} повержен! " 
                                    f"{len(enemies)} врагов осталось в лаборатории.")
                        if COLOR:
                            print(Fore.YELLOW + Style.BRIGHT + win_line + Style.RESET_ALL)
                        else:
                            print(win_line)
                        print(f"Получено золота: {loot}")
                        print(f"Раундов в бою: {len(rounds)}.")
            case "leaders":
                print_leaderboard(log)
            case "shop":
                print("Магазин:")
                for name, price in dungeon.prices.items():
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
                if item not in dungeon.prices:
                    print("Такого товара нет в магазине.")
                    continue
                if qty == 0:
                    print("Количество должно быть больше нуля.")
                    continue
                price = dungeon.prices[item]
                gold_total, ok = dungeon.buy(price, gold_total, quantity=qty)
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
            case "map":
                print("Карта:")
                for i in range(len(MAP)):
                    cells = []
                    for j in range(len(MAP[i])):
                        cell = "@" if (i, j) == (hero_r, hero_c) else MAP[i][j]
                        cells.append(cell)
                    print(" ".join(cells))
            case "scout":
                seen = set()
                print(f"Разведка: достижимых комнат — {scout(hero_r, hero_c, seen)}.")
            case "newgame":
                if os.path.exists("save.json"):
                    os.remove("save.json")
                    print("Сохранение удалено. Следующий забег начнётся с нуля.")
                else:
                    print("Нет сохранения, которое можно удалить.")
                save_enabled = False
                continue
            case "exit":
                print("Вы идете к двери. Лаборатория остается позади.")
                if save_enabled:
                    write_save()
                    print("Прогресс сохранён.")
                outcome = "выход"
                running = False
            case "help":
                print("Команды: " + ", ".join(commands) + ".")
                print("Номера 0-13 работают как раньше.")
            case _:
                print(f"Команды: '{line.strip()}' нет. Введите 'help'.")
                continue
        print()
        state = f"Здоровье: {health} Запас сил: {stamina:.1f} Врагов осталось: {len(enemies)} Золото: {gold_total}"
        if COLOR:
            print(Fore.GREEN + state + Style.RESET_ALL)
        else:
            print(state)
        if running:
            actions += 1
        if health <= 0:
            outcome = "гибель"
            print(f"{hero_name} падает без сил. Лаборатория забирает нового исследователя.")
            if os.path.exists("save.json"):
                os.remove("save.json")
            running = False
except KeyboardInterrupt:
    print()
    print("Игрок прервал сеанс.")
    if save_enabled:
        write_save()

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