import pygame
import collections
import Service
import os

colors = {
    "black": (0, 0, 0, 255),
    "white": (255, 255, 255, 255),
    "red": (255, 0, 0, 255),
    "green": (0, 255, 0, 255),
    "blue": (0, 0, 255, 255),
    "wooden": (153, 92, 0, 255),
}

MINI_MAP = False
class ScreenHandle(pygame.Surface):
    def __init__(self, *args, **kwargs):
        if len(args) > 1:
            self.successor = args[-1]
            self.next_coord = args[-2]
            args = args[:-2]
        else:
            self.successor = None
            self.next_coord = (0, 0)
        super().__init__(*args, **kwargs)
        self.fill(colors["wooden"])

    def draw(self, canvas):
        if self.successor is not None:
            canvas.blit(self.successor, self.next_coord)
            self.successor.draw(canvas)


    def connect_engine(self, engine):
        if self.successor is not None:
            return self.successor.connect_engine(engine)


class GameSurface(ScreenHandle):
    # FIXME сохранить двигатель и отправить его следующему в цепочке +++++
    def connect_engine(self, engine):
        self.game_engine = engine
        if self.successor is not None:
            return self.successor.connect_engine(engine)

    def draw_hero(self):
        self.game_engine.hero.draw(self)




    def draw_map(self):
        global MINI_MAP
        # FIXME || calculate (min_x,min_y) - left top corner - вычислить (min_x,min_y) - левый верхний угол
        size = self.game_engine.sprite_size
        min_x = 0
        min_y = 0
        hero_pos = self.game_engine.hero.position
        min_x = int(hero_pos[0] - 480 / size) if hero_pos[0] - 480 / size > 0 else 0
        min_y = hero_pos[1] - 5 if hero_pos[1] - 5 > 0 else 0

    ##

        if self.game_engine.map:
            if MINI_MAP is False:
                for i in range(len(self.game_engine.map[0]) - min_x):
                    for j in range(len(self.game_engine.map) - min_y):
                        self.blit(self.game_engine.map[min_y + j][min_x + i][
                                  0], (i * size, j * size))
            else:

                for i in range(len(self.game_engine.map[0])):
                    for j in range(len(self.game_engine.map)):
                        self.blit(self.game_engine.map[j][i][
                                  0], (i * 7, j * 7))

        else:
            self.fill(colors["white"])

    def draw_object(self, sprite, coord):
        size = self.game_engine.sprite_size
    # FIXME || calculate (min_x,min_y) - left top corner

        min_x = 0
        min_y = 0
        hero_pos = self.game_engine.hero.position
        min_x = int(hero_pos[0] - 480 / size) if hero_pos[0] - 480 / size > 0 else 0
        min_y = hero_pos[1] - 5 if hero_pos[1] - 5 > 0 else 0

    ##
        if MINI_MAP is False:
            self.blit(sprite, ((coord[0] - min_x) * size,
                           (coord[1] - min_y) * size))
        else:
            self.blit(Service.create_sprite(os.path.join("texture", "Hero.png"), 10), ((coord[0]) * 7,
                           (coord[1]) * 7))


    def draw(self, canvas):
        size = self.game_engine.sprite_size
    # FIXME || calculate (min_x,min_y) - left top corner

        min_x = 0
        min_y = 0
        hero_pos = self.game_engine.hero.position
        min_x = int(hero_pos[0] - 480 / size) if hero_pos[0] - 480 / size > 0 else 0
        min_y = hero_pos[1] - 5 if hero_pos[1] - 5 > 0 else 0

    ##
        if MINI_MAP is False:
            Service.service_init(size, False)
            self.draw_map()
            for obj in self.game_engine.objects:
                self.blit(obj.sprite[0], ((obj.position[0] - min_x) * size,
                                          (obj.position[1] - min_y) * size))
        else:
            Service.service_init(11, False)
            self.draw_map()
            # print(self.game_engine.objects)
            for obj in self.game_engine.objects:
                self.blit(obj.sprite[0], ((obj.position[0]) * 7,
                                          (obj.position[1]) * 7))

        self.draw_hero()

    # draw next surface in chain - нарисовать следующую поверхность в цепочке
        if self.successor is not None:
            canvas.blit(self.successor, self.next_coord)
            return self.successor.draw(canvas)

