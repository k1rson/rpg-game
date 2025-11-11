class BaseItem:
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
        self, name: str, description: str, stackable: bool, max_stack: int
    ) -> None:
        if not name:
            raise ValueError("Название предмета не может быть пустым!")
        if max_stack <= 0:
            raise ValueError("Максимальный стак не может быть меньше 0!")

        # Основные атрибуты
        self.name = name
        self.description = description
        self.stackable = stackable
        self.max_stack = max_stack

    def __str__(self) -> str:
        pass
