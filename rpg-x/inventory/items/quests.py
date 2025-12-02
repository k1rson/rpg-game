from .base import BaseItem

from entities.base import BaseEntity


class QuestKey(BaseItem):
    def __init__(
        self,
        name: str = "Ключ",
        description: str = "Какой-то странный ключ",
        stackable: bool = False,
        max_stack: int = 1,
    ) -> None:
        super().__init__(name, description, stackable, max_stack)

    # РЕАЛИЗУЕМ МЕТОДЫ, КОТОРЫЕ ОБЯЗАНЫ БЫТЬ РЕАЛИЗОВАННЫМИ
    def use(self, entity: BaseEntity) -> bool:
        raise TypeError("Квестовый предмет использовать нельзя")

    # Метод, указывающий, может ли предмет быть ЭКИПИРОВАН
    def is_equippable(self) -> bool:
        return False

    # Метод, указывайющий, может ли предмет быть ИСПОЛЬЗОВАН
    def can_be_consumed(self) -> bool:
        return False