class ProgressBar(ScreenHandle):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fill(colors["wooden"])

    # def connect_engine(self, engine):
        # FIXME save engine and send it to next in chain
    def connect_engine(self, engine):
        self.engine = engine
        if self.successor is not None:
            return self.successor.connect_engine(engine)

    def draw(self, canvas):
        self.fill(colors["wooden"])
        pygame.draw.rect(self, colors["black"], (50, 30, 200, 30), 2)
        pygame.draw.rect(self, colors["black"], (50, 70, 200, 30), 2)

        pygame.draw.rect(self, colors[
                         "red"], (50, 30, 200 * self.engine.hero.hp / self.engine.hero.max_hp, 30))
        pygame.draw.rect(self, colors["green"], (50, 70,
                                                 200 * self.engine.hero.exp / (100 * (2**(self.engine.hero.level - 1))), 30))

        font = pygame.font.SysFont("comicsansms", 20)
        self.blit(font.render(f'Hero at {self.engine.hero.position}', True, colors["black"]),
                  (250, 0))

        self.blit(font.render(f'{self.engine.level} floor', True, colors["black"]),
                  (10, 0))

        self.blit(font.render(f'HP', True, colors["black"]),
                  (10, 30))
        self.blit(font.render(f'Exp', True, colors["black"]),
                  (10, 70))

        self.blit(font.render(f'{self.engine.hero.hp}/{self.engine.hero.max_hp}', True, colors["black"]),
                  (60, 30))
        self.blit(font.render(f'{self.engine.hero.exp}/{(100*(2**(self.engine.hero.level-1)))}', True, colors["black"]),
                  (60, 70))

        self.blit(font.render(f'Level', True, colors["black"]),
                  (300, 30))
        self.blit(font.render(f'Gold', True, colors["black"]),
                  (300, 70))

        self.blit(font.render(f'{self.engine.hero.level}', True, colors["black"]),
                  (360, 30))
        self.blit(font.render(f'{self.engine.hero.gold}', True, colors["black"]),
                  (360, 70))

        self.blit(font.render(f'Str', True, colors["black"]),
                  (420, 30))
        self.blit(font.render(f'Luck', True, colors["black"]),
                  (420, 70))

        self.blit(font.render(f'{self.engine.hero.stats["strength"]}', True, colors["black"]),
                  (480, 30))
        self.blit(font.render(f'{self.engine.hero.stats["luck"]}', True, colors["black"]),
                  (480, 70))

        self.blit(font.render(f'SCORE', True, colors["black"]),
                  (550, 30))
        self.blit(font.render(f'{self.engine.score:.4f}', True, colors["black"]),
                  (550, 70))
        if self.successor is not None:
            canvas.blit(self.successor, self.next_coord)
            return self.successor.draw(canvas)
    # draw next surface in chain


class InfoWindow(ScreenHandle):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.len = 16
        clear = []
        self.data = collections.deque(clear, maxlen=self.len)

    def update(self, value):
        self.data.append(f"> {str(value)}")

    def draw(self, canvas):
        self.fill(colors["wooden"])
        size = self.get_size()

        font = pygame.font.SysFont("comicsansms", 10)
        for i, text in enumerate(self.data):
            self.blit(font.render(text, True, colors["black"]),
                      (5, 20 + 18 * i))

    # FIXME
    # draw next surface in chain
        if self.successor is not None:
            canvas.blit(self.successor, self.next_coord)
            return self.successor.draw(canvas)

    # def connect_engine(self, engine):
        # FIXME set this class as Observer to engine and send it to next in - установите этот класс как Observer для двигателя и отправьте его следующему в
        # chain - цепь
    def connect_engine(self, engine):
        self.engine = engine
        engine.subscribe(self)
        if self.successor is not None:
            return self.successor.connect_engine(engine)

class HelpWindow(ScreenHandle):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.len = 30
        clear = []
        self.data = collections.deque(clear, maxlen=self.len)
        self.data.append([" →", "Move Right"])
        self.data.append([" ←", "Move Left"])
        self.data.append([" ↑ ", "Move Top"])
        self.data.append([" ↓ ", "Move Bottom"])
        self.data.append([" H ", "Show Help"])
        self.data.append(["Num+", "Zoom +"])
        self.data.append(["Num-", "Zoom -"])
        self.data.append([" R ", "Restart Game"])
    # FIXME You can add some help information

    # def connect_engine(self, engine):
        # FIXME save engine and send it to next in chain
    def connect_engine(self, engine):
        self.engine = engine
        if self.successor is not None:
            return self.successor.connect_engine(engine)

    def draw(self, canvas):
        alpha = 0
        if self.engine.show_help:
            alpha = 128
        self.fill((0, 0, 0, alpha))
        size = self.get_size()
        font1 = pygame.font.SysFont("courier", 24)
        font2 = pygame.font.SysFont("serif", 24)
        if self.engine.show_help:
            pygame.draw.lines(self, (255, 0, 0, 255), True, [
                              (0, 0), (700, 0), (700, 500), (0, 500)], 5)
            for i, text in enumerate(self.data):
                self.blit(font1.render(text[0], True, ((128, 128, 255))),
                          (50, 50 + 30 * i))
                self.blit(font2.render(text[1], True, ((128, 128, 255))),
                          (150, 50 + 30 * i))
    # FIXME
    # draw next surface in chain
        if self.successor is not None:
            canvas.blit(self.successor, self.next_coord)
            return self.successor.draw(canvas)