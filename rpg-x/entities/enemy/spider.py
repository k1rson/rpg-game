import random

from base import BaseEntity

class SpiderEntity(BaseEntity):
    def __init__(
        self, 
        name: str, 
        age: int, 
        gender: str, 
        entity_type: str = 'Enemy', 
        level: int = 1, 
        health: float = 50.0, 
        shield: float = 15.0, 
        max_shield: float = 60.0, 
        attack: float = 20.0, 
        crit_chance: float = 0.2, # 20%
        crit_multiplier: float = 1.5,
        poison_chance: float = 0.3, # 30%
        poison_damage: float = 15.0 # x2
    ) -> None:
        super().__init__(name, age, gender, entity_type, level, health, shield, max_shield, attack, crit_chance, crit_multiplier)
        
        # Базовые характеристики отравления
        self.poison_chance = poison_chance
        self.poison_damage = poison_damage
        
        # Базовые характеристики кокона
        self.is_active_cocoon = False
        
    # Просчет урона, наносимого пауком
    def deal_damage(self) -> float:
        base_damage = super().deal_damage()
        
        if self._roll_poison_crit(): # если True, то можем нанести урон от яда
            return base_damage + self.poison_damage
        
        return base_damage
        
    # Получение урона (дополненная логика с коконом)
    def take_damage(self, damage: float) -> None:
        if not self.is_active_cocoon and self.health < 20: # два условия должны сойтись: кокон не должен быть активирован и ХП должно быть меньше 20
            self.is_active_cocoon = True
            return  # урон НЕ наносится

        super().take_damage(damage)
            
    # Внутренний метод: просчитывает возможность нанести урон от яда
    def _roll_poison_crit(self) -> bool:
        return random.random() < self.poison_chance