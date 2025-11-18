import random

from abc import ABC

from effects.effect import BaseEffect


class BaseEntity(ABC):
    # Конструктор класса, вызывается ВСЕГДА при создании НОВОГО объекта
    def __init__(
        self,
        name: str,
        age: int,
        gender: str,
        entity_type: str,  # тип сущности -> игрок, враг, безобидный
        level: int = 1,  # уровень сущности
        health: float = 100.0,
        shield: float = 10.0,
        max_shield: float = 100.0,
        max_health: float = 100.0,  # максимальное значение здоровья
        attack: float = 10.0,  # сила атаки -> сколько ХП снимается от удара
        crit_chance: float = 0.2,  # шанс нанести крит удар
        crit_multiplier: float = 2.0,  # множитель урона
    ) -> None:
        # Основные атрибуты
        self.name: str = name
        self.age: int = age
        self.gender: str = gender
        self.entity_type: str = entity_type
        self.level: int = level

        # Основные характеристики
        self.max_health: float = max_health
        self.max_shield: float = max_shield

        self.health: float = min(health, max_health)
        self.shield: float = min(shield, max_shield)

        self.attack: float = attack
        self.crit_chance: float = crit_chance
        self.crit_multiplier: float = crit_multiplier

        # Система эффектов
        self.active_effects: list[BaseEffect] = []

    # Получение урона с учетом щита
    def take_damage(self, damage: float) -> None:
        if damage <= 0:  # пропускаем логику, если урона не было или он отрицательный
            return

        if self.shield > 0:
            if damage <= self.shield:  # если дамаг меньше значения щита
                self.shield -= damage
            else:  # если все же дамага больше чем щита
                damage -= self.shield
                self.shield = 0

        self.health = max(0, self.health - damage)

    # Просчет наносимого урона
    def deal_damage(self) -> float:
        base_damage = self.attack

        if (
            self._roll_crit()
        ):  # если шанс крита прокнул, то мы наносим урон с учетом crit_multiplier
            return base_damage * self.crit_multiplier

        return base_damage

    # Восстановление здоровья (принудительное восстановление)
    def heal(self, amount: float) -> None:
        self.health = min(self.max_health, self.health + amount)

    # Восстановление щита (принудительное восстановление)
    def restore_shield(self, amount: float) -> None:
        self.shield = min(self.max_shield, self.shield + amount)

    # Добавление эффекта к сущности
    def add_effect(self, effect: BaseEffect) -> None:
        # Удаление эффекта по имени
        self.remove_effect_by_name(effect.name)

        # Применение эффекта (единожды)
        effect.on_apply(self)
        self.active_effects.append(effect)  # добавляем эффект к активным

        print(f"{self.name} получил эффект: {effect.name}!")

    # Удаление эффекта по имени
    def remove_effect_by_name(self, name: str) -> None:
        for effect in self.active_effects:
            if effect.name == name:
                effect.on_remove(self)
                self.active_effects.remove(effect)

    # Обновление всех эффектов
    def tick_effects(self) -> None:
        for effect in self.active_effects:
            effect.duration -= 1
            effect.on_tick(self)

            if effect.duration <= 0:
                effect.on_remove(self)
                self.active_effects.remove(effect)

    # Внутренний метод: проверка на возможность нанести критический удар
    def _roll_crit(self) -> bool:  # True/False
        return random.random() < self.crit_chance
