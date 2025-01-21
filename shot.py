import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(pygame.sprite.Sprite):
    def __init__(self, x, y, velocity):
        super().__init__()
        self.position = pygame.Vector2(x, y)
        self.velocity = velocity
        self.radius = SHOT_RADIUS
        self.image = pygame.Surface((2 * self.radius, 2 * self.radius), pygame.SRCALPHA)  # прозрачная поверхность
        self.rect = self.image.get_rect(center=(self.position.x, self.position.y))

    def update(self, dt):
        # Обновляем положение пули
        self.position += self.velocity * dt
        self.rect.center = (self.position.x, self.position.y)

    def draw(self, screen):
        self.image.fill((0, 0, 0, 0))  # очищаем поверхность перед рисованием
        pygame.draw.circle(self.image, (255, 0, 0), (self.radius, self.radius), self.radius)
        screen.blit(self.image, self.rect)



