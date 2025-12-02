from typing import Optional

from ..base import BaseEntity
from inventory.inventory import Inventory
from world.locations.base import BaseLocation
from world.quests.quest_system import QuestSystem


class PlayerEntity(BaseEntity):
    def __init__(
        self,
        name: str,
        age: int,
        gender: str,
        entity_type: str = "Player",
        level: int = 1,
        health: float = 100.0,
        shield: float = 10.0,
        max_health: float = 100.0,
        max_shield: float = 100.0,
        attack: float = 10.0,
        crit_chance: float = 0.2,
        crit_multiplier: float = 2.0,
        inventory: Optional[Inventory] = None,
    ) -> None:
        super().__init__(
            name,
            age,
            gender,
            entity_type,
            level,
            health,
            shield,
            max_shield,
            max_health,
            attack,
            crit_chance,
            crit_multiplier,
        )

        # Инициализация инвентаря
        self.inventory: Optional[Inventory] = inventory

        # Инициализация локации
        self.current_location: Optional[BaseLocation] = None

        # Инициализация системы квестов персонажа
        self.quests = QuestSystem()
