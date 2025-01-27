import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, groups=None):
        # we will be using this later
        # if hasattr(self, "containers"):
        #     super().__init__(self.containers)
        # else:
        #     super().__init__()
        # Если groups не переданы, инициализируем их как пустой список
        if groups is None:
            groups = []
        super().__init__(*groups)  # Разворачиваем список и передаем в super

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def check_collision(self, other):
        # Вычисление расстояния между центрами двух объектов
        distance = self.position.distance_to(other.position)
        
        # Если расстояние меньше или равно сумме радиусов, значит произошло столкновение
        if distance <= (self.radius + other.radius):
            return True
        return False
