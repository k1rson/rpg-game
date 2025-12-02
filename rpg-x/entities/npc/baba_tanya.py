from ..base import BaseEntity


class BabaTanyaEntity(BaseEntity):
    def __init__(
        self,
        name="Баба Таня",
        age=1500,
        gender="Женский",
        entity_type="NPC",
        level=1500,
        health=50000,
        shield=50000,
        max_shield=1500000,
        max_health=5000000,
        attack=2500000,
        crit_chance=1,
        crit_multiplier=100,
    ):
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
