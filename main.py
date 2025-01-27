import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_RADIUS, PLAYER_SHOOT_SPEED
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Создаем группу для игрока
    player_group = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()  # Группа пуль
    asteroids_group = pygame.sprite.Group()  # Группа астероидов
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    clock = pygame.time.Clock()

    # Переменная для хранения времени в каждом кадре
    dt = 0

    # Создание групп
    updatable = [player, AsteroidField(asteroids_group)]  # Добавляем объекты для обновления
    drawable = [player, AsteroidField(asteroids_group)]  # Добавляем объекты для рисования

    # Добавляем Player в обе группы
    updatable.append(player)
    drawable.append(player)

    asteroids = pygame.sprite.Group()  # Группа для астероидов
    asteroid_field = AsteroidField(asteroids)  # Создаем объект AsteroidField и передаем группу
    updatable.append(asteroid_field)  # Добавляем в список обновляемых объектов
    drawable.append(asteroid_field)   # Добавляем в список рисуемых объектов

    # Добавляем пули в список обновляемых и рисуемых объектов
    updatable.append(player.shots)
    drawable.append(player.shots)
    
    # Создаем группу для пуль
    # all_shots = pygame.sprite.Group()  # Группа для всех пуль
    # updatable.append(all_shots)  # Добавляем пули в обновляемые объекты
    # drawable.append(all_shots)   # Добавляем пули в рисуемые объекты

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        dt = clock.tick(60) / 1000  # Расчет времени между кадрами
        for obj in updatable:
            obj.update(dt)

        # Проверка столкновений
        for asteroid in asteroids_group:
            if player.check_collision(asteroid):
                print("Game over!")
                running = False

        # Проверка столкновений между пулями и астероидами
        for asteroid in asteroids_group:
            for shot in player.shots:  # Перебираем все пули
                if asteroid.rect.colliderect(shot.rect):  # Проверка на столкновение
                    asteroid.kill()  # Удаляем астероид
                    shot.kill()  # Удаляем пулю

        # Рисуем все объекты в drawable
        screen.fill((0, 0, 0))  # Заливаем экран черным
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # dt = clock.tick(60) / 1000

    pygame.quit()


if __name__ == "__main__":
    main()