import pygame, pymunk
import random

cacti_sprites = [
    pygame.image.load('C:/MASTER FOLDER/wierd-dino/dino game/assets/dino/cactus_0.png'),
    pygame.image.load('C:/MASTER FOLDER/wierd-dino/dino game/assets/dino/cactus_1.png'),
    pygame.image.load('C:/MASTER FOLDER/wierd-dino/dino game/assets/dino/cactus_2.png'),
    pygame.image.load('C:/MASTER FOLDER/wierd-dino/dino game/assets/dino/big_cactus_1.png'),
    pygame.image.load('C:/MASTER FOLDER/wierd-dino/dino game/assets/dino/cacti_group_0.png'),
    pygame.image.load('C:/MASTER FOLDER/wierd-dino/dino game/assets/dino/cacti_group_1.png')
]

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, speed, mass, space):
        super().__init__()
        self.is_updating = True
        self.space = space
        self.mass = mass
        self.image = random.choice(cacti_sprites)
        self.rect = self.image.get_rect(bottomleft=(pos_x, pos_y))
        self.speed = speed

        self.rect.width -= 15

        self.shape = self.add_physics()

    def add_physics(self):
        body = pymunk.Body(self.mass, pymunk.moment_for_box(self.mass, self.rect.size), body_type=pymunk.Body.KINEMATIC)
        body.position = self.rect.center
        shape = pymunk.Poly.create_box(body, size=self.rect.size)
        shape.friction = 1.0
        shape.elasticity = 0.0
        shape.collision_type = 1
        self.space.add(body, shape)
        return shape

    def update(self):
        if self.is_updating:
            self.rect.x -= self.speed
            self.shape.body.position = (self.rect.centerx, self.rect.centery)
