import random

from base import BaseEntity


class DogEntity(BaseEntity):
    def __init__(
        self,
        name: str,
        age: int,
        gender: str,
        entity_type: str = "Enemy",
        level: int = 1,
        health: float = 20.0,
        shield: float = 0.0,
        max_shield: float = 5.0,
        max_health: float = 50.0,
        attack: float = 2.0,
        crit_chance: float = 0.4,
        crit_multiplier: float = 2,
        evasion_chance: float = 0.1,  # шанс уклониться от урона -> 10%
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

        # Дополнительные боевые способности
        self.evasion_chance = evasion_chance
        self.can_evasion = True

    # Переопределение метода получения урона (с учетом уклонения)
    def take_damage(self, damage):
        if self._roll_evasion_chance() and self.can_evasion:  # уклонились от удара
            self._toggle_evasion()  # сменили состояние
            return

        self._toggle_evasion()
        return super().take_damage(damage)

    # Внутренний метод: просчет возможности уклонения
    def _roll_evasion_chance(self) -> bool:
        return random.random() < self.evasion_chance

    # Внутренний метод: переключение состояния уклонения
    def _toggle_evasion(self) -> None:
        self.can_evasion = not self.can_evasion
