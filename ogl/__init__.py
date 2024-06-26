"""
    OGL|Ouail Graphics Library| : Graphics library build on pygame\n
    There object are:\n
        Base Objects
        --------------
            Window, Color, WindowObject\n
        Scenes Objects
        ----------------
            Scene, |Basic Objects|, |Animations Objects|, |ui Objects|\n
        Basic Objects
        -------------
            Square, Image
        Animations Objects
        ------------------
            Animation, AnimatedObject , MultiAnimationsObject\n
        ui Objects
        ----------
            Label, Button\n
"""


import pygame
import atexit

from .classes import color, window, animation, scene, ui, basic
VERSION = (0, 0, 0, 1) # 0.0.0.1 BETA
@atexit.register
def quit():
    pygame.quit()
    pygame.font.quit()
pygame.init()
pygame.font.init()
