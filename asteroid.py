import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        # Вызов конструктора родительского класса CircleShape
        super().__init__(x, y, radius)

        # Создаем изображение астероида как круг
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 255, 255), (self.radius, self.radius), self.radius, 2)
        
        # Устанавливаем прямоугольник (rect), который будет использоваться для позиционирования
        self.rect = self.image.get_rect(center=(x, y))

    def update(self, dt):
        # Обновляем позицию астероида по его скорости
        self.position += self.velocity * dt
        self.rect.center = self.position  # Обновляем позицию rect
        print(f"Asteroid at {self.position}")  # Отладочное сообщение

    def draw(self, screen):
        # Рисуем астероид на экране
        screen.blit(self.image, self.rect)

