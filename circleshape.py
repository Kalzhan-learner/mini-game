import pygame
from circleshape import CircleShape

class PlayerCircle(CircleShape):
    def __init__(self, x, y, radius, color):
        super().__init__(x, y, radius)
        self.color = color  # Цвет игрока

    def draw(self, screen):
        # Отображаем круг с учетом позиции и радиуса
        pygame.draw.circle(screen, self.color, (int(self.position.x), int(self.position.y)), self.radius)

    def update(self, dt):
        # Обновляем позицию или другие параметры (например, по скорости)
        self.position += self.velocity * dt

class Player(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 255, 0), (int(self.position.x), int(self.position.y)), self.radius)

    def update(self, dt):
        self.position += self.velocity * dt