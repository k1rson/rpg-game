from ..base import BaseEntity


class RafikEntity(BaseEntity):
    def __init__(
        self,
        name: str,
        age: int,
        gender: str,
        entity_type: str,
        level: int = 1,
        health: float = 300,
        shield: float = 150,
        max_shield: float = 300,
        max_health: float = 300,
        attack: float = 35,
        crit_chance: float = 0.3,
        crit_multiplier: float = 3,
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
