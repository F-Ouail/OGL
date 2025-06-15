import pygame
from math import trunc
from . import window


class Animation:
    def __init__(self, period_with_frame: int) -> None:
        self.self_paths: list[str] = []
        self.time: int = period_with_frame
        self.count: float = 0

    def append_path(self, image_path: str) -> None:
        self.self_paths.append(image_path)

    def append_paths(self, *paths) -> None:
        for path in paths:
            if type(path) is str:
                self.self_paths.append(path)

    def lenght(self) -> int:
        return len(self.self_paths)

    def include(self) -> pygame.Surface:
        image = pygame.image.load(self.self_paths[trunc(self.count) % self.lenght()])
        self.count += 1 / self.time
        if self.count >= self.lenght():
            self.count = 0
        return image

    def __str__(self) -> str:
        return f"<Animation lenght:{self.lenght()} time:{self.time} frame>"


class SymmetricalAnimation(Animation):
    def __init__(self, period_with_frame: int) -> None:
        self.self_paths: list[str] = []
        self.time: int = period_with_frame
        self.count: float = 0

    def include(self) -> pygame.Surface:
        paths = self.self_paths + self.self_paths[::-1]
        image = pygame.image.load(paths[trunc(self.count) % self.lenght()])
        self.count += 1 / self.time
        if self.count >= self.lenght():
            self.count = 0
        return image

    def lenght(self) -> int:
        return super().lenght() * 2

    def __str__(self) -> str:
        return (
            f"<SymmetricalAnimation lenght:{self.lenght( * 2)} time:{self.time} frame>"
        )


class AnimatedObject(window.WindowObject):
    def __init__(
        self,
        animation: Animation | None,
        x: int = 0,
        y: int = 0,
        width: int = 50,
        height: int = 50,
    ) -> None:
        super().__init__(False, x, y)
        self.object_string_name = "Animated Object"
        self.animation = animation
        self.width = width
        self.height = height
        self.size = (self.width, self.height)

    def surface(self) -> pygame.Surface | None:
        if self.animation is None:
            return
        surface = self.animation.include()
        self.size = (self.width, self.height)
        surface = pygame.transform.scale(surface, self.size)
        return surface

    def draw(self, window: window.Window) -> None:
        if self.animation is not None:
            surface = self.surface()
            if surface is None:
                return
            window.self.blit(surface, (self.x, self.y))


class MultiAnimationsObject(AnimatedObject):
    def __init__(
        self,
        animations: list[Animation] = [],
        x: int = 0,
        y: int = 0,
        width: int = 50,
        height: int = 50,
    ) -> None:
        super().__init__(None, x, y, width, height)
        self.object_string_name = "Object"
        self.animations: list[Animation] = animations
        self.animation: Animation | None = None

    def set_animation(self, element: int | str) -> bool:
        if type(element) == int:
            if element > len(self.animations):
                return False
            self.animation = self.animations[element]
        elif type(element) == str:
            pass
        return False
