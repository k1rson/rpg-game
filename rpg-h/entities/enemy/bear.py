from base import BaseEntity

class BearEntity(BaseEntity):
    def __init__(
        self, 
        name, 
        age,
        gender,
        entity_type = 'Enemy', 
        level = 15, 
        health = 500, 
        shield = 50, 
        max_shield = 150, 
        max_health = 500, 
        attack = 25,
        crit_chance = 0.2, 
        crit_multiplier = 1.5
    ):
        super().__init__(name, age, gender, entity_type, level, health, shield, max_shield, max_health, attack, crit_chance, crit_multiplier)