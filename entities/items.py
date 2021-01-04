from entities.entity import Entity


class Item(Entity):
    def __init__(self, x, y, width, height, color:list):
        super().__init__(x, y, width, height, color)
        self.parent = None

    def pick(self, player):
        if player.collision(self):
            player.get_item(self)
            Entity.entities.remove(self)

    def __str__(self):
        return "null item"

class WoodItem(Item):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, [150, 75, 0])


class StoneItem(Item):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, [100, 100, 100])
