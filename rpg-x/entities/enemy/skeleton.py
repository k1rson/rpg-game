from base import BaseEntity


class SkeletonEntity(BaseEntity):
    def __init__(
        self,
        name,
        age,
        gender,
        entity_type="Enemy",
        level=1,
        health=20,
        shield=0,
        max_shield=0,
        max_health=20,
        attack=5,
        crit_chance=0.2,
        crit_multiplier=1,
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
