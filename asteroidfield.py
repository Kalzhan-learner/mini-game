import pygame
import random
from asteroid import Asteroid
from constants import *

class AsteroidField:
    edges = [
        [pygame.Vector2(1, 0), lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT)],
        [pygame.Vector2(-1, 0), lambda y: pygame.Vector2(SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT)],
        [pygame.Vector2(0, 1), lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS)],
        [pygame.Vector2(0, -1), lambda x: pygame.Vector2(x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS)],
    ]

    def __init__(self, asteroids_group):
        self.spawn_timer = 0.0
        self.asteroids_group = asteroids_group  # Группа астероидов

    def spawn(self, radius, position, velocity):
        # Ограничиваем позицию астероида в пределах экрана
        position.x = max(min(position.x, SCREEN_WIDTH - radius), radius)
        position.y = max(min(position.y, SCREEN_HEIGHT - radius), radius)
        
        print(f"Spawning asteroid at {position}")  # Добавляем отладочную информацию
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity

        # Добавляем астероид в группу
        self.asteroids_group.add(asteroid)

    def update(self, dt):
        self.spawn_timer += dt
        if self.spawn_timer > ASTEROID_SPAWN_RATE:
            self.spawn_timer = 0

            # Появление нового астероида случайным образом
            edge = random.choice(self.edges)
            speed = random.randint(40, 60)
            velocity = edge[0] * speed
            velocity = velocity.rotate(random.randint(-30, 30))
            position = edge[1](random.uniform(0, 1))
            kind = random.randint(1, ASTEROID_KINDS)
            self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity)

    def draw(self, screen):
        self.asteroids_group.draw(screen)  # Рисуем все астероиды из группы












