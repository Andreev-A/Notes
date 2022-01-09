# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
#
# import pygame
# import random
# import math
#
# SCREEN_DIM = (800, 600)
#
#
# # =======================================================================================
# # Функции для работы с векторами
# # =======================================================================================
#
# def sub(x, y):
#     """"возвращает разность двух векторов"""
#     return x[0] - y[0], x[1] - y[1]
#
#
# def add(x, y):
#     """возвращает сумму двух векторов"""
#     return x[0] + y[0], x[1] + y[1]
#
#
# def length(x):
#     """возвращает длину вектора"""
#     return math.sqrt(x[0] * x[0] + x[1] * x[1])
#
#
# def mul(v, k):
#     """возвращает произведение вектора на число"""
#     return v[0] * k, v[1] * k
#
#
# def vec(x, y):
#     """возвращает пару координат, определяющих вектор (координаты точки конца вектора),
#     координаты начальной точки вектора совпадают с началом системы координат (0, 0)"""
#     return sub(y, x)
#
#
# # =======================================================================================
# # Функции отрисовки
# # =======================================================================================
# def draw_points(points, style="points", width=3, color=(255, 255, 255)):
#     """функция отрисовки точек на экране"""
#     if style == "line":
#         for p_n in range(-1, len(points) - 1):
#             pygame.draw.line(gameDisplay, color,
#                              (int(points[p_n][0]), int(points[p_n][1])),
#                              (int(points[p_n + 1][0]), int(points[p_n + 1][1])), width)
#
#     elif style == "points":
#         for p in points:
#             pygame.draw.circle(gameDisplay, color,
#                                (int(p[0]), int(p[1])), width)
#
#
# def draw_help():
#     """функция отрисовки экрана справки программы"""
#     gameDisplay.fill((50, 50, 50))
#     font1 = pygame.font.SysFont("courier", 24)
#     font2 = pygame.font.SysFont("serif", 24)
#     data = []
#     data.append(["F1", "Show Help"])
#     data.append(["R", "Restart"])
#     data.append(["P", "Pause/Play"])
#     data.append(["Num+", "More points"])
#     data.append(["Num-", "Less points"])
#     data.append(["", ""])
#     data.append([str(steps), "Current points"])
#
#     pygame.draw.lines(gameDisplay, (255, 50, 50, 255), True, [
#         (0, 0), (800, 0), (800, 600), (0, 600)], 5)
#     for i, text in enumerate(data):
#         gameDisplay.blit(font1.render(
#             text[0], True, (128, 128, 255)), (100, 100 + 30 * i))
#         gameDisplay.blit(font2.render(
#             text[1], True, (128, 128, 255)), (200, 100 + 30 * i))
#
#
# # =======================================================================================
# # Функции, отвечающие за расчет сглаживания ломаной
# # =======================================================================================
# def get_point(points, alpha, deg=None):
#     if deg is None:
#         deg = len(points) - 1
#     if deg == 0:
#         return points[0]
#     return add(mul(points[deg], alpha), mul(get_point(points, alpha, deg - 1), 1 - alpha))
#
#
# def get_points(base_points, count):
#     alpha = 1 / count
#     res = []
#     for i in range(count):
#         res.append(get_point(base_points, i * alpha))
#     return res
#
#
# def get_knot(points, count):
#     if len(points) < 3:
#         return []
#     res = []
#     for i in range(-2, len(points) - 2):
#         ptn = []
#         ptn.append(mul(add(points[i], points[i + 1]), 0.5))
#         ptn.append(points[i + 1])
#         ptn.append(mul(add(points[i + 1], points[i + 2]), 0.5))
#
#         res.extend(get_points(ptn, count))
#     return res
#
#
# def set_points(points, speeds):
#     """функция перерасчета координат опорных точек"""
#     for p in range(len(points)):
#         points[p] = add(points[p], speeds[p])
#         if points[p][0] > SCREEN_DIM[0] or points[p][0] < 0:
#             speeds[p] = (- speeds[p][0], speeds[p][1])
#         if points[p][1] > SCREEN_DIM[1] or points[p][1] < 0:
#             speeds[p] = (speeds[p][0], -speeds[p][1])
#
#
# # =======================================================================================
# # Основная программа
# # =======================================================================================
# if __name__ == "__main__":
#     pygame.init()
#     gameDisplay = pygame.display.set_mode(SCREEN_DIM)
#     pygame.display.set_caption("MyScreenSaver")
#
#     steps = 35
#     working = True
#     points = []
#     speeds = []
#     show_help = False
#     pause = True
#
#     hue = 0
#     color = pygame.Color(0)
#
#     while working:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 working = False
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_ESCAPE:
#                     working = False
#                 if event.key == pygame.K_r:
#                     points = []
#                     speeds = []
#                 if event.key == pygame.K_p:
#                     pause = not pause
#                 if event.key == pygame.K_KP_PLUS:
#                     steps += 1
#                 if event.key == pygame.K_F1:
#                     show_help = not show_help
#                 if event.key == pygame.K_KP_MINUS:
#                     steps -= 1 if steps > 1 else 0
#
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 points.append(event.pos)
#                 speeds.append((random.random() * 2, random.random() * 2))
#
#         gameDisplay.fill((0, 0, 0))
#         hue = (hue + 1) % 360
#         color.hsla = (hue, 100, 50, 100)
#         draw_points(points)
#         draw_points(get_knot(points, steps), "line", 3, color)
#         if not pause:
#             set_points(points, speeds)
#         if show_help:
#             draw_help()
#
#         pygame.display.flip()
#
#     pygame.display.quit()
#     pygame.quit()
#     exit(0)

