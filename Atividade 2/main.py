import pygame
import sys
import time

WHITE = (255, 255, 255)

def DDA(x1, y1, x2, y2, screen):
    dx = x2 - x1
    dy = y2 - y1
    steps = 0
    if abs(dx) > abs(dy):
        steps = abs(dx)
    else:
        steps = abs(dy)
    x_inc = dx / steps
    y_inc = dy / steps
    x = x1
    y = y1
    for i in range(steps):
        pygame.draw.rect(screen, WHITE, (x, y, 1, 1))
        x += x_inc
        y += y_inc

#teste
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("DDA")
    screen.fill((0, 0, 0))
    pygame.display.flip()
    time.sleep(5)
    DDA(100, 100, 200, 200, screen)
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()
    sys.exit()


