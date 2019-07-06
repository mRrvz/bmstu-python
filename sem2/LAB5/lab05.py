import pygame
import time
from math import pi, cos, sin, radians

def rocket_lines_right(y):
    # rocket lines (right)
    std_x1 = x_rocket_base + 60
    std_y1 = RB_bottom_left[1]
    std_x2 = x_rocket_base + 70
    std_y2 = RB_bottom_left[1] + 40
    for i in range(0, 90, 5):
        pygame.draw.line(screen, YELLOW, [std_x1 + i, std_y1 - y], [std_x2 + i, std_y2 - y], 3)


def rocket_lines_left(y):
    # rocket lines (left)
    std_x1 = x_rocket_base - 27
    std_y1 = RB_bottom_left[1]
    std_x2 = x_rocket_base - 40
    std_y2 = RB_bottom_left[1] + 40
    for i in range(0, 90, 5):
        pygame.draw.line(screen, YELLOW, [std_x1 + i, std_y1 - y], [std_x2 + i, std_y2 - y], 3)


def rocket_move(x, y):
    # ROCKET TOP
    pygame.draw.ellipse(screen, YELLOW, (x_rocket_base + x + 0.5, y_rocket_base - 90  - y, 118, 170))
    # ROCKET BASE
    pygame.draw.rect(screen, RED, (x_rocket_base - x, y_rocket_base - y, rocket_base_width, rocket_base_height))
    # ROCKET BOTTOM
    pygame.draw.polygon(screen, WHITE, [[RB_top_left[0] - x, RB_top_left[1] - y], \
                        [RB_top_right[0] + x, RB_top_right[1] - y], [RB_bottom_right[0] + x, RB_bottom_right[1] - y], \
                        [RB_bottom_left[0] - x, RB_bottom_left[1] - y]])
    # ROCKET MID
    pygame.draw.rect(screen, BLACK, (x_rocket_base - 1, y_rocket_base - 10 - y, rocket_base_width + 1, rocket_base_height - 180))
    # DRAW LINES (FUEL)
    rocket_lines_left(y)
    rocket_lines_right(y)


def static_land():
    # LAND
    pygame.draw.rect(screen, GREEN, (0, WINY - 100, WINX, 100))
    pygame.draw.rect(screen, GRAY, (x_rocket_base - 50, 480, 220, 20))


def static_sky():
    # SKY
    pygame.draw.rect(screen, LIGHT_BLUE, (0, 0, WINX, WINY - 100))


