import random

from typing import Optional

from entities.base import BaseEntity
from entities.player.player import PlayerEntity

from inventory.items.potions import HealingPotion


class Battle:
    """
    Система пошагового боя
    """

    def __init__(self, player: PlayerEntity, enemy: BaseEntity) -> None:
        # Инициализация базовых свойств класса
        self.player = player
        self.enemy = enemy

        self.in_battle = True

    # Запуск цикла боя
    def start(self) -> None:
        print(f"БОЙ: {self.player.name} vs {self.enemy.name}")
        print("-" * 50)

        while self.in_battle:
            self._player_turn()

            if self.enemy.health <= 0:
                self._on_enemy_defeated()
                break

            self._enemy_turn()
            if self.player.health <= 0:
                self._on_player_defeated()
                break

        print("Бой завершен!!!")

    # Метод: ход игрока
    def _player_turn(self) -> None:
        print(
            f"\n♥️ {self.player.name}: {self.player.health:.0f}/{self.player.max_health:.0f}"
        )
        print(
            f"\n👽 {self.enemy.name}: {self.enemy.health:.0f}/{self.enemy.max_health:.0f}"
        )

        print("\n Ваш ход! Выберите действие: ")
        print("1. Атаковать")
        print("2. Инвентарь")
        print("3. Сбежать")

        while True:
            choice = input("Ваш выбор (1-3): ").strip()
            match choice:
                case "1":
                    self._player_attack()
                    break
                case "2":
                    # Просмотр инвентаря
                    pass
                case "3":
                    if self._try_flee():
                        self.in_battle = False
                        print("Вы успешно сбежали из боя!")
                        return
                    else:
                        print("Сбежать из боя не удалось!")
                        break
                case _:
                    print("Некорректный выбор действия! Выберите от 1 до 3")

    # Метод: ход врага
    def _enemy_turn(self) -> None:
        dmg = self.enemy.deal_damage()
        self.player.take_damage(dmg)

        print(f"💨 {self.enemy.name} наносит удар! Вы получили {dmg} урона!")

    # Атака персонажа
    def _player_attack(self) -> None:
        dmg = self.player.deal_damage()
        self.enemy.take_damage(dmg)

        print(f"💀 Вы нанесли {dmg} урона врагу: {self.enemy.name}!")

    # Попытка сбежать из боя
    def _try_flee(self) -> bool:
        return random.random() < 0.4

    # Поражение игрока
    def _on_player_defeated(self) -> None:
        print("\n Вы были повержены в бою...")

        # TODO: GameOver

    # Поражение врага
    def _on_enemy_defeated(self) -> None:
        print(f"\n  {self.enemy.name} повержен вами в бою!")

        healing_potion = HealingPotion(
            "Зелье здоровья", "Восстанавливает здоровье игрока", True, 10, 20
        )

        for _ in range(0, 5):
            self.player.inventory.add_item(healing_potion)