#################################################################################################################

# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import random

SCREEN_DIM = (800, 600)


class Vec2d:
    def __init__(self, x_or_pair, y=None):
        if y is None and type(x_or_pair) == tuple:
            self.x = x_or_pair[0]
            self.y = x_or_pair[1]
        else:
            self.x = x_or_pair
            self.y = y

    def __add__(self, other):
        return self.x + other.x, self.y + other.y

    def __sub__(self, other):
        return self.x - other.x, self.y - other.y

    def __mul__(self, k):
        return self.x * k.x, self.y * k.x

    @staticmethod
    def len(x, y):
        return (x ** 2 + y ** 2) ** 0.5

    def int_pair(self):
        return (int(self.x), int(self.y))


class Polyline:
    def __init__(self):
        self.points = []
        self.speeds = []
        self.factor_speed = 1

    def add_point(self, point, speed):
        self.points.append(point)
        self.speeds.append(Vec2d(speed) * Vec2d(self.factor_speed))

    def del_point(self):
        if len(self.points):
            self.points.pop()
            self.speeds.pop()

    def change_speed(self, k):
        if k > 1 and self.factor_speed < 6:
            self.factor_speed *= k
        elif k < 1 and self.factor_speed > 0.17:
            self.factor_speed *= k
        if 0.17 < self.factor_speed < 6:
            self.speeds = list(map(lambda pair: Vec2d(pair) *
                                   Vec2d(k), self.speeds))

    def set_points(self):
        for p in range(len(self.points)):
            self.points[p] = Vec2d(self.points[p]) + Vec2d(self.speeds[p])
            if self.points[p][0] > SCREEN_DIM[0] or self.points[p][0] < 0:
                self.speeds[p] = (- self.speeds[p][0], self.speeds[p][1])
            if self.points[p][1] > SCREEN_DIM[1] or self.points[p][1] < 0:
                self.speeds[p] = (self.speeds[p][0], -self.speeds[p][1])

    def draw_points(self, points, width=3, color=(255, 255, 255)):
        for p in points:
            pygame.draw.circle(gameDisplay, color,
                               Vec2d(p).int_pair(), width)


class Knot(Polyline):
    # def __init__(self):
    #     # super().__init__()
    count = 35

    def add_point(self, point, speed):
        super().add_point(point, speed)
        self.get_knot()

    def del_point(self):
        super().del_point()
        self.get_knot()

    def change_speed(self, k):
        super().change_speed(k)
        self.get_knot()

    def get_point(self, points, alpha, deg=None):
        if deg is None:
            deg = len(points) - 1
        if deg == 0:
            return points[0]
        return Vec2d(Vec2d(points[deg]) * Vec2d(alpha)) + Vec2d(
            Vec2d(self.get_point(points, alpha, deg - 1)) * Vec2d(1 - alpha))

    def get_points(self, base_points):
        alpha = 1 / self.count
        res = []
        for i in range(self.count):
            res.append(self.get_point(base_points, i * alpha))
        return res

    def get_knot(self):
        if len(self.points) < 3:
            return []
        res = []
        for i in range(-2, len(self.points) - 2):
            ptn = []
            ptn.append(Vec2d(Vec2d(self.points[i]) +
                             Vec2d(self.points[i + 1])) * Vec2d(0.5))
            ptn.append(self.points[i + 1])
            ptn.append(Vec2d(Vec2d(self.points[i + 1]) +
                             Vec2d(self.points[i + 2])) * Vec2d(0.5))
            res.extend(self.get_points(ptn))
        return res

    def draw_points(self, points, width=3, color=(255, 255, 255)):
        for p_n in range(-1, len(points) - 1):
            pygame.draw.line(gameDisplay, color,
                             Vec2d(points[p_n]).int_pair(),
                             Vec2d(points[p_n + 1]).int_pair(), width)


