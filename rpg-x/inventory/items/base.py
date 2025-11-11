from abc import ABC

from entities.base import BaseEntity


class BaseItem(ABC):
    """
    Базовый класс для представления предметов в нашей игре (абстрактный, наследуемый)

    Атрибуты:
        name (str) -> Название предмета
        description (str) -> Описание предмета
        stackable (bool) -> Можно ли стакать предмет
        max_stack (int) -> Максимальное количество предметов, которое можно сложить в один слот инвентаря

    Методы:
        __init__ -> Конструктор класса
        __str__ -> Для красивого вывода в консоль
        use(self, entity: BaseEntity) -> bool: виртуальный метод (реализуется в подклассах): отвечает за использование предмета
        is_equippable(self) -> bool: виртуальный метод (реализуется в подклассах): можно ли надеть/вооружиться
        can_be_consumed(self) - bool: виртуальный метод (реализуется в подклассах): можно ли использовать предмет, как расходник
    """

    def __init__(
        self,
        name: str,
        description: str,
        stackable: bool,
        max_stack: int = 10,
        quantity: int = 1,
    ) -> None:
        if not name:
            raise ValueError("Название предмета не может быть пустым!")
        if max_stack <= 0:
            raise ValueError("Максимальный стак не может быть меньше либо равен 0!")
        if quantity <= 0:
            raise ValueError("Количество предмета не может быть меньше либо равно 0!")

        # Основные атрибуты
        self.name = name
        self.description = description
        self.stackable = stackable
        self.max_stack = max_stack
        self.quantity = quantity

    # Один из магических методов: позволяет красиво выводить объект в консоль
    def __str__(self) -> str:
        return f"Item (name: {self.name}, stackable: {self.stackable}, max_stack: {self.max_stack})"

    # Указываем, какие методы мы ОБЯЗАНЫ реализовать в классах наследниках
    def use(self, entity: BaseEntity) -> bool:
        raise NotImplementedError(
            "Метод use() обязан быть реализован в классе наследнике"
        )

    def is_equippable(self) -> bool:
        raise NotImplementedError(
            "Метод is_equippable() обязан быть реализован в классе наследнике"
        )

    def can_be_consumed(self) -> bool:
        raise NotImplementedError(
            "Метод can_be_consumed() обязан быть реализован в классе наследнике"
        )
