from .quest import Quest


class QuestSystem:
    def __init__(self) -> None:
        self.quests = {}  # key: class Quest instance

    def add_quest(self, quest: Quest):
        self.quests[quest.id] = quest

    def activate(self, quest_id: int):
        if quest_id in self.quests:
            self.quests[quest_id].active = True

    def update(self, player):
        for quest in self.quests.values():
            if quest.active and not quest.completed:
                if quest.can_complete(player):
                    quest.complete(player)
                    print(f"Квест: {quest.name} завершен!")
