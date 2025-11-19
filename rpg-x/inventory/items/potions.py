import random

from entities.base import BaseEntity
from .base import BaseItem

from effects.applied_effects import HealOverTime, ShieldBuff


class HealingPotion(BaseItem):
    def __init__(
        self,
        name: str,
        description: str,
        stackable: bool,
        max_stack: int,
        heal_amount: float = 10,  # сколько ХП восстанавливает,
        chance_apply_effect: float = 0.2,
    ) -> None:
        super().__init__(name, description, stackable, max_stack)

        # Инициализируем базовые атрибуты
        self.heal_amount = heal_amount
        self.chance_apply_effect = chance_apply_effect

    # РЕАЛИЗУЕМ МЕТОДЫ, КОТОРЫЕ ОБЯЗАНЫ БЫТЬ РЕАЛИЗОВАННЫМИ
    def use(self, entity: BaseEntity) -> bool:
        # если ХП меньше максимального, то будем восстанавливать ХП
        if entity.health < entity.max_health:
            entity.heal(amount=self.heal_amount)
            print(
                f"{entity.name} выпил {self.name} и восстановил здоровье на {self.heal_amount}. Текущее значение: {entity.health}"
            )

            # с какой-то вероятностью накладываем эффект восстановления здоровья
            if random.random() < self.chance_apply_effect:
                buff = HealOverTime(
                    name="Снадобье великана Рафика",
                    description="Великий бафф великого Рафика для великого отхила",
                    duration=random.randint(1, 3),
                    heal_per_tern=random.randint(1, 30),
                )

                print(
                    f"Поздравляю! Вы выпили чудодейственное зелье, которое наложило на вас эффект ({buff.name})!"
                )
                entity.add_effect(buff)

            return True
        else:
            print("HP полны!")
            return False

    # Метод, указывающий, может ли предмет быть ЭКИПИРОВАН
    def is_equippable(self) -> bool:
        return False  # зелье не может быть экипировано

    # Метод, указывайющий, может ли предмет быть ИСПОЛЬЗОВАН
    def can_be_consumed(self) -> bool:
        return True  # зелье может быть использовано


class ShieldRecoveryPotion(BaseItem):
    def __init__(
        self,
        name: str,
        description: str,
        stackable: bool,
        max_stack: int,
        shield_recovery_amount: float = 10,
    ) -> None:
        super().__init__(name, description, stackable, max_stack)

        # Инициализация базовых атрибутов
        self.shield_recovery_amount = shield_recovery_amount

    def use(self, entity: BaseEntity) -> bool:
        if entity.shield < entity.max_shield:
            entity.restore_shield(amount=self.shield_recovery_amount)
            print(
                f"{entity.name} выпил {self.name} и восстановил щит на {self.shield_recovery_amount}. Текущее значение: {entity.shield}"
            )
            return True
        else:
            print("Щит полон!")
            return False

    def is_equippable(self) -> bool:
        return False

    def can_be_consumed(self) -> bool:
        return True
