import pygame
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED
from circleshape import CircleShape

class Player(pygame.sprite.Sprite):
    def __init__(self, x=100, y=100):
        # Вызов конструктора родительского класса CircleShape с цветом (красный) и радиусом PLAYER_RADIUS
        super().__init__()

        self.position = pygame.Vector2(x, y)

        self.rotation = 0
        
        self.color = (255, 255, 255)

        self.rect = pygame.Rect(0, 0, PLAYER_RADIUS * 2, PLAYER_RADIUS * 2)
        self.rect.center = self.position  # Центрируем прямоугольник на позиции
        
    def move(self, dt, forward=True):
        # создаём единичный вектор, направленный вверх
        forward_vector = pygame.Vector2(0, 1).rotate(self.rotation)
        
        # если нужно двигаться назад, инвертируем направление
        if not forward:
            forward_vector = -forward_vector
        
        # перемещаем игрока
        self.position += forward_vector * PLAYER_SPEED * dt
        

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * PLAYER_RADIUS / 1.5
        a = self.position + forward * PLAYER_RADIUS
        b = self.position - forward * PLAYER_RADIUS - right
        c = self.position - forward * PLAYER_RADIUS + right
        print(f"Triangle points: A={a}, B={b}, C={c}")
        return [a, b, c]

    def draw(self, screen):
        points = self.triangle()  # Получаем точки треугольника
        pygame.draw.polygon(screen, self.color, points, 2)

    def rotate(self, dt):
        # Добавляем угол поворота, учитывая скорость и время
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()  # Получаем состояния всех клавиш

        if keys[pygame.K_a]:
            # Когда нажата клавиша A, вращаем игрока влево (инвертируем dt)
            self.rotation -= PLAYER_TURN_SPEED * dt  # инвертируем поворот
        if keys[pygame.K_d]:
            # Когда нажата клавиша D, вращаем игрока вправо
            self.rotate(dt)  # вызываем метод для поворота вправо
        # проверяем, нажата ли клавиша W или S
        if keys[pygame.K_w]:
            self.move(dt, forward=True)  # двигаем игрока вперёд
        if keys[pygame.K_s]:
            self.move(dt, forward=False)  # двигаем игрока назад













