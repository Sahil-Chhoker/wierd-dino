import pygame

bird_sprites = [
    pygame.image.load('C:/MASTER FOLDER/GitHub/wierd-dino/dino game/assets/dino/bird_0.png'),
    pygame.image.load('C:/MASTER FOLDER/GitHub/wierd-dino/dino game/assets/dino/bird_1.png')
]

class Bird(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.is_moving = True
        self.is_animating = False
        self.current_sprite = 0
        self.image = bird_sprites[self.current_sprite]
        self.rect = self.image.get_rect(topleft=(pos_x, pos_y))

    def animate(self):
        self.is_animating = True

    def update(self, dx):
        if self.is_animating:
            self.current_sprite += dx
            if self.current_sprite >= len(bird_sprites):
                self.current_sprite = 0
            self.image = bird_sprites[int(self.current_sprite)]

    def move(self, speed):
        self.speed = speed
        if self.is_moving:
            self.rect.x -= self.speed
