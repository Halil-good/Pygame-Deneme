import pygame

from entities.entity import Entity
from entities.player import Player
from entities.blocks import Wood
from entities.blocks import Stone
from ui.ui import Ui

class Game:
    """
    Main game class
    """
    def __init__(self, win: pygame.Surface):
        self.win = win
        self.win.get_height()
        self.win.get_width()
        self.background_color = (130, 100, 255)
        Wood(x=10, y=10, width=150, height=200)
        Wood(x=300, y=400, width=200, height=200)
        Wood(x=800, y=400, width=100, height=100)
        Stone(x=-200, y=-400, width=100, height=100)
        Player(win.get_width(), win.get_height())

    def run(self):
        """
        Runs the game
        :return: None
        """
        clock = pygame.time.Clock()
        run = True
        timer = 0
        while run:
            clock.tick(200)
            timer += 1
            if timer >= 1000:
                timer = 0
                print(clock.get_fps())

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            self.update()
            self.render()

        pygame.quit()

    def render(self):
        """
        Render all objects
        :return: None
        """
        self.win.fill(self.background_color)
        Entity.render_all(self.win)
        Ui.render_all(self.win)
        pygame.display.update()

    def update(self):
        Entity.update_all()
        Ui.update_all()
