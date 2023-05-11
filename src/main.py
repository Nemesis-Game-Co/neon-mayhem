from entities.player import Player
from entities.shield import Shield
import pygame
from pygame import Vector2

def main():
    pygame.init()

    # constantes de tamanho da janela
    WIDTH = 1280
    HEIGHT = 720
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # instancio um player pra testar a renderização.
    player = Player(Vector2(WIDTH / 2, HEIGHT / 2), 100, Shield(0))

    clock = pygame.time.Clock()
    deltaTime = 0
    running = True

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("Black")

        # RENDER YOUR GAME HERE
        player.drawAt(screen)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            running = False

        if keys[pygame.K_w]:
            player.moveUp(deltaTime)

        if keys[pygame.K_a]:
            player.moveLeft(deltaTime)

        if keys[pygame.K_s]:
            player.moveDown(deltaTime)

        if keys[pygame.K_d]:
            player.moveRight(deltaTime)

        # flip() the display to put your work on screen
        pygame.display.flip()

        deltaTime = clock.tick(60) / 1000  # limits FPS to 60

    pygame.quit()

if __name__ == '__main__':
    main()