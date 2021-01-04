from entities.entity import Entity
from entities.items import WoodItem
from entities.items import StoneItem

import timeit

class Block(Entity):
    """
    Abstract class for all breakable
    """

    def __init__(self, x, y, width, height, color:list, health, time_btw_damage):
        super().__init__(x, y, width, height, color)
        self.health = health
        self.minus_color = 50
        self.time_btw_damage = time_btw_damage
        self.time = timeit.default_timer()

    def get_damage(self, damage):
        """
        Gets damage for breaking this
        :param damage: int
        :return: None
        """
        if timeit.default_timer() - self.time >= self.time_btw_damage:
            self.time = timeit.default_timer()
            self.health -= damage
            for i in range(3):
                self.color[i] -= self.minus_color
                if self.color[i] < 0:
                    self.color[i] = 0
            if self.health <= 0:
                self.health = 0
                self.delete()
                self.break_up()

    def delete(self):
        """
        Delete from everywhere
        :return: None
        """
        Entity.entities.remove(self)

    def get_item_pos(self):
        return self.x + self.width / 2 - 10, self.y + self.height / 2 - 10, 10, 10

    def break_up(self):
        """
        Abstract method for creating item at the end of breaking
        :return: None
        """
        pass

class Wood(Block):
    item = WoodItem

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, [150, 75, 0], health=10, time_btw_damage=0.2)
        self.minus_color = 15

    def break_up(self):
        Wood.item(self.get_item_pos()[0], self.get_item_pos()[1], self.get_item_pos()[2], self.get_item_pos()[3])

    @staticmethod
    def to_str():
        return "wood"

    @staticmethod
    def set_item(item):
        Wood.item = item

class Stone(Block):
    item = StoneItem

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, [100, 100, 100], health=20, time_btw_damage=0.3)
        self.minus_color = 5

    def break_up(self):
        Stone.item(self.get_item_pos()[0], self.get_item_pos()[1], self.get_item_pos()[2], self.get_item_pos()[3])

    @staticmethod
    def to_str():
        return "stone"

    @staticmethod
    def set_item(item):
        Stone.item = item