def draw_help():
    gameDisplay.fill((50, 50, 50))
    font1 = pygame.font.SysFont("courier", 24)
    font2 = pygame.font.SysFont("serif", 24)
    data = []
    data.append(["Сommon", ""])
    data.append(["F1", "Show Help"])
    data.append(["R", "Restart"])
    data.append(["P", "Pause/Play (in pause the screens are separate)"])
    data.append(["Q", "First/Second (key toggle screens)"])
    data.append(["", ""])
    data.append([screen_name, ""])
    data.append([str(steps), "Current points"])
    data.append(["Num+", "More points"])
    data.append(["Num-", "Less points"])
    data.append(["", ""])
    data.append([str(round(speed, 2)), "Current speed"])
    data.append(["Num8", "Speed is higher"])
    data.append(["Num2", "Speed is lower"])
    data.append(["", ""])
    data.append(["DELETE", "Delete supporting point"])

    pygame.draw.lines(gameDisplay, (255, 50, 50, 255), True, [
        (0, 0), (800, 0), (800, 600), (0, 600)], 5)
    for i, text in enumerate(data):
        gameDisplay.blit(font1.render(
            text[0], True, (128, 128, 255)), (100, 50 + 30 * i))
        gameDisplay.blit(font2.render(
            text[1], True, (128, 128, 255)), (230, 50 + 30 * i))


if __name__ == "__main__":
    pygame.init()
    gameDisplay = pygame.display.set_mode(SCREEN_DIM)
    pygame.display.set_caption("MyScreenSaver")

    working = True
    show_help = False
    pause = True
    screen = True

    polyline_1, knot_1 = Polyline(), Knot()
    polyline_2, knot_2 = Polyline(), Knot()

    hue = 0
    color = pygame.Color(0)

    while working:

        if screen:
            knot = knot_1
            steps, change_speed = knot_1.count, knot_1.change_speed
            screen_name, speed = 'First screen', polyline_1.factor_speed
        else:
            knot = knot_2
            steps, change_speed = knot_2.count, knot_2.change_speed
            screen_name, speed = 'Second screen', polyline_2.factor_speed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                working = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    working = False
                if event.key == pygame.K_F1:
                    show_help = not show_help
                if event.key == pygame.K_r:
                    polyline_1, knot_1 = Polyline(), Knot()
                    polyline_2, knot_2 = Polyline(), Knot()
                if event.key == pygame.K_p:
                    pause = not pause
                if event.key == pygame.K_KP_PLUS:
                    steps += 1
                if event.key == pygame.K_KP_MINUS:
                    steps -= 1 if steps > 1 else 0
                if event.key == pygame.K_DELETE:
                    # polyline.del_point()
                    knot.del_point()
                if event.key == pygame.K_q:
                    screen = not screen
                if event.key == pygame.K_KP8:
                    # polyline.change_speed(1.2)
                    knot.change_speed(1.2)
                if event.key == pygame.K_KP2:
                    # polyline.change_speed(0.83333)
                    knot.change_speed(0.83333)

            if event.type == pygame.MOUSEBUTTONDOWN:
                # polyline.add_point(event.pos, (random.random() * 2,
                #                                random.random() * 2))
                knot.add_point(event.pos, (random.random() * 2,
                                           random.random() * 2))

        gameDisplay.fill((0, 0, 0))
        hue = (hue + 1) % 360
        color.hsla = (hue, 100, 50, 100)
        if not pause or screen:
            polyline_1.draw_points(knot_1.points)
            knot_1.draw_points(knot_1.get_knot(), 3, color)
        if not pause or not screen:
            polyline_2.draw_points(knot_2.points)
            knot_2.draw_points(knot_2.get_knot(), 3, color)
        knot.count = steps
        if not pause:
            # polyline_1.set_points()
            knot_1.set_points()
            # polyline_2.set_points()
            knot_2.set_points()
        if show_help:
            draw_help()

        pygame.display.flip()

    pygame.display.quit()
    pygame.quit()
    exit(0)

