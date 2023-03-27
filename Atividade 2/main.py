import pygame
import sys
import time


def DDA(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    step = 0
    if abs(dx) > abs(dy):
        step = abs(dx)
    else:
        step = abs(dy)

    x_inc = dx / step
    y_inc = dy / step

    x = x1
    y = y1

    points = []

    while x != x2 and y != y2:
        points.append((round(x), round(y)))
        x += x_inc
        y += y_inc

    points.append((x2, y2))
    return points


def bresenham_lines(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1

    p = 2 * dy - dx
    _2dy = 2 * dy
    _2dy_2dx = 2 * (dy - dx)

    points = []
    if dy > dx:
        points = bresenham_lines(y1, x1, y2, x2)
        for i in range(len(points)):
            points[i] = (points[i][1], points[i][0])
        return points

    x = x1
    y = y1

    while x != x2 and y != y2:
        points.append((x, y))

        x += sx
        if p < 0:
            p += _2dy
        else:
            y += sy
            p += _2dy_2dx

    points.append((x2, y2))
    return points


def bresenham_circle(xc, yc, r):
    p = 1 - r
    x = 0
    y = r

    points = []
    while x <= y:
        points.append((xc + x, yc + y))
        points.append((xc + x, yc - y))
        points.append((xc - x, yc + y))
        points.append((xc - x, yc - y))
        points.append((xc + y, yc + x))
        points.append((xc + y, yc - x))
        points.append((xc - y, yc + x))
        points.append((xc - y, yc - x))

        if p < 0:
            p += 2 * x + 1
        else:
            p += 2 * (x - y) + 1
            y -= 1
        x += 1

    return points


if __name__ == "__main__":
    WHITE = (255, 255, 255)
    _points1 = DDA(0, 0, 250, 300)
    _points2 = bresenham_lines(0, 0, 250, 300)
    _points3 = bresenham_circle(200, 200, 50)

    print("Pontos DDA: {}".format(_points1))
    print("Pontos Bresenham: {}".format(_points2))
    print("Pontos Circulo: {}".format(_points3))

    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    screen.fill(WHITE)
    pygame.display.flip()

    for point in _points1:
        pygame.draw.circle(screen, (0, 0, 0), point, 1)
        pygame.display.flip()
        time.sleep(0.01)

    for point in _points2:
        pygame.draw.circle(screen, (0, 0, 255), point, 1)
        pygame.display.flip()
        time.sleep(0.01)

    for point in _points3:
        pygame.draw.circle(screen, (255, 0, 0), point, 1)
        pygame.display.flip()
        time.sleep(0.01)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