def tank_move(x, x_shot_upd):
    # TOP OF TANK
    pygame.draw.ellipse(screen, DARK_GREEN, (x_cater + 100 + x, y_cater - 120, tank_top_width, tank_height + 40))
    # BASE OF TANK
    pygame.draw.polygon(screen, DARK_GREEN, [[x_cater + 40 + x, y_cater - 60], [x_cater + tank_width - 80 + x, y_cater - 60], \
                                        [x_cater + 400 + x, y_cater + 20], [x_cater + x, y_cater + 20] ])
    pygame.draw.line(screen, BLACK, (x_cater + 40 + x, y_cater - 58), (x_cater + x + tank_top_width + 122, y_cater - 58), 3)
    pygame.draw.line(screen, BLACK, (x_cater + 40 + x, y_cater - 58), (x_cater + x, y_cater + 20), 3)
    pygame.draw.line(screen, BLACK, (x_cater + tank_width - 80 + x, y_cater - 58), (x_cater + tank_width + x, y_cater + 20), 3)
    pygame.draw.line(screen, BLACK, (x_cater + x, y_cater + 20), (x_cater + x + 25, y_cater + 20), 3)
    pygame.draw.line(screen, BLACK, (x_cater + x + tank_width - 40, y_cater + 20), (x_cater + x + tank_width, y_cater + 20), 3)
    # CATERPILLARS
    pygame.draw.ellipse(screen, DARK_OLIVE, (x_cater + x, y_cater, tank_width, tank_height), 0)
    pygame.draw.ellipse(screen, BLACK, (x_cater + x, y_cater, tank_width, tank_height), 5)
    # MUZZLE
    pygame.draw.line(screen, DARK_GREEN, (x_muzzle + x, y_muzzle), (x_muzzle + 240 + x, y_muzzle), 10)
    pygame.draw.line(screen, BLACK, (x_muzzle + 240 + x, y_muzzle), (x_muzzle + 260 + x, y_muzzle), 10)
    # WHEELS
    LEN = 30
    cos_wheel = cos(180 * x * 0.0001 / pi)
    sin_wheel = sin(180 * x * 0.0001 / pi)
    pygame.draw.ellipse(screen, BLACK, ((x_cater + 40) + x, (y_cater + 10), tank_width / 5, (tank_height - 20)), 3)

    pygame.draw.line(screen, ORANGE, (x_cater + 80 + x, y_cater + 40), \
                     (x_cater + 80 + x + sin_wheel * LEN, y_cater + 40 + cos_wheel * LEN), 3)
    pygame.draw.line(screen, ORANGE, (x_cater + 80 + x, y_cater + 40), \
                     (x_cater + 80 + x + sin_wheel * -LEN, y_cater + 40 + cos_wheel * -LEN), 3)
    pygame.draw.line(screen, ORANGE, (x_cater + 80 + x, y_cater + 40), \
                    (x_cater + 80 + x + cos_wheel * LEN, y_cater + 40 - sin_wheel * LEN), 3)
    pygame.draw.line(screen, ORANGE, (x_cater + 80 + x, y_cater + 40), \
                     (x_cater + 80 + x + cos_wheel * -LEN, y_cater + 40 - sin_wheel * -LEN), 3)

    # wheels cross
    pygame.draw.ellipse(screen, BLACK, ((x_cater + 120) + x, (y_cater + 3), tank_width / 5, (tank_height - 6)), 3)
    pygame.draw.line(screen, ORANGE, (x_cater + 160 + x, y_cater + 40), \
                     (x_cater + 160 + x + sin_wheel * LEN + 3, y_cater + 40 + cos_wheel * LEN + 3), 3)
    pygame.draw.line(screen, ORANGE, (x_cater + 160 + x, y_cater + 40), \
                     (x_cater + 160 + x + sin_wheel * -(LEN + 3) , y_cater + 40 + cos_wheel * -(LEN + 3)), 3)
    pygame.draw.line(screen, ORANGE, (x_cater + 160 + x, y_cater + 40), \
                     (x_cater + 160 + x + cos_wheel * LEN + 3, y_cater + 40 - sin_wheel * LEN + 3), 3)
    pygame.draw.line(screen, ORANGE, (x_cater + 160 + x, y_cater + 40), \
                     (x_cater + 160 + x + cos_wheel * -(LEN + 3), y_cater + 40 - sin_wheel * -(LEN + 3)), 3)

    # wheels cross
    pygame.draw.ellipse(screen, BLACK, ((x_cater + 196) + x, (y_cater + 3), tank_width / 5, (tank_height - 6)), 3)
    pygame.draw.line(screen, ORANGE, (x_cater + 236 + x, y_cater + 40), \
                     (x_cater + 236 + x + sin_wheel * LEN + 3, y_cater + 40 + cos_wheel * LEN + 3), 3)
    pygame.draw.line(screen, ORANGE, (x_cater + 236 + x, y_cater + 40), \
                     (x_cater + 236 + x + sin_wheel * -(LEN + 3), y_cater + 40 + cos_wheel * -(LEN + 3)), 3)
    pygame.draw.line(screen, ORANGE, (x_cater + 236 + x, y_cater + 40), \
                     (x_cater + 236 + x + cos_wheel * LEN + 3, y_cater + 40 - sin_wheel * LEN + 3), 3)
    pygame.draw.line(screen, ORANGE, (x_cater + 236 + x, y_cater + 40), \
                     (x_cater + 236 + x + cos_wheel * -(LEN + 3), y_cater + 40 - sin_wheel * -(LEN + 3)), 3)

    # wheels cross
    pygame.draw.ellipse(screen, BLACK, ((x_cater + 273) + x, (y_cater + 10), tank_width / 5, (tank_height - 20)), 3)
    pygame.draw.line(screen, ORANGE, (x_cater + x + 313, y_cater + 40), \
                     (x_cater + x + 313 + sin_wheel * LEN, y_cater + 40 + cos_wheel * LEN), 3)
    pygame.draw.line(screen, ORANGE, (x_cater + x + 313, y_cater + 40), \
                     (x_cater + x + 313 + sin_wheel * -LEN, y_cater + 40 + cos_wheel * -LEN), 3)
    pygame.draw.line(screen, ORANGE, (x_cater + x + 313, y_cater + 40), \
                     (x_cater + x + 313 + cos_wheel * LEN , y_cater + 40 - sin_wheel * LEN), 3)
    pygame.draw.line(screen, ORANGE, (x_cater + x + 313, y_cater + 40), \
                     (x_cater + x + 313 + cos_wheel * -LEN, y_cater + 40 - sin_wheel * -LEN), 3)

    # MINI WHEELS
    LEN = 14
    # mini wheels cross
    pygame.draw.ellipse(screen, BLACK, ((x_cater + 5) + x, (y_cater + 23), tank_width / 10 - 2, (tank_height - 46)), 3)
    pygame.draw.line(screen, ORANGE, (x_cater + 25 + x, y_cater + 40), \
                     (x_cater + 25 + x + sin_wheel * LEN, y_cater + 40 + cos_wheel * LEN), 3)
    pygame.draw.line(screen, ORANGE, (x_cater + 25 + x, y_cater + 40), \
                     (x_cater + 25 + x + sin_wheel * -LEN, y_cater + 40 + cos_wheel * -LEN), 3)
    pygame.draw.line(screen, ORANGE, (x_cater + 25 + x, y_cater + 40), \
                     (x_cater + 25 + x + cos_wheel * LEN, y_cater + 40 - sin_wheel * LEN), 3)
    pygame.draw.line(screen, ORANGE, (x_cater + 25 + x, y_cater + 40), \
                     (x_cater + 25 + x + cos_wheel * -LEN, y_cater + 40 - sin_wheel * -LEN), 3)

    # mini wheels cross
    pygame.draw.ellipse(screen, BLACK, ((x_cater + 350) + x, (y_cater + 21), tank_width / 10 - 2, (tank_height - 42)), 3)
    pygame.draw.line(screen, ORANGE, (x_cater + 370 + x, y_cater + 40), \
                    (x_cater + 370 + x + sin_wheel * LEN, y_cater + 40 + cos_wheel * LEN), 3)
    pygame.draw.line(screen, ORANGE, (x_cater + 370 + x , y_cater + 40), \
                     (x_cater + 370 + x + sin_wheel * -LEN, y_cater + 40 + cos_wheel * -LEN), 3)
    pygame.draw.line(screen, ORANGE, (x_cater + 370 + x, y_cater + 40), \
                     (x_cater + 370 + x + cos_wheel * LEN, y_cater + 40 - sin_wheel * LEN), 3)
    pygame.draw.line(screen, ORANGE, (x_cater + 370 + x + sin_wheel, y_cater + 40), \
                     (x_cater + 370 + x + cos_wheel * -LEN, y_cater + 40 - sin_wheel * -LEN), 3)

    # SHOT
    if x > 400:
        pygame.draw.line(screen, YELLOW, (x_shot_upd + x_shot, y_shot), (x_shot_upd + 30 + x_shot, y_shot), 10)


