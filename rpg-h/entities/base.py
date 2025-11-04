import random

from abc import ABC

class BaseEntity(ABC):
    # Конструктор класса, вызывается ВСЕГДА при создании НОВОГО объекта
    def __init__(
        self,
        name: str,
        age: int,
        gender: str,
        entity_type: str, # тип сущности -> игрок, враг, безобидный
        level: int = 1, # уровень сущности
        health: float = 100.0,
        shield: float = 10.0,
        max_shield: float = 100.0,
        max_health: float = 100.0, # максимальное значение здоровья
        attack: float = 10.0, # сила атаки -> сколько ХП снимается от удара
        crit_chance: float = 0.2, # шанс нанести крит удар
        crit_multiplier: float = 2.0, # множитель урона
    ) -> None:
        
        # Основные атрибуты
        self.name = name
        self.age = age
        self.gender = gender
        self.entity_type = entity_type
        self.level = level
        
        # Основные характеристики
        self.max_health = max_health
        self.max_shield = max_shield
        
        self.health = min(health, max_health)
        self.shield = min(shield, max_shield)
        
        self.attack = attack
        self.crit_chance = crit_chance
        self.crit_multiplier = crit_multiplier
        
    # Получение урона с учетом щита
    def take_damage(self, damage: float) -> None:
        if damage <= 0: # пропускаем логику, если урона не было или он отрицательный
            return
        
        if self.shield > 0:
            if damage <= self.shield: # если дамаг меньше значения щита
                self.shield -= damage
            else: # если все же дамага больше чем щита
                damage -= self.shield
                self.shield = 0
                
        self.health = max(0, self.health - damage)       
        
    # Просчет наносимого урона
    def deal_damage(self) -> float:
        base_damage = self.attack
        
        if self._roll_crit(): # если шанс крита прокнул, то мы наносим урон с учетом crit_multiplier
            return base_damage * self.crit_multiplier
        
        return base_damage
    
    # Восстановление здоровья (принудительное восстановление)
    def heal(self, amount: float) -> None:
        self.health = min(self.max_health, self.health + amount)
    
    # Восстановление щита (принудительное восстановление)
    def restore_shield(self, amount: float) -> None:
        self.shield = min(self.max_shield, self.shield + amount)
    
    # Внутренний метод: проверка на возможность нанести критический удар
    def _roll_crit(self) -> bool:
        return random.random() < self.crit_chance
        