from .base import BaseLocation

from entities.enemy.bear import BearEntity
from entities.enemy.spider import SpiderEntity
from entities.enemy.goblin import GoblinEntity

from inventory.items.potions import HealingPotion, ShieldRecoveryPotion


class DarkForestLocation(BaseLocation):
    def __init__(self) -> None:
        super().__init__(
            name="Темный лес",
            description="Густой, темный и зловещий лес... Где-то в кустах шуршит... Дядя Амаль",
            enemy_types=[BearEntity, SpiderEntity, GoblinEntity],
            enemy_spawn_chance=0.8,
            max_enemies=3,
            loot_table=[HealingPotion, ShieldRecoveryPotion],
            loot_spawn_chance=0.6,
            max_loot=2,
            respawn_time=3,
        )
