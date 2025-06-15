import pygame
from . import window, color, animation, ui, basic


class Scene(window.WindowObject):
    def __init__(
        self,
        _window: window.Window,
        name: str,
        background: color.Color | tuple[int, int, int] | None = None,
        background_image: animation.AnimatedObject | None = None,
    ) -> None:
        self.linked_objects: list[tuple[window.WindowObject, bool, bool]] = []
        self.object_string_name = "Scene"
        self.name = name
        self.window = _window
        self.should_draw: bool = False
        self.most_priority: list[window.WindowObject] = []
        if background is None:
            self.background = color.Color(0, 0, 0)
        elif type(background) is tuple:
            if len(background) != 3:
                raise TypeError(f"The background Color is not tuple[int, int, int]")
            if not (
                type(background[0]) == type(background[1]) == type(background[2]) == int
            ):
                raise TypeError(
                    f"The background Color is not tuple[{type(background[0])}, {type(background[1])}, {type(background[2])}]"
                )
            self.background = color.Color(background[0], background[1], background[2])
        elif type(background) is color.Color:
            self.background = background
        else:
            raise TypeError(
                "The background type is one of Color,"
                + "None, tuple[int, int, int]."
                + f"The Entred type is {type(background)}"
            )
        _window.append(self)
        self.save = ()

    def input_to_update(self, *args) -> None:
        self.save = args
        return

    def append_most_priority_object(self, object: window.WindowObject) -> None:
        self.most_priority.append(object)

    def set_should_draw(self, should_draw: bool) -> None:
        if not self.should_draw is should_draw and should_draw:
            self.re_init()
        self.should_draw = should_draw

    def get_should_draw(self) -> bool:
        return self.should_draw

    def append_object(
        self,
        obj: window.WindowObject,
        centred_horizontally: bool = False,
        centred_vertically: bool = False,
    ) -> None:
        obj._mouse = window.mouse.pos
        self.linked_objects.append((obj, centred_horizontally, centred_vertically))
        self.reset()

    def reset(self) -> None:
        for p in self.most_priority:
            self.linked_objects.remove(p)  # type: ignore
            self.linked_objects.append(p)  # type: ignore

    def draw(self) -> None:
        if self.window.running is False:
            return
        if self.should_draw:
            self.window.fill(self.background.value())
            self.reset()
            self.update(self, self.save)  # type: ignore
            for obj, x_centre_flag, y_centre_flag in self.linked_objects:
                if x_centre_flag:
                    if type(obj) in [basic.Square, ui.Button, ui.Edit]:
                        obj.x = (self.window.width - obj.width) // 2
                    if type(obj) == ui.Label:
                        surface = obj.surface()
                        if surface is None:
                            continue
                        width = surface.get_width()
                        obj.x = (self.window.width - width) // 2
                if y_centre_flag:
                    if type(obj) in [basic.Square, ui.Button]:
                        obj.y = (self.window.height - obj.height) // 2
                    if type(obj) == ui.Label:
                        surface = obj.surface()
                        if surface is None:
                            continue
                        height = surface.get_height()
                        obj.y = (self.window.height - height) // 2
                obj.draw(self.window)

    def re_init(*args) -> None:
        return

    def update(*args) -> None:
        return
