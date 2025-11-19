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

# Импорты локаций, квестов, NPC
from world.locations import BaseLocation, DarkForestLocation


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def battle(player: PlayerEntity, enemy: BaseEntity):
    print(f"БОЙ: {player.name} vs {enemy.name}")

    print("-" * 50)
    input("Нажмите ENTER, чтобы начать легендарный бой")

    while player.health > 0 and enemy.health > 0:
        dmg = player.deal_damage()
        enemy.take_damage(dmg)

        print(f"💀 {player.name} нанес {dmg} урона!")
        if enemy.health <= 0:
            print(f"{enemy.name} пал в бою! Естестественно!")
            player.inventory.add_item(
                HealingPotion(
                    name="Зелье гиганта Рафика",
                    description="Оля-ля-ля",
                    stackable=True,
                    max_stack=10,
                )
            )
            break

        dmg = enemy.deal_damage()
        player.take_damage(dmg)
        print(f"{enemy.name} нанес нам {dmg} урона!")

        input("Нажмите ENTER, для продолжения легендарного боя")

    input("Бой окончен! Нажмите ENTER, чтобы продолжить игру")


def main():
    # Создаем инвентарь
    player_inventory = Inventory()

    # Создаем игрока
    player = PlayerEntity(
        name="КириллЧудотворец", age=12, gender="М", inventory=player_inventory
    )

    # Создаем локации
    forest = DarkForestLocation()  # TODO: поправить конструктор локации "Темный лес"

    # Прикрепляем локацию к игроку
    player.current_location = forest

    # Получим текущую локацию игрока для генерации
    loc = player.current_location
    loc.enter()

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
        print("4. Выйти")

        choice = int(input("\n Ваш выбор: ").strip())

        # Обработка выбора пункта меню игроком
        match choice:
            case 1:
                print(f"\n 🌍 {loc.name}")
                print(f"Описание: {loc.description}")
                print("\n" + loc.display_loot() + "\n")  # отображение лута
                print(
                    "\n" + loc.display_enemies() + "\n"
                )  # отображение врагов на локации

                input("\n (Нажмите ENTER для продолжения...)")
            case 2:
                pass
            case 3:
                if loc.current_enemies:
                    battle(player, loc.current_enemies[0])
                    if loc.current_enemies[0].health <= 0:
                        loc.current_enemies.pop(0)
                else:
                    print("НЕМА ВРАГОВ")
                    input("\n (Нажмите ENTER для продолжения...)")
            case 4:
                pass
            case _:
                print("Выберите верный пункт меню! (1-4)")


if __name__ == "__main__":
    main()
