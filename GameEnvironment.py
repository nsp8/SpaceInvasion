import pygame
from constants import *
from Player import Player
from Invader import Invader
import utils


class GameEnvironment:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(GAME_TITLE)
        icon_path = utils.get_path(PLAYER_ICONS_PATH, TITLE_ICON_FILE_NAME)
        GameEnvironment.add_image(icon_path)
        background_path = utils.get_path("icons", GAME_BACKGROUND_FILE_NAME)
        self.background = pygame.image.load(background_path)
        self.player = Player()
        self.invader = Invader()

    @staticmethod
    def add_image(path):
        _img = pygame.image.load(path)
        pygame.display.set_icon(_img)

    def add_player(self):
        player = self.player
        self.screen.blit(player.player_icon, (player.x, player.y))

    def add_invader(self):
        invader = self.invader
        self.screen.blit(invader.invader_icon, (invader.x, invader.y))

    def handle_player_actions(self, e):
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT:
                self.player.dx = -PLAYER_X_SPEED
            if e.key == pygame.K_RIGHT:
                self.player.dx = PLAYER_X_SPEED
            if e.key == pygame.K_SPACE:
                self.player.fire_weapon()
        if e.type == pygame.KEYUP:
            if e.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                # Reset/Stop movement on key-up
                self.player.dx = 0
