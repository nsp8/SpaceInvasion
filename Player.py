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
        self.right_boundary = WIDTH - PLAYER_ICON_SIZE
        self.weapon = PlayerWeapon()
        # TODO: add weapons on RT (on each press of SPACE)

    def correct_boundary(self):
        self.x += self.dx
        if self.x <= 0:
            self.x = 0
        if self.x >= self.right_boundary:
            self.x = self.right_boundary

    # def fire_weapon(self):
    #     self.weapon.state = "fire"

    def __repr__(self):
        # return f"({self.x}, {self.y}) [{self.weapon}]"
        return f"Player @({self.x}, {self.y})"


class PlayerWeapon:
    def __init__(self, x=None, y=None):
        # self.x, self.y = PLAYER_X_INIT, PLAYER_Y_INIT
        self.x, self.y = x, y
        self.dx, self.dy = WEAPON_DX, WEAPON_DY
        self.is_ready = True
        self.state = "ready"
        weapon_path = utils.get_path(PLAYER_ICONS_PATH, BULLET_ICON_FILE_NAME)
        self.img = pygame.image.load(weapon_path)

    def fire(self):
        print("FIRING!")
        self.is_ready = False
        self.state = "fire"
        # while self.y != 0:
        #     self.y -= self.dy

    def move(self):
        if self.y + PLAYER_ICON_SIZE + WEAPON_Y_OFFSET > 0:
            self.y -= self.dy
        else:
            self.reload_weapon()

    def reload_weapon(self):
        # TODO: make limited: check if weapons exist
        self.is_ready = True
        self.state = "ready"

    def set_coordinates(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return f"{self.state.upper()} ({self.x}, {self.y})"
