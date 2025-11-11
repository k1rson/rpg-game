from entities.base import BaseEntity
from .base import BaseItem


class HealingPotion(BaseItem):
    def __init__(
        self,
        name: str,
        description: str,
        stackable: bool,
        max_stack: int,
        heal_amount: float = 10,  # сколько ХП восстанавливает
    ) -> None:
        super().__init__(name, description, stackable, max_stack)

        # Инициализируем базовые атрибуты
        self.heal_amount = heal_amount

    # РЕАЛИЗУЕМ МЕТОДЫ, КОТОРЫЕ ОБЯЗАНЫ БЫТЬ РЕАЛИЗОВАННЫМИ
    def use(self, entity: BaseEntity) -> bool:
        # если ХП меньше максимального, то будем восстанавливать ХП
        if entity.health < entity.max_health:
            entity.heal(amount=self.heal_amount)
            print(
                f"{entity.name} выпил {self.name} и восстановил здоровье на {self.heal_amount}. Текущее значение: {entity.health}"
            )
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
