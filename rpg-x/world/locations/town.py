import random

from .base import BaseLocation

from entities.npc.baba_tanya import BabaTanyaEntity


class MainTownLocation(BaseLocation):
    def __init__(self) -> None:
        super().__init__(
            name="Химки",
            description="Увлекательное место, где проживают добрые НПС",
            enemy_types=[],
            npc_types=[BabaTanyaEntity],
            enemy_spawn_chance=0.8,
            max_enemies=3,
            loot_table=[],
            loot_spawn_chance=0.6,
            max_loot=2,
            respawn_time=3,
        )

    def _generate_content(self) -> None:
        self.current_npc = []

        baba_tanya = BabaTanyaEntity()

        self.current_npc.append(baba_tanya)
