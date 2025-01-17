import pygame
from constants import *  # Импортируем SCREEN_WIDTH и SCREEN_HEIGHT

def main():
    # Инициализация Pygame
    pygame.init()

    # Создание окна с размерами из constants.py
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Простой игровой цикл")  # Заголовок окна
    print("Game window created!")

    clock = pygame.time.Clock()

    dt = 0

    # Основной игровой цикл
    running = True  # Игра продолжается, пока running = True
    while running:
        print("Waiting for events...")

        # Обработка всех событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Закрытие игры

        # Заполнение экрана чёрным цветом
        screen.fill((0, 0, 0))  # Чёрный фон для игры

        dt = clock.tick(60) / 1000
        # Обновление экрана
        pygame.display.flip()

        # Дополнительная отладочная информация
        print("Game is running...")

    # Завершение работы Pygame
    pygame.quit()
    print("Game has ended.")

if __name__ == "__main__":
    main()

