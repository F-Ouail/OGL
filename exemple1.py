import graphics

def on_click(*args):
    if btn.is_click():
        print("BTN clicked")


window = graphics.window.Window("exemple 1", auto_draw=True, resizability=True)
btn = graphics.ui.Button()
scene = graphics.scene.Scene(window, "scene 1")

scene.append_object(btn, True, True)
scene.set_should_draw(True)
btn._mouse = graphics.window.mouse.pos
window.mouse_handler = on_click # type: ignore

while window.running:
    window.show()
