import random

from typing import Optional, Type

from entities.base import BaseEntity
from inventory.items.base import BaseItem


class BaseLocation:
    def __init__(
        self,
        name: str,
        description: str,
        enemy_types: Optional[list[Type[BaseEntity]]],
        enemy_spawn_chance: float = 0.7,
        max_enemies: int = 3,
        loot_table: Optional[list[BaseItem]] = None,
        loot_spawn_chance: float = 0.5,
        respawn_time: int = 3,  # через сколько будет респавниваться локация (0 - никогда)
    ) -> None:
        # Базовая информация о локации
        self.name = name
        self.description = description

        # Враги
        self.enemy_types = enemy_types
        self.enemy_spawn_chance = enemy_spawn_chance
        self.max_enemies = max_enemies

        # Лут
        self.loot_table = loot_table
        self.loot_spawn_chance = loot_spawn_chance

        # Респавн локации
        self.respawn_time = respawn_time
        self._visits_since_respawn = 0

        # Текущее состояние локации (данное состояние будет генерироваться перед каждым входом в локацию)
        self.current_enemies: list[BaseEntity] = []
        self.current_loot: list[BaseItem] = []

    # Внутренние методы класса
    # Метод отвечает за генерацию контента на локации (враги/лут)
    def _generate_content(self) -> None:
        self.current_enemies = []
        self.current_loot = []

        # Генерация врагов
        if self.enemy_types and random.random() < self.enemy_spawn_chance:
            num_enemies = random.randint(
                1, min(self.max_enemies, len(self.enemy_types))
            )

            for _ in range(num_enemies):
                enemy_class = random.choice(self.enemy_types)

                enemy = enemy_class()

    # Базовые методы (поведение каждой локации)
    # Вызывается при входе на локацию и генерирует контент
    def enter(self) -> None:
        pass

    # Метод, позволяющий подбирать предмет с локации по индексу
    def take_loot(self, index: int) -> Optional[BaseItem]:
        pass

    # Метод, позволяющий показать какой лут находится сейчас на локации
    def display_loot(self) -> str:
        pass
