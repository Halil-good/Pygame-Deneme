import pygame

class Entity:
    """
    Abstract class for all Entities
    """

    # static variables
    entities = []

    def __init__(self, x, y, width, height, color:list):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        Entity.entities.append(self)

    def update(self):
        """
        Abstract method for childrens of this class
        :return: None
        """
        pass

    def render(self, win):
        """
        Render this object on window
        :param win: pygame window
        :return: None
        """
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))

    def is_clicked(self):
        if pygame.mouse.get_pressed()[0]:
            x, y = pygame.mouse.get_pos()
            if self.x < x < self.x + self.width and self.y < y < self.y + self.height:
                return True
        return False

    @staticmethod
    def render_all(win):
        """
        Render all Entity object in our sceen
        :param win: pygame window
        :return: None
        """
        for entity in Entity.entities:
            entity.render(win)

    @staticmethod
    def update_all():
        """
        Update all Entities in our screen
        :return: None
        """
        for entity in Entity.entities:
            entity.update()

    @staticmethod
    def move_entities(x, y):
        """
        Move all entities with given position
        :param x: int
        :param y: int
        :return: None
        """
        for entity in Entity.entities:
            entity.x += x
            entity.y += y
