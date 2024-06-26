import pygame
from . import window, color

class Label(window.WindowObject):
    def __init__(self, text:str = "Graphics Label",_color:color.Color|None = None,\
                 text_font:str = "Corbel", text_size:int = 18, x:int = 0,\
                 y:int = 0) -> None:
        super().__init__(_color, x, y)
        if type(self.color) != color.Color:
            return
        self.object_string_name = "Label"
        self.text = text
        self.tsize = text_size
        utfont = None if text_font == "" else text_font
        self.font = pygame.font.SysFont(utfont, text_size) # type: ignore
    def surface(self) -> pygame.Surface | None:
        if type(self.color) != color.Color:
            return None
        return self.font.render(self.text, True, self.color.value())
    def update(*args):
        return
    def draw(self, window:window.Window, *args):
        self.update(self)
        surface = self.surface()
        if surface == None:
            return None
        window.self.blit(surface, (self.x, self.y))
class Button(window.WindowObject):
    def __init__(self, text:str = "Button", x:int = 0, y:int = 0, w:int = 140,
                  h:int = 50, color:color.Color = color.Color(200,200,200),
                  label_color:color.Color|None = None, label_font:str = "Corbel",
                  label_size:int = 18) -> None:
        super().__init__(color, x, y)
        self.object_string_name = "Button"
        self.width = w
        self.height = h
        self.label = Label(text, label_color, label_font, label_size)
    def is_mouse_on(self) -> bool:
        mouse = self._mouse()
        return self.x <= mouse[0] <= self.x + self.width and self.y <= mouse[1] <= self.y + self.height
    def is_click(self) -> bool | None:
        if type(self.color) != color.Color:
            return None
        mouse = self._mouse()
        return self.x <= mouse[0] <= self.x + self.width and self.y <= mouse[1] <= self.y + self.height
    def draw(self, window:window.Window, *args) -> None:
        if type(self.color) != color.Color:
            return None
        used_color = self.color.Not().value() if self.is_mouse_on() else self.color.value()
        pygame.draw.rect(window.self, used_color,
                         pygame.Rect((self.x, self.y), (self.width, self.height)))
        surface = self.label.surface()
        if surface is None:
            return None
        h, w = surface.get_width(), surface.get_width()
        self.label.x = self.x+self.width / 2 - surface.get_width() / 2
        self.label.y = self.y+self.height / 2 - surface.get_height() / 2
        self.label.draw(window)