######################################################################################################################
#
# import pygame
# import random
# import math
#
# SCREEN_DIM = (800, 600)
#
#
# class Vec2d:
#     def __init__(self, x_or_pair, y=None):
#         if y is None:
#             self.x = x_or_pair[0]
#             self.y = x_or_pair[1]
#         else:
#             self.x = x_or_pair
#             self.y = y
#
#     def __add__(self, vec):
#         return Vec2d(self.x + vec.x, self.y + vec.y)
#
#     def __sub__(self, vec):
#         return Vec2d(self.x - vec.x, self.y - vec.y)
#
#     def __mul__(self, k):
#         if isinstance(k, Vec2d):
#             return self.x * k.x + self.y * k.y
#         return Vec2d(self.x * k, self.y * k)
#
#     def len(self, x):
#         return (x.x ** 2 + x.y ** 2) ** .5
#
#     def int_pair(self):
#         return (int(self.x), int(self.y))
#
#
# class Polyline:
#     def __init__(self):
#         self.points = []
#         self.speeds = []
#
#     def add_point(self, point, speed):
#         self.points.append(point)
#         self.speeds.append(speed)
#
#     def set_points(self):
#         for i in range(len(self.points)):
#             self.points[i] += self.speeds[i]
#             if self.points[i].x > SCREEN_DIM[0] or self.points[i].x < 0:
#                 self.speeds[i] = Vec2d(- self.speeds[i].x, self.speeds[i].y)
#             if self.points[i].y > SCREEN_DIM[1] or self.points[i].y < 0:
#                 self.speeds[i] = Vec2d(self.speeds[i].x, -self.speeds[i].y)
#
#     def draw_points(self, points, width=3, color=(255, 255, 255)):
#         for point in points:
#             pygame.draw.circle(gameDisplay, color, point.int_pair(), width)
#
#
# class Knot(Polyline):
#     def __init__(self, count):
#         super().__init__()
#         self.count = count
#
#     def add_point(self, point, speed):
#         super().add_point(point, speed)
#         self.get_knot()
#
#     def set_points(self):
#         super().set_points()
#         self.get_knot()
#
#     def get_point(self, points, alpha, deg=None):
#         if deg is None:
#             deg = len(points) - 1
#         if deg == 0:
#             return points[0]
#         return points[deg] * alpha + self.get_point(points, alpha, deg - 1) * (1 - alpha)
#
#     def get_points(self, base_points):
#         alpha = 1 / self.count
#         res = []
#         for i in range(self.count):
#             res.append(self.get_point(base_points, i * alpha))
#         return res
#
#     def get_knot(self):
#         if len(self.points) < 3:
#             return []
#         res = []
#         for i in range(-2, len(self.points) - 2):
#             ptn = []
#             ptn.append((self.points[i] + self.points[i + 1]) * 0.5)
#             ptn.append(self.points[i + 1])
#             ptn.append((self.points[i + 1] + self.points[i + 2]) * 0.5)
#             res.extend(self.get_points(ptn))
#         return res
#
#     def draw_points(self, points, width=3, color=(255, 255, 255)):
#         for p_n in range(-1, len(points) - 1):
#             pygame.draw.line(gameDisplay, color, points[p_n].int_pair(), points[p_n + 1].int_pair(), width)
#
#
# def draw_help():
#     gameDisplay.fill((50, 50, 50))
#     font1 = pygame.font.SysFont("courier", 24)
#     font2 = pygame.font.SysFont("serif", 24)
#     data = []
#     data.append(["F1", "Show Help"])
#     data.append(["R", "Restart"])
#     data.append(["P", "Pause/Play"])
#     data.append(["Num+", "More points"])
#     data.append(["Num-", "Less points"])
#     data.append(["", ""])
#     data.append([str(steps), "Current points"])
#     pygame.draw.lines(gameDisplay, (255, 50, 50, 255), True, [
#         (0, 0), (800, 0), (800, 600), (0, 600)], 5)
#     for i, text in enumerate(data):
#         gameDisplay.blit(font1.render(
#             text[0], True, (128, 128, 255)), (100, 100 + 30 * i))
#         gameDisplay.blit(font2.render(
#             text[1], True, (128, 128, 255)), (200, 100 + 30 * i))
#
#
# if __name__ == "__main__":
#     pygame.init()
#     gameDisplay = pygame.display.set_mode(SCREEN_DIM)
#     pygame.display.set_caption("MyScreenSaver")
#     steps = 35
#     working = True
#     polyline = Polyline()
#     knot = Knot(steps)
#     show_help = False
#     pause = True
#     hue = 0
#     color = pygame.Color(0)
#     while working:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 working = False
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_ESCAPE:
#                     working = False
#                 if event.key == pygame.K_r:
#                     polyline = Polyline()
#                     knot = Knot(steps)
#                 if event.key == pygame.K_p:
#                     pause = not pause
#                 if event.key == pygame.K_KP_PLUS:
#                     steps += 1
#                 if event.key == pygame.K_F1:
#                     show_help = not show_help
#                 if event.key == pygame.K_KP_MINUS:
#                     steps -= 1 if steps > 1 else 0
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 polyline.add_point(Vec2d(event.pos), Vec2d(random.random() * 2, random.random() * 2))
#                 knot.add_point(Vec2d(event.pos), Vec2d(random.random() * 2, random.random() * 2))
#         gameDisplay.fill((0, 0, 0))
#         hue = (hue + 1) % 360
#         color.hsla = (hue, 100, 50, 100)
#         polyline.draw_points(polyline.points)
#         knot.draw_points(knot.get_knot(), 3, color)
#         if not pause:
#             polyline.set_points()
#             knot.set_points()
#         if show_help:
#             draw_help()
#         pygame.display.flip()
#     pygame.display.quit()
#     pygame.quit()
#     exit(0)
