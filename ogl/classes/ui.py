# -------------------- -------------------- -------------------- -------------


import pygame
from . import window, color, basic
import math

class Label(window.WindowObject):
    def __init__(self,
                 text:str = "Graphics Label",
                 color:color.Color|None = None,
                 text_font:str = "Corbel", text_size:int = 18,
                 x:int = 0,y:int = 0) -> None:
        super().__init__(color, x, y)
        self.object_string_name = "Label"
        self.text, self.text_size = text, text_size
        utfont = None if text_font == "" else text_font
        self.font = pygame.font.SysFont(utfont, text_size)


    def surface(self) -> pygame.Surface | None:
        if type(self.color) != color.Color:
            return None
        return self.font.render(self.text, True, self.color.value())


    def is_mouse_on(self) -> bool:
        return super().is_mouse_on()


    def draw(self, window:window.Window, *args):
        surface = self.surface()
        if surface == None:
            return None
        window.self.blit(surface, (self.x, self.y))


class Button(window.WindowObject):
    def __init__(self,
                 text:str = "Button",
                 x:int = 0, y:int = 0,
                 w:int = 140, h:int = 50,
                 color:color.Color = color.Color(200,200,200),
                 label_color:color.Color|None = None,
                 label_font:str = "Corbel", label_size:int = 18) -> None:
        super().__init__(color, x, y)
        self.object_string_name = "Button"
        self.height = h
        self.width = w
        self.rect = basic.Square(color, x, y, w, h)
        self.label = Label(text, label_color, label_font, label_size)


    def is_mouse_on(self) -> bool:
        return self.rect.is_mouse_on()


    def resize(self, w:int, h:int):
        self.rect.width = w
        self.rect.height = h


    def draw(self, window:window.Window, *args) -> None:
        if type(self.color) != color.Color:
            return None
        self.rect._mouse = self._mouse
        if self.is_mouse_on():
            self.rect.color = self.color.shift()
        surface = self.label.surface()
        if surface is None:
            return None
        self.label.x = self.x + (self.width - surface.get_width()) // 2
        self.label.y = self.y + (self.height - surface.get_height()) // 2
        self.rect.x = self.x
        self.rect.y = self.y
        self.rect.width = self.width
        self.rect.height = self.height

        self.rect.draw(window)
        self.label.draw(window)


class RadioButton(window.WindowObject):
    def __init__(self, text:str = "RadioButton",
                 x:int = 0, y:int = 0,
                 label_color:color.Color|None = None,
                 label_font:str = "Corbel",
                 label_size:int = 18,
                 radius:int = 16) -> None:
        super().__init__(color.Color(238, 238, 238), x, y)
        self.object_string_name = "RadioButton"
        self.valide = False
        self.raduis = radius
        self.circle = basic.Circle(self.color, x, y , radius)
        self.min_circle = basic.Circle(x = x, y = y, radius = round(radius/3, 0))
        self.label = Label(text, label_color, label_font, label_size)


    def is_mouse_on(self) -> bool:
        return self.circle.is_mouse_on() or self.label.is_mouse_on()


    def draw(self, window:window.Window, *args) -> None:
        if type(self.color) != color.Color:
            return None
        if self.valide:
            used_color = color.Color(33, 150, 243)
        else:
            used_color = self.color.shift() if self.is_mouse_on() else self.color
        surface = self.label.surface()
        if surface is None:
            return None
        h, w = surface.get_height(), surface.get_width()
        self.label.x = self.circle.radius + self.circle.x + 10
        self.label.y = self.circle.y - h / 2
        self.circle.color = used_color
        self.circle.draw(window)
        if self.valide:
            self.min_circle.draw(window)
        self.label.draw(window)

## NEW under test

class Edit(Button):
    # def __init__(self):
    #     self.padding_x = 0
    #     self.padding_y = 0

    #     x = 0
    #     y = 0
    #     w = 0
    #     h = 0


    def __init__(self,
                 text:str = "Edit",
                 x:int = 0, y:int = 0,
                 w:int = 140, h:int = 50,
                 pad_x:int = 10, pad_y:int = 2,
                 max_text_length:int = 15,
                 color:color.Color = color.Color(200,200,200),
                 label_color:color.Color|None = None,
                 label_font:str = "Corbel",label_size:int = 18) -> None:
        super().__init__(text, x, y, w, h, color, label_color, label_font, label_size)
        self.object_string_name = "Edit"
        self.max_text_length = max_text_length
        self.padding_x = pad_x
        self.padding_y = pad_y
        self.var_text = ""
    def user_input(self, key):
        if key == pygame.K_BACKSPACE:
            self.var_text = self.var_text[:-1]
        else:
            self.var_text += chr(key)
    def draw(self, window:window.Window, *args) -> None:
        if type(self.color) != color.Color:
            return None
        self.rect._mouse = self._mouse
        self.rect.color = self.color.shift() if self.is_mouse_on() else self.color


        surface = self.label.surface()
        if surface is None:
            return None
        self.label.x = self.x + self.padding_x
        self.label.y = self.y + (self.height - surface.get_height()) // 2
        self.rect.x = self.x
        self.rect.y = self.y
        self.rect.width = self.width
        self.rect.height = self.height

        self.rect.draw(window)
        self.label.draw(window)



