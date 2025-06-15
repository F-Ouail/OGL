import pygame
import signal
from . import color


class Mouse:
    _pos: tuple[int, int] = (0, 0)

    def pos(self) -> tuple[int, int]:
        return self._pos

    def update(self) -> None:
        self._pos = pygame.mouse.get_pos()


mouse = Mouse()


class Window:
    def __init__(
        self,
        title: str = "Graphics Window",
        width: int = 460,
        height: int = 460,
        resizability: bool = False,
        auto_event: bool = True,
        auto_draw: bool = False,
    ) -> None:
        """
        Settings
        --------
            Resizability
            ------------
            it is deactivated (set to False) by default.\n
            when it is activated the user becomes able\n
            to change the window size\n
            Auto draw
            ---------
            it is activated by default.\n
            when it is activated the window will automatically\n
            draw all graphics-objects linked to the window\n
            Auto Event
            ----------
            it is deactivated by default.\n
            to make the Window control it self diretly activate\n
                        the auto_event(is activate by default)\n
            event functions:\n
                funtionality      [there inputs]    : the time that it work in\n
                on_exit           []                : destroying the window\n
                on_reasize        [width, height]   : resizing the window\n
                on_key_down       [click key]       : a key pressed\n
                on_key_up         [click key]       : a key released\n
                on_every_frame    [fps value]       : on every frame\n
                keybored_hendler  [all keys statue] : on every frame\n

        """
        self.running = True
        self.clock = pygame.time.Clock()
        self.max_fps = None
        self.objs = []

        self.height = height
        self.width = width
        self.title = title
        self.auto_draw = auto_draw
        self.auto_event = auto_event
        self.size = (self.width, self.height)
        self.self = (
            pygame.display.set_mode(self.size, pygame.RESIZABLE)
            if resizability
            else pygame.display.set_mode(self.size)
        )

    def set_icon(self, image_or_path, use_image=False) -> None:
        if not self.running:
            return
        if use_image:
            pygame.display.set_icon(image_or_path)
        else:
            ico = pygame.image.load(image_or_path)
            pygame.display.set_icon(ico)

    def set_auto_draw(self, auto_draw: bool = False) -> None:
        if not self.running:
            return
        self.auto_draw = auto_draw

    def set_auto_event(self, auto_event: bool = True) -> None:
        if not self.running:
            return
        self.auto_event = auto_event

    def show(self) -> None:
        if not self.running:
            return
        mouse.update()
        pygame.display.set_caption(self.title)
        if self.auto_draw:
            for obj in self.objs:
                obj.draw()
        self.clock.tick(self.max_fps if not self.max_fps is None else 0)
        if self.auto_event:
            keys = pygame.key.get_pressed()
            self.keyboard_handler(keys)  # type: ignore
            for event in pygame.event.get():
                if not self.running:
                    return
                if event.type == pygame.QUIT:
                    self.destroy()
                    self.running = False
                elif event.type == pygame.VIDEOEXPOSE:
                    pygame.display.update()
                elif event.type == pygame.VIDEORESIZE:
                    self.height = event.dict["h"]
                    self.width = event.dict["w"]
                    self.on_reasize(event.dict["w"], event.dict["h"])
                elif event.type == pygame.KEYDOWN:
                    self.on_key_down(event.key)
                elif event.type == pygame.KEYUP:
                    self.on_key_up(event.key)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    self.mouse_handler(pos)
        self.on_every_frame(self.get_fps())
        if self.running:
            pygame.display.flip()

    def fill(self, color: tuple[int, int, int] = (0, 0, 0)) -> None:
        if self.running:
            self.self.fill(color)

    def ctrl_c(self, *args) -> None:
        if not self.running:
            return
        self.on_exit(args)
        self.destroy()

    def destroy(self) -> None:
        if not self.running:
            return
        self.running = False
        self.on_exit()
        pygame.display.quit()

    def get_centre(self) -> tuple[float, float]:
        return (int(self.width) // 2, int(self.height) // 2)

    def get_fps(self) -> float:
        value = self.clock.get_fps()
        return round(value if value != 0 else 1000, 2)

    def append(self, obj):
        self.objs.append(obj)

    def __str__(self) -> str:
        return f'<Window[title:"{self.title}"]>'

    @staticmethod
    def on_every_frame(fps: float):
        pass

    @staticmethod
    def on_exit(*args):
        pass

    @staticmethod
    def on_reasize(*args):
        pass

    @staticmethod
    def keyboard_handler(*args):
        pass

    @staticmethod
    def mouse_handler(pos: tuple[int, int], *args):
        pass

    @staticmethod
    def on_key_down(*args):
        pass

    @staticmethod
    def on_key_up(*args):
        pass


class WindowObject:
    def __init__(
        self, _color: color.Color | None | bool = None, x: int = 0, y: int = 0
    ) -> None:
        self.x: float = x
        self.y: float = y
        self.width: int = 0
        self.height: int = 0
        if _color != False:
            self.color = _color if _color is not None else color.Color(0, 0, 0)
        if type(self.color) != color.Color:
            self.color = color.Color(0, 0, 0)
        self.object_string_name = "Window Object"

    def is_mouse_on(self) -> bool:
        x, y = self._mouse()
        return (
            self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height
        )

    @staticmethod
    def _mouse() -> tuple[int, int]:
        return (-1, -1)

    def surface(self) -> pygame.Surface | None:
        return None

    def draw(self, window: Window) -> None:
        return

    def __str__(self) -> str:
        return f"<{self.object_string_name}>"
