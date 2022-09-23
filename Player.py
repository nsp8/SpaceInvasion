import pygame
from constants import *
import utils


class Player:
    def __init__(self):
        self.x, self.y = PLAYER_X_INIT, PLAYER_Y_INIT
        self.dx = 0
        player_icon_path = utils.get_path(PLAYER_ICONS_PATH,
                                          PLAYER_ICON_FILE_NAME)
        self.player_icon = pygame.image.load(player_icon_path)
        self.icon_size = PLAYER_ICON_SIZE
        self.right_boundary = WIDTH - self.icon_size
        self.weapon = PlayerWeapon()

    def correct_boundary(self):
        self.x += self.dx
        if self.x <= 0:
            self.x = 0
        if self.x >= self.right_boundary:
            self.x = self.right_boundary

    def fire_weapon(self):
        self.weapon.state = "fire"


class PlayerWeapon:
    def __init__(self):
        self.x, self.y = 0, PLAYER_Y_INIT
        self.dx, self.dy = 0, 10
        self.state = "ready"
        weapon_path = utils.get_path(PLAYER_ICONS_PATH, BULLET_ICON_FILE_NAME)
        self.img = pygame.image.load(weapon_path)
