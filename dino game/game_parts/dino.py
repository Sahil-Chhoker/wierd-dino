import pygame

dino_sprites = [
    pygame.image.load('C:/MASTER FOLDER/wierd-dino/dino game/assets/dino/dino_2.png'),
    pygame.image.load('C:/MASTER FOLDER/wierd-dino/dino game/assets/dino/dino_3.png')
]
dead_dino_sprite = pygame.image.load('C:/MASTER FOLDER/wierd-dino/dino game/assets/dino/hurt_dino.png')

class Dino(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, sprite_group, HEIGHT):
        super().__init__()
        self.is_animating = False
        self.current_sprite = 0
        self.image = dino_sprites[self.current_sprite]
        self.rect = self.image.get_rect(topleft=(pos_x, pos_y))
        self.vel_y = 0
        self.collided_with_obstacle = False
        self.collided_with_bird = False

        self.rect.width -= 10
        self.rect.height -= 10

        self.sprite_group = sprite_group
        self.sprite_group.add(self)

        self.HEIGHT = HEIGHT

    def jump(self, jump_force):
        if self.rect.bottom == self.HEIGHT - 36:
            self.vel_y = -jump_force

    def die(self, obstacles, cloud_list, birds):
        if not self.collided_with_obstacle:
            for obstacle in obstacles:
                collide = self.rect.colliderect(obstacle.rect)
                if collide:
                    self.collided_with_obstacle = True
                    obstacle.is_updating = False
                    for cloud in cloud_list:
                        cloud.is_updating = False
                    break
        
        if not self.collided_with_bird:
            for bird in birds:
                collide = self.rect.colliderect(bird.rect)
                if collide:
                    self.collided_with_bird = True
                    bird.is_moving = False
                    for cloud in cloud_list:
                        cloud.is_updating = False
                    for obstacle in obstacles:
                        obstacle.is_updating = False
                    break

    def animate(self):
        self.is_animating = True

    def update(self, dx):
        if self.is_animating:
            self.current_sprite += dx
            if self.current_sprite >= len(dino_sprites):
                self.current_sprite = 0
                self.is_animating = False
            self.image = dino_sprites[int(self.current_sprite)]

        # Apply gravity
        self.vel_y += 0.7
        self.rect.y += self.vel_y

        if self.rect.bottom >= self.HEIGHT - 36:
            self.rect.bottom = self.HEIGHT - 36
            self.vel_y = 0
