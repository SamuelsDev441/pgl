import pygame
import sgl.net
import sgl.event
import sgl.image
import sgl.math
rect = 'rect'
circle = 'circle'
blue = (0, 0, 255)
window = pygame.display.set_mode((500, 500))

QUIT = pygame.QUIT


def init():
    pygame.init()


def cwindow(size, title="pySGL Window"):
    pygame.display.set_mode(size)
    pygame.display.set_caption(title)


def update():
    pygame.display.flip()


def title(t):
    pygame.display.set_caption(t)


def wfill(window, color):
    if window == window:
        if color == blue:
            window.fill(blue)


def kill():
    pygame.quit()
