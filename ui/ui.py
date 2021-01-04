import pygame

class Ui:
    all_ui = []

    def __init__(self):
        Ui.all_ui.append(self)

    def update(self):
        pass

    def render(self, win:pygame.Surface):
        pass

    @staticmethod
    def render_all(win:pygame.Surface):
        for ui in Ui.all_ui:
            ui.render(win)

    @staticmethod
    def update_all():
        for ui in Ui.all_ui:
            ui.update()

class Text(Ui):
    def __init__(self, font_name, font, text, x=0, y=0):
        super().__init__()
        self.x = x
        self.y = y
        self.text = text
        self.color = [255, 255, 255]
        self.font_name = font_name
        self.font_size = font
        self.font = pygame.font.SysFont(font_name, font)
        self.text_surfce = self.font.render(text, False, self.color)

    def set_font(self, font):
        self.font = pygame.font.SysFont(self.font_name, self.font_name)
        self.text_surfce = self.font.render(self.text, False, self.color)

    def set_text(self, text):
        self.text = text
        self.text_surfce = self.font.render(text, False, self.color)

    def set_background_color(self, color:list):
        self.color = color
        self.text_surfce = self.font.render(self.text, False, color)

    def set_pos(self, x, y):
        self.x = x
        self.y = y

    def render(self, win:pygame.Surface):
        win.blit(self.text_surfce, (self.x, self.y))

class Button(Ui):
    def __init__(self, x, y, width, height, text):
        super().__init__()
        self.x = x
        self.y = y
        self.func = None # funciton for on click
        self.width = width
        self.height = height
        self.pressed_color = [150, 150, 150]
        self.on_mouse_btn_color = [100, 100, 100]
        self.inactive_color = [50, 50, 50]
        self.color = self.inactive_color
        self.text = Text('Comic Sans MS', 30, text)
        self.text.set_pos(x + width / 2 - self.text.text_surfce.get_width() / 2, y + height / 2 - self.text.text_surfce.get_height() / 2)

    def set_pressed_color(self, color):
        self.pressed_color = color

    def set_on_mouse_btn_color(self, color):
        self.on_mouse_btn_color = color

    def set_inactive_color(self, color):
        self.inactive_color = color

    def set_on_click(self, fun):
        self.func = fun

    def update(self):
        x, y = pygame.mouse.get_pos()
        if self.x < x < self.x + self.width and self.y < y < self.y + self.height:
            if pygame.mouse.get_pressed()[0]:
                self.color = self.pressed_color
                self.func()
            else:
                self.color = self.on_mouse_btn_color
        else:
            self.color = self.inactive_color

    def render(self, win:pygame.Surface):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
