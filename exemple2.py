import graphics

KeysMap = {
    "UP" : [
        graphics.pygame.K_UP,
        graphics.pygame.K_w,
        graphics.pygame.K_z, # for azerty keyboards
    ],
    "DOWN" : [
        graphics.pygame.K_DOWN,
        graphics.pygame.K_s,
    ],
    "RIGHT" : [
        graphics.pygame.K_RIGHT,
        graphics.pygame.K_d,
    ],
    "LEFT" : [
        graphics.pygame.K_LEFT,
        graphics.pygame.K_a,
        graphics.pygame.K_q, # for azerty keyboards
    ],
    "BREAK" : [
        graphics.pygame.K_ESCAPE,
    ],
    "RESET" : [
        graphics.pygame.K_F4,
    ]
}

def KeyMap(key:str, keys) -> bool:
    global KeysMap
    key = key.upper()
    if key not in KeysMap.keys():
        return False
    for _key in KeysMap[key]:
        if keys[_key]:
            return True
    return False
def MapedKey(key:str, value) -> bool:
    global KeysMap
    key = key.upper()
    if key not in KeysMap.keys():
        return False
    return value in KeysMap[key]

class Player(graphics.basic.Square):
    def __init__(self, pos:tuple[int, int], speed:int) -> None:
        super().__init__(graphics.color.Color(252, 226, 196), pos[0], pos[1], 
                         width = 50, height = 50)
        self.object_string_name = "Player"
        self.speed:int = speed
    def move(self, x:tuple[bool, bool], y:tuple[bool, bool], delta:float):
        _x = None if x[0] == x[1] else False if x[0] else True
        _y = None if y[0] == y[1] else False if y[0] else True
        self.x += self.speed * delta * (0 if _x is None else -1 if _x else 1)
        self.y += self.speed * delta * (0 if _y is None else -1 if _y else 1)
            
    def draw(self, window: graphics.window.Window, *args) -> None:
        return super().draw(window, *args)


def on_click(window:graphics.window.Window, scene_1:graphics.scene.Scene,
             scene_2:graphics.scene.Scene, button_1:graphics.ui.Button,
             button_2:graphics.ui.Button, *args) -> None:
    if scene_1.get_should_draw():
        if button_1.is_click():
            scene_1.set_should_draw(False)
            scene_2.set_should_draw(True)
        if button_2.is_click():
            window.destroy()

def keydown(window:graphics.window.Window, scene_1:graphics.scene.Scene,
             scene_2:graphics.scene.Scene, player:Player, key, *args):
    if MapedKey("Reset", key):
        if not (scene_1.get_should_draw() or scene_2.get_should_draw()):
            scene_1.set_should_draw(True)
    if scene_1.get_should_draw():
        if MapedKey("Break", key):
            scene_1.set_should_draw(False)
    elif scene_2.get_should_draw():
        if MapedKey("Break", key):
            scene_1.set_should_draw(True)
            scene_2.set_should_draw(False)
def keyboard_handler(window:graphics.window.Window, scene_1:graphics.scene.Scene,
             scene_2:graphics.scene.Scene, player:Player, keys, *args):
    if scene_1.get_should_draw():
        pass
    elif scene_2.get_should_draw():
        # Calc Delta
        delta = round(1 / window.get_fps(), 4)
        # Move Player
        player.move(
            [KeyMap("RIGHT", keys), KeyMap("LEFT", keys)],
            [KeyMap("DOWN", keys), KeyMap("UP", keys)],
            delta
        )

def main() -> int:
    # Create Objects
    ## Create the Window
    window = graphics.window.Window(
        title = "exemple 2",
        auto_draw = True,
        resizability = False
    )
    ## Create Player
    player = Player((0, 0), 200)
    ## Centre The Player
    width, height = window.get_centre()
    player.x = width - player.width // 2
    player.y = height - player.height // 2
    ## Create the 2 ui.Button
    button_1 = graphics.ui.Button(
        text = "Play",
        y = 120
    )
    button_2 = graphics.ui.Button(
        text = "Exit",
        y = 240
    )
    ## Create the Scene (a Container)
    scene_1 = graphics.scene.Scene(
        window,
        name = "scene 1",
        background = (28, 120, 71)
    )
    scene_2 = graphics.scene.Scene(
        window,
        name = "scene 2",
        background = (0x34, 0x1A, 0x00)
    )
    # Link Objects
    scene_1.append_object(
        button_1,
        centred_horizontally = True,
    )
    scene_1.append_object(
        button_2,
        centred_horizontally = True,
    )
    scene_2.append_object(
        player,
        centred_horizontally = True,
    )
    # Setup handles
    window.mouse_handler = lambda *args: on_click(window, scene_1, scene_2,
                                                  button_1, button_2, *args)
    window.keyboard_handler = lambda *args: keyboard_handler(window, scene_1,
                                                            scene_2, player,
                                                            *args)
    window.on_key_down = lambda *args: keydown(window, scene_1,scene_2,
                                               player,*args)
    scene_1.set_should_draw(True)
    # the Window Loop
    while window.running:
        window.show()
    return 0
# The Entry Point
if __name__ == "__main__":
    exit(
        main()
    )
