import pygame
import sys
import math

pygame.init()

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

WIDTH = int(input("Введите ширину экрана: "))
HEIGHT = int(input("Введите высоту экрана: "))
mass1 = float(input("Введите массу первого шара: "))
mass2 = float(input("Введите массу второго шара: "))
velocity1 = float(input("Введите начальную скорость первого шара: "))
velocity2 = float(input("Введите начальную скорость второго шара: "))
angle1 = float(input("Введите угол (в градусах) движения первого шара: "))
angle2 = float(input("Введите угол (в градусах) движения второго шара: "))

# Преобразуем углы из градусов в радианы
angle1_rad = math.radians(angle1)
angle2_rad = math.radians(angle2)

# Определяем начальные компоненты скорости для каждого шара
velocity1_x = velocity1 * math.cos(angle1_rad)
velocity1_y = velocity1 * math.sin(angle1_rad)
velocity2_x = velocity2 * math.cos(angle2_rad)
velocity2_y = velocity2 * math.sin(angle2_rad)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Абсолютно упругое столкновение")

radius1, radius2 = 30, 30
x1, y1 = 100, HEIGHT // 2
x2, y2 = WIDTH - 100, HEIGHT // 2

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Обновляем позиции
    x1 += velocity1_x
    y1 += velocity1_y
    x2 += velocity2_x
    y2 += velocity2_y

    # Проверка столкновения
    if math.hypot(x1 - x2, y1 - y2) <= radius1 + radius2:
        v1x, v1y = velocity1_x, velocity1_y
        v2x, v2y = velocity2_x, velocity2_y

        velocity1_x = ((mass1 - mass2) * v1x + 2 * mass2 * v2x) / (mass1 + mass2)
        velocity1_y = ((mass1 - mass2) * v1y + 2 * mass2 * v2y) / (mass1 + mass2)
        velocity2_x = ((mass2 - mass1) * v2x + 2 * mass1 * v1x) / (mass1 + mass2)
        velocity2_y = ((mass2 - mass1) * v2y + 2 * mass1 * v1y) / (mass1 + mass2)

    # Проверка границ
    if x1 <= radius1 or x1 >= WIDTH - radius1:
        velocity1_x = -velocity1_x
    if y1 <= radius1 or y1 >= HEIGHT - radius1:
        velocity1_y = -velocity1_y

    if x2 <= radius2 or x2 >= WIDTH - radius2:
        velocity2_x = -velocity2_x
    if y2 <= radius2 or y2 >= HEIGHT - radius2:
        velocity2_y = -velocity2_y

    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (int(x1), int(y1)), radius1)
    pygame.draw.circle(screen, BLUE, (int(x2), int(y2)), radius2)
    pygame.display.flip()
    clock.tick(60)