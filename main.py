import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_RADIUS
from player import Player

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    clock = pygame.time.Clock()

    # Переменная для хранения времени в каждом кадре
    dt = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        player.update(dt)
        screen.fill((0, 0, 0))
        player.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

    pygame.quit()


if __name__ == "__main__":
    main()