def text_move(x):
    myfont = pygame.font.SysFont("Comic Sans MS", 24)
    label = myfont.render("ИУ7-23Б", 1, RED)
    screen.blit(label, (x_cater + 140 + x, 320))
    label2 = myfont.render("Методы уточнения корней", 1, GREEN)
    screen.blit(label2, (x_cater + 36 + x, 375))


# ========= CONSTANTS ========

# Window
FPS = 60
WINX = 1200
WINY = 600

# Colors
BLUE = (0, 0, 255)
DARK_OLIVE = (85, 107, 47)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0 )
GRAY = (125, 125, 125)
LIGHT_BLUE = (0, 0, 153)
GREEN = (0, 204, 102)
DARK_GREEN = (0, 51, 0)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
RED = (255, 0, 0)
ORANGE = (99, 51, 3)


# Rocket coordinates
x_rocket_base = 150
y_rocket_base = WINY
rocket_base_width = 120
rocket_base_height = 200
RB_top_left = [x_rocket_base, y_rocket_base + rocket_base_height]
RB_top_right = [x_rocket_base + rocket_base_width, y_rocket_base + rocket_base_height]
RB_bottom_left = [x_rocket_base - 30, y_rocket_base + rocket_base_height + 60]
RB_bottom_right = [x_rocket_base + rocket_base_width + 30, y_rocket_base + rocket_base_height + 60]

# Tank coordinates
x_cater = -805
y_cater = 420
tank_width = 400
tank_height = 80
tank_top_width = 200
x_muzzle = -520
y_muzzle = y_cater - 90
x_shot = 100
y_shot = y_cater - 90

pygame.init()
screen = pygame.display.set_mode((WINX, WINY))
pygame.display.set_caption('Лабораторная работа №5')
clock = pygame.time.Clock()


# Create main window
def main():
    y_rocket = 0; x_rocket = -1
    x_tank = 0; x_shot = -1100
    const_y = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        static_sky()
        rocket_move(x_rocket, y_rocket)
        static_land()
        tank_move(x_tank, x_shot)
        text_move(x_tank)
        const_y += 0.1

        x_rocket *= -1
        x_tank += 7; x_shot += 20
        y_rocket += (const_y * const_y * const_y) / 1000

        if y_rocket > WINY + 520:
            y_rocket = 0; const_y = 0

        if x_tank > WINX + 805:
            x_tank = 0
            x_shot = -1100

        pygame.display.update()
        clock.tick(FPS)


if __name__ == '__main__':
    main()
