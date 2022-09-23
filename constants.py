from random import randint


GAME_TITLE = "Space Invasion!"
PLAYER_ICON_SIZE, INVADER_ICON_SIZE = 64, 64
PLAYER_ICONS_PATH = rf"icons\space_invaders_{PLAYER_ICON_SIZE}\png"
INVADER_ICONS_PATH = rf"icons\space_invaders_{INVADER_ICON_SIZE}\png"
GAME_BACKGROUND_FILE_NAME = "space-bg-med.jpg"
TITLE_ICON_FILE_NAME = "003-alien.png"
PLAYER_ICON_FILE_NAME = "001-space-ship.png"
INVADER_ICON_FILE_NAME = "008-alien-2.png"
BULLET_ICON_FILE_NAME = "001-bullet.png"
# WIDTH, HEIGHT = 800, 600
WIDTH, HEIGHT = 1920/2, 1248/2
# PLAYER_X_INIT, PLAYER_Y_INIT = 370, 480
PLAYER_X_INIT, PLAYER_Y_INIT = (WIDTH / 2) - PLAYER_ICON_SIZE, 480
INVADER_INIT = randint(0, 800), randint(50, 150)
INVADER_CHANGES = 0.1, 40
PLAYER_X_SPEED, PLAYER_Y_SPEED = 0.3, 0.1
# TODO: create map of different ships with their properties (speed,
#  health, etc.)
