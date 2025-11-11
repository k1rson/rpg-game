from entities.player.player import PlayerEntity
from inventory.inventory import Inventory
from inventory.items.potions import HealingPotion


healign_potion = HealingPotion(
    "Зелье варенье", "Чудодейственное зелье Рафика", True, 10
)

inventory_player = Inventory()
player = PlayerEntity(
    name="Oleg", age=12, gender="M", inventory=inventory_player, health=80
)

player.inventory.add_item(healign_potion)
player.inventory.add_item(healign_potion)

print(player.inventory.show())
print(player.inventory.use_item_by_index(0, player))
