import pygame
import math
import timeit

from entities.entity import Entity
from entities.blocks import Block
from entities.blocks import Wood
from entities.blocks import Stone
from entities.items import Item
from entities.items import WoodItem
from entities.items import StoneItem
from ui.ui import Text

class Player(Entity):
    """
    Player class extends with Entity class
    """

    def __init__(self, win_width, win_height):
        super().__init__(win_width / 2 - 25, win_height / 2 - 25, 50, 50, [50, 50, 50])
        self.items = []
        self.selected_block_type = Wood
        self.item_texts = {
            "wood": Text('Comic Sans MS', 25, "Wood: 0"),
            "stone": Text('Comic Sans MS', 25, "Stone: 0", 0, 30)
        }
        self.put_block_delta_time = 0.2
        self.put_block_time = timeit.default_timer()
        self.go_right = True
        self.go_left = True
        self.go_up = True
        self.go_down = True
        self.vel = 2

    def update(self):
        """
        Player's update loop
        :return: None
        """
        self.check_collide()
        self.put_block()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            if self.go_up:
                self.y -= self.vel
                Entity.move_entities(0, self.vel)
        elif keys[pygame.K_s]:
            if self.go_down:
                self.y += self.vel
                Entity.move_entities(0, -self.vel)
        if keys[pygame.K_d]:
            if self.go_right:
                self.x += self.vel
                Entity.move_entities(-self.vel, 0)
        elif keys[pygame.K_a]:
            if self.go_left:
                self.x -= self.vel
                Entity.move_entities(self.vel, 0)

        for entity in Entity.entities:
            if isinstance(entity, Item):
                entity.pick(self)

            if isinstance(entity, Block):
                if entity.is_clicked():
                    if self.distance(entity) < 200:
                        entity.get_damage(2)

    def check_collide(self):
        """
        Checks collide and sets possibility of going specific dircetion
        :return: None
        """
        go_everywhere = True
        for entity in Entity.entities:
            if entity == self or isinstance(entity, Item):
                continue
            if self.x + self.width + self.vel > entity.x and self.x < entity.x + entity.width:
                if self.y + self.height > entity.y and self.y < entity.y + entity.height:
                    self.go_right = False
                    go_everywhere = False
            if self.x - self.vel < entity.x + entity.width and self.x > entity.x:
                if self.y + self.height > entity.y and self.y < entity.y + entity.height:
                    self.go_left = False
                    go_everywhere = False
            if self.y - self.vel < entity.y + entity.height and self.y > entity.y:
                if self.x + self.width > entity.x and self.x < entity.x + entity.width:
                    self.go_up = False
                    go_everywhere = False
            if self.y + self.height + self.vel > entity.y and self.y < entity.y + entity.height:
                if self.x + self.width > entity.x and self.x < entity.x + entity.width:
                    self.go_down = False
                    go_everywhere = False

        if go_everywhere:
            self.go_right = True
            self.go_left = True
            self.go_up = True
            self.go_down = True

    def put_block(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            self.selected_block_type = Wood
        elif keys[pygame.K_2]:
            self.selected_block_type = Stone

        for i, item_text in self.item_texts.items():
            item_text.set_background_color([255, 255, 255])
        self.item_texts[self.selected_block_type.to_str()].set_background_color([255, 0, 0])

        if pygame.mouse.get_pressed()[2]:
            for item in self.items:
                if isinstance(item, self.selected_block_type.item):
                    x, y = pygame.mouse.get_pos()
                    if self.distance_btw_point(x, y) < 200:
                        if timeit.default_timer() - self.put_block_time >= self.put_block_delta_time:
                            self.put_block_time = timeit.default_timer()
                            self.selected_block_type(x - 25, y - 25, 50, 50)
                            self.items.remove(item)
                            self.update_texts()
                            break

    def distance(self, entity):
        """
        Calculate distance btw entity and self
        :param entity: Entity
        :return: None
        """
        return math.sqrt((math.fabs((self.x + self.width / 2) - (entity.x + entity.width / 2)) ** 2)
                         + (math.fabs((self.y + self.height / 2) - (entity.y + entity.height / 2)) ** 2))

    def distance_btw_point(self, x, y):
        return math.sqrt((math.fabs((self.x + self.width / 2) - x) ** 2) + (math.fabs((self.y + self.height / 2) - y) ** 2))

    def collision(self, entity):
        """
        Return collision of entity and self
        :param entity: Entity
        :return: bool
        """
        return self.x < entity.x + entity.width and self.x + self.width > entity.x and self.y < entity.y + entity.height and self.y + self.height > entity.y

    def get_item(self, item):
        """
        Add item to players items
        :param item: Item
        :return: None
        """
        self.items.append(item)
        self.update_texts()

    def update_texts(self):
        wood_item = 0
        stone_item = 0
        for item in self.items:
            if isinstance(item, WoodItem):
                wood_item += 1
            elif isinstance(item, StoneItem):
                stone_item += 1
        self.item_texts["wood"].set_text(f"Wood: {wood_item}")
        self.item_texts["stone"].set_text(f"Stone: {stone_item}")
