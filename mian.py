import pygame
import os
import random
import sys

pygame.init()
(width, height) = 750, 698
screen = pygame.display.set_mode((width, height))
screen.fill((0, 0, 0))
clock = pygame.time.Clock();
running = False


def load_image(name, colorkey=None):
    fullname = os.path.join('dist', name)
    image = pygame.image.load(fullname)
    image = image.convert_alpha()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    fon = pygame.transform.scale(load_image('kafk.png'), (width, height))
    screen.blit(fon, (0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return True
        pygame.display.flip()
        clock.tick(50)


def end_screen():
    fon = pygame.transform.scale(load_image('game over.jpg'), (width, height))
    screen.blit(fon, (0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return True
        pygame.display.flip()
        clock.tick(50)


def load_level(filename):
    filename = 'dist/' + filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    max_width = max(map(len, level_map))
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


tile_images = {
    'wall': load_image('box.png'),
    'empty': load_image('grass.png'),
    'helper': pygame.transform.scale(load_image('helper.png'), (50, 50)),
    'bomb': pygame.transform.scale(load_image("bomb.png"), (50, 50)),
    'trash': pygame.transform.scale(load_image("trash.png"), (50, 50)),
    'mush': pygame.transform.scale(load_image("mushroom.png"), (50, 50)),
    'ship': pygame.transform.scale(load_image("ship.png"), (50, 50)),
    'bye': pygame.transform.scale(load_image("finish.png"), (50, 50)),
    'wel': pygame.transform.scale(load_image("welcome.png"), (50, 50)),
}
player_positions = [pygame.transform.scale(load_image('marup.png'), (40, 50)),
                    pygame.transform.scale(load_image('marr.png'), (40, 50)),
                    pygame.transform.scale(load_image('mard.png'), (40, 50)),
                    pygame.transform.scale(load_image('marl.png'), (40, 50))]
i = 0
player_image = player_positions[-0]
tile_width = tile_height = 50


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)

    def remember(self):
        self.back = self.rect.copy()

    def update(self, dx, dy):
        self.rect = self.rect.move(dx, dy)

    def update2(self):
        self.rect = self.back


class Box(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(boxes_group, all_sprites)
        self.add(prep_group)
        self.image = tile_images[tile_type]
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)

    def remember(self):
        self.back = self.rect.copy()

    def update(self, dx, dy):
        self.rect = self.rect.move(dx, dy)

    def update2(self):
        self.rect = self.back


class Trash(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(trash_group, all_sprites)
        self.image = tile_images[tile_type]
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)

    def remember(self):
        self.back = self.rect.copy()

    def update(self, dx, dy):
        self.rect = self.rect.move(dx, dy)

    def update2(self):
        self.rect = self.back


class Mushroom(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(mushroom_group, all_sprites)
        self.image = tile_images[tile_type]
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)

    def remember(self):
        self.back = self.rect.copy()

    def update(self, dx, dy):
        self.rect = self.rect.move(dx, dy)

    def update2(self):
        self.rect = self.back


class Ship(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(ship_group, all_sprites)
        self.image = tile_images[tile_type]
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)

    def hide(self):
        self.image = pygame.transform.scale(load_image('grass.png'), (50, 50))

    def appear(self):
        self.image = pygame.transform.scale(load_image('ship.png'), (50, 50))

    def remember(self):
        self.back = self.rect.copy()

    def update(self, dx, dy):
        self.rect = self.rect.move(dx, dy)

    def update2(self):
        self.rect = self.back


class Finish(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(bye_group, all_sprites)
        self.image = tile_images[tile_type]
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)

    def hide(self):
        self.image = pygame.transform.scale(load_image('grass.png'), (50, 50))

    def appear(self):
        self.image = pygame.transform.scale(load_image('ship.png'), (50, 50))

    def remember(self):
        self.back = self.rect.copy()

    def update(self, dx, dy):
        self.rect = self.rect.move(dx, dy)

    def update2(self):
        self.rect = self.back


class Welcome(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(hi_group, all_sprites)
        self.image = tile_images[tile_type]
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)

    def hide(self):
        self.image = pygame.transform.scale(load_image('grass.png'), (50, 50))

    def appear(self):
        self.image = pygame.transform.scale(load_image('ship.png'), (50, 50))

    def remember(self):
        self.back = self.rect.copy()

    def update(self, dx, dy):
        self.rect = self.rect.move(dx, dy)

    def update2(self):
        self.rect = self.back


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image = player_image
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + 15, tile_height * pos_y + 5)


class Bomb(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(bomb_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + 15, tile_height * pos_y + 5)

    def remember(self):
        self.back = self.rect.copy()

    def update(self, dx, dy):
        self.rect = self.rect.move(dx, dy)

    def update2(self):
        self.rect = self.back


player = None
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
hi_group = pygame.sprite.Group()
bye_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
boxes_group = pygame.sprite.Group()
prep_group = pygame.sprite.Group()
helper_group = pygame.sprite.Group()
bomb_group = pygame.sprite.Group()
trash_group = pygame.sprite.Group()
explosion = pygame.sprite.Group()
mushroom_group = pygame.sprite.Group()
ship_group = pygame.sprite.Group()

flag = 0


def generate_level(level):
    new_player, h1, h2 = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == '#':
                Box('wall', x, y)
            elif level[y][x] == '@':
                Tile('empty', x, y)
                new_player = Player(x, y)
            elif level[y][x] == 'b':
                Tile('empty', x, y)
                Bomb('bomb', x, y)
            elif level[y][x] == 't':
                Tile('empty', x, y)
                Trash('trash', x, y)
            elif level[y][x] == 'm':
                Tile('empty', x, y)
                Mushroom('mush', x, y)
            elif level[y][x] == 's':
                Tile('empty', x, y)
                Ship('ship', x, y)
            elif level[y][x] == 'a':
                Tile('empty', x, y)
                Welcome('wel', x, y)
            elif level[y][x] == 'e':
                Tile('empty', x, y)
                Finish('bye', x, y)

    return new_player, h1, h2


class Camera:
    def __init__(self):
        self.dx = 0
        self.dy = 0

    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - width // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - height // 2)


def game():
    flag = 0
    i = 0
    start_screen()
    clock = pygame.time.Clock()
    health = 150
    l = load_level('labirinthard')
    camera = Camera()
    player, h1, h2 = generate_level(l)
    running = True
    s = 0
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if pygame.key.get_pressed()[273]:
            player.rect.y -= 5
            i = 0
        if pygame.sprite.spritecollideany(player, prep_group):
            player.rect.y += 5

        if pygame.key.get_pressed()[274]:
            player.rect.y += 5
            i = 2
        if pygame.sprite.spritecollideany(player, prep_group):
            player.rect.y -= 5

        if pygame.key.get_pressed()[275]:
            player.rect.x += 5
            i = 1
        if pygame.sprite.spritecollideany(player, prep_group):
            player.rect.x -= 5

        if pygame.key.get_pressed()[276]:
            player.rect.x -= 5
            i = 3
        if pygame.sprite.spritecollideany(player, prep_group):
            player.rect.x += 5

        if pygame.sprite.spritecollideany(player, bomb_group):
            for lu in bomb_group:
                if pygame.sprite.pygame.sprite.collide_mask(player, lu):
                    health = (health - 50) * (health - 50 >= 0) % 150
                    if health < 0:
                        health = 0
                    lu.image = load_image('boom.png')
                    lu.add(explosion)
                    bomb_group.remove_internal(lu)
        if pygame.sprite.spritecollideany(player, trash_group):
            for lu in trash_group:
                if pygame.sprite.pygame.sprite.collide_mask(player, lu):
                    health = 150
                    trash_group.remove_internal(lu)
        if pygame.sprite.spritecollideany(player, mushroom_group) or health <= 30:
            if flag == 0:
                all_sprites.rememder()
            all_sprites.update(random.randrange(3) - 1, random.randrange(3) - 1)
            flag += 1
        if flag >= 1 and not pygame.sprite.spritecollideany(player, ship_group):
            all_sprites.update2()
            flag = 0
        health -= 0.01
        player.image = player_positions[i]
        camera.update(player)
        for sprite in all_sprites:
            camera.apply(sprite)
        hi_group.draw(screen)
        bye_group.draw(screen)
        tiles_group.draw(screen)
        boxes_group.draw(screen)
        helper_group.draw(screen)
        bomb_group.draw(screen)
        trash_group.draw(screen)
        explosion.draw(screen)
        mushroom_group.draw(screen)
        if s < 500:
            ship_group.draw(screen)
            s += 1
        elif 500 <= s < 700:
            s += 1
        elif s == 700:
            s = 0
        if s < 500 and pygame.sprite.spritecollideany(player, ship_group):
            health = 0
        player_group.draw(screen)
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(player.rect.x + 200, player.rect.y - 300, health, 20))
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(player.rect.x + 200, player.rect.y - 300, 150, 20), 1)
        if (health <= 0) or (player.rect.x == 1 and player.rect.y == 1):
            if end_screen():
                if start_screen():
                    flag = None
                    i = None
                    clock = None
                    health = None
                    l = None
                    camera = None
                    player, h1, h2 = None, None, None
                    running = None
                    s = None
                    hi_group.empty()
                    bye_group.empty()
                    all_sprites.empty()
                    tiles_group.empty()
                    player_group.empty()
                    boxes_group.empty()
                    prep_group.empty()
                    helper_group.empty()
                    bomb_group.empty()
                    trash_group.empty()
                    explosion.empty()
                    mushroom_group.empty()
                    ship_group.empty()
                    game()
        pygame.display.flip()
        clock.tick(100)


game()

