import graphics


def movement(b1, b2, speed):
    if b1 and b2: # don't move (return 0) if both is true because the move and their opposite canceled each other
        return 0
    if b1: # move posite
        return speed
    elif b2: # move negative
        return -speed
    else: # if there is a runtime problem don't move
        return 0
def keyboard(keys, *args):
    delta = round(1/window.get_fps(), 4)
    square.x, square.y = square.x + movement(keys[ord('d')], keys[ord('a')], delta * speed), square.y + movement(keys[ord('s')], keys[ord('w')], delta * speed)
speed = 250
window = graphics.window.Window("exemple 2", auto_draw=True, resizability=True)
square = graphics.basic.Square()
scene = graphics.scene.Scene(window, "scene 1", (155,155,255))
window.keyboard_handler = keyboard
scene.append_object(square)
scene.set_should_draw(True)

while window.running:
    window.show()
