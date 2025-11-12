import random

from typing import Optional

from entities.base import BaseEntity
from inventory.items.base import BaseItem


class Location:
    def __init__(
        self,
        name: str,
        description: str,
        enemy_types: Optional[list[BaseEntity]],
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
