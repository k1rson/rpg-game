from entities.player.player import PlayerEntity


class Quest:
    def __init__(
        self, qid: int, name: str, description: str, requirements: dict, reward: dict
    ) -> None:
        # Инициализация базовых атрибутов класса
        self.id = qid  # уникальный ID квеста
        self.name = name  # название квеста
        self.description = description  # описание квеста
        self.requirements = requirements  # требования к выполнению -> dict: {"has_item": "Ключ", "visited": "Город"}
        self.reward = reward  # награда за квест -> dict: {"item": Item}

    # Методы классса (поведение класса)
    # Проверяет, выполнен ли квест
    def can_complete(self, player: PlayerEntity):
        pass

    # Выполнить квест -> выдать награду
    def complete(self, player: PlayerEntity):
        pass
