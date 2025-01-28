import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS, ASTEROID_KINDS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, groups=None):
        super().__init__(x, y, radius, groups)

        # Создаем изображение астероида как круг
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 255, 255), (self.radius, self.radius), self.radius, 2)
        
        # Устанавливаем прямоугольник (rect), который будет использоваться для позиционирования
        self.rect = self.image.get_rect(center=(x, y))

    def update(self, dt):
        # Обновляем позицию астероида по его скорости
        self.position += self.velocity * dt
        self.rect.center = self.position

    def draw(self, screen):
        # Рисуем астероид на экране
        screen.blit(self.image, self.rect)

    def split(self):
        # Удаляем текущий астероид
        self.kill()

        # Если радиус астероида меньше или равен минимальному, астероид исчезает
        if self.radius <= ASTEROID_MIN_RADIUS:
            return  # Малый астероид исчезает

        # Вычисляем случайный угол для поворота астероидов
        random_angle = random.uniform(20, 50)

        # Рассчитываем новые скорости для астероидов, повернутых на random_angle и -random_angle
        velocity1 = self.velocity.rotate(random_angle) * 1.2  # Увеличиваем скорость на 1.2 для новых астероидов
        velocity2 = self.velocity.rotate(-random_angle) * 1.2  # Увеличиваем скорость для второго астероида

        # Новый радиус для меньших астероидов
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Создаем два новых астероида с новым радиусом и скоростью
        Asteroid(self.position.x, self.position.y, new_radius, [self.groups()[0]]).velocity = velocity1
        Asteroid(self.position.x, self.position.y, new_radius, [self.groups()[0]]).velocity = velocity2

        # Задаем скорости для новых астероидов
        new_asteroid1.velocity = velocity1  # Устанавливаем скорость для первого нового астероида
        new_asteroid2.velocity = velocity2  # Устанавливаем скорость для второго нового астероида

