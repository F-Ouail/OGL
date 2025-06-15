import ogl

"""
    A simple window with one scene
"""


def on_click(window: ogl.window.Window, button: ogl.ui.Button, *args):
    if button.is_mouse_on():
        window.destroy()


def main() -> int:
    # Create Objects
    ## Create the Window
    window = ogl.window.Window(title="exemple 1", auto_draw=True, resizability=True)
    ## Create the ui.Button
    button = ogl.ui.Button(text="Exit")
    ## Create the Scene (a Container)
    scene = ogl.scene.Scene(window, name="scene 1", background=(28, 120, 71))
    # Link Objects
    scene.append_object(button, centred_horizontally=True, centred_vertically=True)
    # Setup Objects
    window.mouse_handler = lambda *args: on_click(window, button, *args)
    scene.set_should_draw(True)
    # the Window Loop
    while window.running:
        window.show()
    return 0


# The Entry Point
if __name__ == "__main__":
    exit(main())
