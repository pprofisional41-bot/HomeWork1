import pygame
import random

# Инициализация Pygame
pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Простой Тир")

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Настройки мишени
target_size = 50
target_x = random.randint(0, WIDTH - target_size)
target_y = random.randint(0, HEIGHT - target_size)

# Очки и шрифт
score = 0
font = pygame.font.SysFont("Arial", 32)

# Главный цикл игры
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)  # Заливка фона

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Логика стрельбы (клик мышкой)
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Проверка попадания в квадрат
            if target_x <= mouse_x <= target_x + target_size and \
                    target_y <= mouse_y <= target_y + target_size:
                score += 1
                # Перемещаем мишень в новое место
                target_x = random.randint(0, WIDTH - target_size)
                target_y = random.randint(0, HEIGHT - target_size)

    # Рисуем мишень
    pygame.draw.rect(screen, RED, (target_x, target_y, target_size, target_size))

    # Отображаем счет
    score_text = font.render(f"Очки: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    # Обновление экрана
    pygame.display.flip()
    clock.tick(60)  # 60 кадров в секунду

pygame.quit()