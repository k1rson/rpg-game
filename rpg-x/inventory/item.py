class Item:
    """
        Базовый класс для представления предметов в нашей игре
        
        Атрибуты:
            name (str) -> Название предмета
            description (str) -> Описание предмета
            quantity (int) -> количество экземпляров предмета (для стака предметов)
            max_stack (int) -> Максимальное количество предметов, которое можно сложить в один слот инвентаря
    """
    
    def __init__(
        self, 
        name: str, 
        description: str, 
        quantity: int, 
        max_stack: int
    ) -> None:
        if not name:
            raise ValueError("Название предмета не может быть пустым!")
        if quantity <= 0:
            raise ValueError("Количество предметов должно быть больше 0!")
        if max_stack <= 0:
            raise ValueError("Максимальный стак не может быть меньше 0!")
        
        # Основные атрибуты
        self.name = name
        self.description = description
        self.quantity = quantity
        self.max_stack = max_stack
        
    def __str__(self) -> str:
        # Возращает строковое представление предмета для вывода в консоль
        if self.quantity > 1:
            return f'{self.name} x{self.quantity}'
        return self.name
