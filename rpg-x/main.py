import os
import random

# Импорты сущностей
from entities.player.player import PlayerEntity
from entities.base import BaseEntity
from entities.enemy import (
    BearEntity,
    DogEntity,
    GoblinEntity,
    RafikEntity,
    SkeletonEntity,
    SpiderEntity,
)

# Импорты предметов, инвентаря
from inventory.inventory import Inventory
from inventory.items import BaseItem, HealingPotion, ShieldRecoveryPotion
from inventory.items.quests import QuestKey

# Импорты локаций, квестов, NPC
from world.locations import BaseLocation, DarkForestLocation, MainTownLocation

# Импорт боевой системы
from battle.battle_system import Battle

# Импорт систеиы квестов
from world.quests.quest import Quest


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def main():
    # Создаем инвентарь
    player_inventory = Inventory()

    # Создаем игрока
    player = PlayerEntity(
        name="КириллЧудотворец", age=12, gender="М", inventory=player_inventory
    )

    # Создаем квестовый предмет
    quest_key = QuestKey()

    # Создаем базовый квест
    key_quest = Quest(
        qid=1,
        name="Найди ключ",
        description="Ключ от входа в город находится рядом с тобой",
        requirements={"has_item": quest_key},
        reward={
            "item": HealingPotion(
                name="Зелье восстановления",
                description="Отличное зелье для восстановления ХП",
                stackable=True,
                max_stack=10,
            )
        },
    )

    # Выдаем квест игроку
    player.quests.add_quest(key_quest)
    player.quests.activate(1)

    # Создаем локации
    forest = DarkForestLocation()  # TODO: поправить конструктор локации "Темный лес"
    town = MainTownLocation()

    locations = [forest, town]

    # Прикрепляем локацию к игроку
    player.current_location = locations[0]  # стартовая локация -> лес

    # Получим текущую локацию игрока для генерации
    loc = player.current_location

    # Главный цикл игры
    while player.health > 0:
        # Очищение экрана
        clear_screen()

        # КириллЧудотворец | 100/100
        print(f"🎄 {player.name} | ❤️ {player.health:.0f}/{player.max_health:.0f}")
        print("-" * 50)
        print("\n --- МЕНЮ ---")
        print("1. Осмотреть локацию")
        print("2. Осмотреть инвентарь")
        print("3. Атаковать врага")
        print("4. Телепорт")
        print("5. Выйти")

        choice = input("\n Ваш выбор: ").strip()

        # Обработка выбора пункта меню игроком
        match choice:
            case "1":
                loc.enter()
                print(f"\n 🌍 {loc.name}")
                print(f"Описание: {loc.description}")
                print("\n" + loc.display_loot() + "\n")  # отображение лута
                print("\n" + loc.display_enemies() + "\n")  # отображение врагов
                print("\n" + loc.display_npc() + "\n")  # отображение NPC на локации

                input("\n (Нажмите ENTER для продолжения...)")
            case "2":
                print(player.inventory.show())

                choice = input("Выберите предмет для использования: ")
                try:
                    player.inventory.use_item_by_index(int(choice) - 1, player)
                except Exception as exc:
                    print(f"Ошибка использования предмета: {exc}")

                input("\n (Нажмите ENTER для продолжения...)")
            case "3":
                if loc.current_enemies:
                    lines = [f"Враги на локации ({(len(loc.current_enemies))}): "]

                    for i, enemy in enumerate(loc.current_enemies, 1):
                        lines.append(f"{i}. {enemy.name} L:{enemy.level}")

                    print("\n".join(lines))

                    choice = input("Выберите врага, которого желаете атаковать: ")
                    try:
                        battle = Battle(player, loc.current_enemies[int(choice) - 1])
                        battle.start()
                    except Exception as exc:
                        print(f"Проблема: {exc}")

                    if loc.current_enemies[int(choice) - 1].health <= 0:
                        loc.current_enemies.pop(int(choice) - 1)

                    input("\n (Нажмите ENTER для продолжения...)")
                else:
                    print("НЕМА ВРАГОВ")
                    input("\n (Нажмите ENTER для продолжения...)")
            case "4":
                lines = [f"Доступные локации ({(len(locations))}): "]

                for i, loc in enumerate(locations, 1):
                    lines.append(f"{i}. {loc.name}")

                print("\n".join(lines))

                choice = input(
                    "Выберите локацию, в которую желаете телепортироваться: "
                )

                try:
                    player.current_location = locations[int(choice) - 1]
                except Exception as exc:
                    print(
                        f"Телепорт не удался! Попробуйте выбрать другую локацию. Ошибка: {exc}"
                    )

            case "5":
                exit()
            case _:
                print("Выберите верный пункт меню! (1-5)")


if __name__ == "__main__":
    main()
