import os
import random

# Импорты сущностей
from entities.player.player import PlayerEntity
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

    # Главный цикл игры
    while player.health > 0:
        # Очищение экрана
        # КОД

        # КириллЧудотворец | 100/100
        print(f"🎄 {player.name} | ❤️ {player.health}/{player.max_health}")
        print("-" * 50)
        print("\n --- МЕНЮ ---")
        print("1. Осмотреть локацию")
        print("2. Осмотреть инвентарь")
        print("3. Атаковать врага")
        print("4. Выйти")

        choice = int(input("\n Ваш выбор: ").strip())

        # Получим текущую локацию игрока для генерации
        loc = player.current_location
        loc.enter()

        # Обработка выбора пункта меню игроком
        match choice:
            case 1:
                print(f"\n 🌍 {loc.name}")
                print(f"Описание: {loc.description}")
                print("\n" + loc.display_loot())  # отображение лута
                print("\n" + loc.display_enemies())  # отображение врагов на локации
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case _:
                print("Выберите верный пункт меню! (1-4)")


if __name__ == "__main__":
    main()
