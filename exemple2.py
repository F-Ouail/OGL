import ogl

KeysMap = {
    "UP" : [
        ogl.pygame.K_UP,
        ogl.pygame.K_w,
        ogl.pygame.K_z, # for azerty keyboards
    ],
    "DOWN" : [
        ogl.pygame.K_DOWN,
        ogl.pygame.K_s,
    ],
    "RIGHT" : [
        ogl.pygame.K_RIGHT,
        ogl.pygame.K_d,
    ],
    "LEFT" : [
        ogl.pygame.K_LEFT,
        ogl.pygame.K_a,
        ogl.pygame.K_q, # for azerty keyboards
    ],
    "BREAK" : [
        ogl.pygame.K_ESCAPE,
    ],
    "RESET" : [
        ogl.pygame.K_F4,
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

class Player(ogl.basic.Square):
    def __init__(self, pos:tuple[int, int], speed:int) -> None:
        super().__init__(ogl.color.Color(252, 226, 196), pos[0], pos[1], 
                         width = 50, height = 50)
        self.object_string_name = "Player"
        self.speed:int = speed
    def move(self, vertically:tuple[bool, bool], horizontally:tuple[bool, bool], delta:float):
        x = None if vertically[0] == vertically[1] else False if vertically[0] else True
        y = None if horizontally[0] == horizontally[1] else False if horizontally[0] else True
        self.x += self.speed * delta * (0 if x is None else -1 if x else 1)
        self.y += self.speed * delta * (0 if y is None else -1 if y else 1)
            
    def draw(self, window: ogl.window.Window, *args) -> None:
        return super().draw(window, *args)


def on_click(window:ogl.window.Window, scene_1:ogl.scene.Scene,
             scene_2:ogl.scene.Scene, button_1:ogl.ui.Button,
             button_2:ogl.ui.Button, *args) -> None:
    if scene_1.get_should_draw():
        if button_1.is_click():
            scene_1.set_should_draw(False)
            scene_2.set_should_draw(True)
        if button_2.is_click():
            window.destroy()

def keydown(window:ogl.window.Window, scene_1:ogl.scene.Scene,
             scene_2:ogl.scene.Scene, player:Player, key, *args):
    if MapedKey("Reset", key):
        if not (scene_1.get_should_draw() or scene_2.get_should_draw()):
            scene_1.set_should_draw(True)
    if scene_1.get_should_draw():
        window.destroy()
    elif scene_2.get_should_draw():
        if MapedKey("Break", key):
            scene_1.set_should_draw(True)
            scene_2.set_should_draw(False)
def keyboard_handler(window:ogl.window.Window, scene_1:ogl.scene.Scene,
             scene_2:ogl.scene.Scene, player:Player, keys, *args):
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
    window = ogl.window.Window(
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
    button_1 = ogl.ui.Button(
        text = "Play",
        y = 120
    )
    button_2 = ogl.ui.Button(
        text = "Exit",
        y = 240
    )
    ## Create the Scene (a Container)
    scene_1 = ogl.scene.Scene(
        window,
        name = "scene 1",
        background = (28, 120, 71)
    )
    scene_2 = ogl.scene.Scene(
        window,
        name = "scene 2",
        background = (0x56,0x7d,0x46 )
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
