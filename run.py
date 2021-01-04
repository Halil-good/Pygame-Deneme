import pygame

if __name__ == "__main__":
    pygame.init()
    pygame.font.init()
    win = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption("2D Adventure Game")
    from game import Game
    g = Game(win)
    g.run()
