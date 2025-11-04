from base import BaseEntity

class GoblinEntity(BaseEntity):
    def __init__(
        self, 
        name, 
        age, 
        gender, 
        entity_type, 
        level = 1, 
        health = 40, 
        shield = 40,
        max_shield = 40, 
        max_health = 40, 
        attack = 15, 
        crit_chance = 0.2, 
        crit_multiplier = 3
    ):
        super().__init__(name, age, gender, entity_type, level, health, shield, max_shield, max_health, attack, crit_chance, crit_multiplier)