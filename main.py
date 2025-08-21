import pygame
from sprites import Ball
from constants import Config


def main():
    pygame.init()
    screen = pygame.display.set_mode((Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True

    ball = Ball()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        ball.move()

        screen.fill((0, 0, 0))
        ball.draw(screen)
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
