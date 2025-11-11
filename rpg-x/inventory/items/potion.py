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
                f"{entity.name} выпил зелье {self.name} и восстановил {self.heal_amount} HP"
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
