# Импорты сущностей и систем
from entities.player.player import PlayerEntity
from inventory.inventory import Inventory
from world.locations.dark_forest import DarkForestLocation


def main():
    location = DarkForestLocation()
    inventory = Inventory()

    player = PlayerEntity(name="Олег", age=12, gender="М", inventory=inventory)

    player.current_location = location

    # Главный цикл игры
    while player.health > 0:
        print(f"☹️  {player.name} | 💪 {player.health}/{player.max_health}")

        loc = player.current_location

        print("-" * 50)

        print("\n ------ Меню ------")
        print("1. Осмотреть локацию")
        print("2. Атаковать врага")
        print("3. Инвентарь")
        print("4. Использовать предмет из инвентаря")
        print("5. Подобрать лут")
        print("6. Выйти")

        choice = input("\n Ваш выбор:").strip()
        match choice:
            case "1":
                print(f"\n 👨🏼‍🦽 {loc.name}")
                print(f"{loc.description}")
                print("\n" + loc.display_loot())

                if loc.current_enemies:
                    print(
                        f"\n🧙🏼‍♂️ Враги: {', '.join(enemy.name for enemy in loc.current_enemies)}"
                    )
                else:
                    print("\n Врагов не видно!")
            case "2":
                pass
            case "3":
                print(player.inventory.show())
            case "4":
                pass
            case "5":
                pass
            case "6":
                pass
            case _:
                pass


if __name__ == "__main__":
    main()
