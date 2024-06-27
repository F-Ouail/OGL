import pygame
from . import window, color

class Square(window.WindowObject):
    def __init__(self, color: color.Color = color.Color(255, 255, 255), x: int = 0,\
                 y: int = 0, width:int = 50, height:int = 50) -> None:
        super().__init__(color, x, y)
        self.object_string_name = "Square"
        self.resize(width, height)
    def centre(self) -> tuple[int, int]:
        return (self.width//2, self.height//2)
    def resize(self, width:int, height:int) -> None:
        self.width, self.height = width, height
    def surface(self):
        return pygame.Rect((self.x, self.y), (self.width, self.height))
    def draw(self, window:window.Window, *args) -> None:
        if type(self.color) != color.Color:
            self.color = color.Color(0, 0, 0)
        pygame.draw.rect(window.self, self.color.value(), self.surface())
class Circle(window.WindowObject):
    def __init__(self, color: color.Color = color.Color(255, 255, 255), x: int = 0,\
                 y: int = 0, radius:int = 50) -> None:
        super().__init__(color, x, y)
        self.object_string_name = "Circle"
        self.radius = radius
        self.resize(radius, radius)
    def centre(self) -> tuple[int, int]:
        return (self.x, self.y)
    def resize(self, radius:int, *args) -> None:
        self.radius = radius
    def surface(self) -> pygame.surface.Surface | None:
        return None
    def draw(self, window:window.Window, *args) -> None:
        if type(self.color) != color.Color:
            self.color = color.Color(0, 0, 0)
        pygame.draw.circle(window.self, self.color.value(), self.centre(), self.radius)
class Image(window.WindowObject):
    def __init__(self, path:str = "", x: int = 0, y: int = 0) -> None:
        super().__init__(False, x, y)
        self.object_string_name = "Image"
        self.loaded = False
        self.path = path if not path is None else ""
        if self.path != "":
            self.reload()
    def reload(self, path:str|None = None) -> None:
        self.loaded = True
        self.image = pygame.image.load(self.path)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
    def rotate(self, dgr:int = 1) -> None:
        if self.loaded:
            self.image = pygame.transform.rotate(self.image, dgr)
    def resize(self, width:int = 0, height:int = 0):
        if self.loaded:
            self.width = width
            self.height = height
            self.image = pygame.transform.scale(self.image, (width, height))
    def draw(self, window:window.Window, *args) -> None:
        if self.loaded:
            window.self.blit(self.image, (self.x,self.y))
