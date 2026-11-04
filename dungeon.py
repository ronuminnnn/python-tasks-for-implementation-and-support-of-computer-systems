"""Правила игры «Школьная лаборатория»: бой, цены, карточки врагов."""
import random
prices = {"Зелье": 10, "Споры": 15, "Жидкий уран": 40}
enemy_stats = {
    "химичка": {"hp": 45, "damage": 6, "loot": 25},
    "биологичка": {"hp": 30, "damage": 4, "loot": 15},
    "олимпиадник": {"hp": 20, "damage": 3, "loot": 10},
    "сирота": {"hp": 12, "damage": 2, "loot": 5},
}


def hero_hit(strike_n, damage, crit_damage):
    """Урон героя в удар strike_n; возвращает пару (hit, crit)."""
    if strike_n % 3 == 0:
        return crit_damage, True
    return damage, False


def fight(enemy, hero_health, bonus, damage, crit_damage):
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
        hit, crit = hero_hit(round_n, damage, crit_damage)
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


if __name__ == "__main__":
    rounds, won, hp, loot = fight("химичка", 100, 0, 20.5, 41.0)
    print(f"self-test: {len(rounds)} rounds, won={won}, loot={loot}")