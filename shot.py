import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        # Инициализация пули
        super().__init__(x, y, SHOT_RADIUS)  # Вызов конструктора родительского класса CircleShape
        self.velocity = velocity  # Устанавливаем скорость пули
        
        # Инициализация прямоугольника (rect) для рисования пули
        self.rect = pygame.Rect(0, 0, SHOT_RADIUS * 2, SHOT_RADIUS * 2)
        self.rect.center = (x, y)  # Центрируем прямоугольник на позиции пули

        # Создание изображения пули (круглый объект)
        self.image = pygame.Surface((SHOT_RADIUS * 2, SHOT_RADIUS * 2), pygame.SRCALPHA)  # Прозрачная поверхность
        pygame.draw.circle(self.image, (255, 0, 0), (SHOT_RADIUS, SHOT_RADIUS), SHOT_RADIUS)  # Рисуем красный круг

    def update(self, dt):
        # Обновляем позицию пули по её скорости
        self.position += self.velocity * dt  # Обновление позиции пули с учетом времени
        self.rect.center = self.position  # Обновляем прямоугольник для рисования пули

    def draw(self, screen):
        # Рисуем пулю (используем self.image для рисования)
        screen.blit(self.image, self.rect)
