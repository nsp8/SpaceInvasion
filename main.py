import pygame
from GameEnvironment import GameEnvironment

running = True
game = GameEnvironment()
player_X = game.player.x
invader_X, invader_Y = game.invader.x, game.invader.y
while running:
    # game.screen.fill((0, 0, 0))
    game.screen.blit(game.background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        game.handle_player_actions(event)
    # TODO: Refactor this
    game.player.correct_boundary()
    game.add_player()
    game.invader.move()
    game.add_invader()
    if game.player.weapon.state == "fire":
        game.player.weapon.move()
        game.add_weapon()
    pygame.display.update()

print("Exited Game")
