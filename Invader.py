import pygame
from constants import *
import utils


class Invader:
    def __init__(self):
        self.x, self.y = INVADER_INIT
        self.dx, self.dy = INVADER_CHANGES
        invader_icon_path = utils.get_path(INVADER_ICONS_PATH,
                                           INVADER_ICON_FILE_NAME)
        self.invader_icon = pygame.image.load(invader_icon_path)
        self.icon_size = INVADER_ICON_SIZE
        self.right_boundary = WIDTH - self.icon_size

    def move(self):
        self.x += self.dx
        dx, dy = INVADER_CHANGES
        if self.x <= 0:
            self.dx = dx
            self.y += dy
        if self.x >= self.right_boundary:
            self.dx = -dx
            self.y += dy
