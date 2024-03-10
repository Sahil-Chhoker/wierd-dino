import pygame

class GameManager:
    def __init__(self, dino, obstacles, cloud_list, moving_sprites, obstacle_spawned, WIDTH, HEIGHT):
        self.dino = dino
        self.obstacles = obstacles
        self.cloud_list = cloud_list
        self.moving_sprites = moving_sprites
        self.obstacle_spawned = obstacle_spawned
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT

        self.game_over_sprite = pygame.image.load('C:/MASTER FOLDER/wierd-dino/dino game/assets/dino/game_over.png')
        self.restart_button_sprite = pygame.image.load('C:/MASTER FOLDER/wierd-dino/dino game/assets/dino/restart.png')
        self.restart_button_rect = self.restart_button_sprite.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2 + 50))

    def show_game_over(self, window):
        window.blit(self.game_over_sprite, (self.WIDTH // 2 - self.game_over_sprite.get_width() // 2, self.HEIGHT // 2 - self.game_over_sprite.get_height() // 2))
        window.blit(self.restart_button_sprite, self.restart_button_rect)

    def restart_button_clicked(self, mouse_pos):
        return self.restart_button_rect.collidepoint(mouse_pos)
    
    def reset_game_state(self):
        self.game_over = False
        self.obstacle_spawned = False
        self.dino.rect.topleft = (100, 100)
        self.dino.collided_with_obstacle = False
        self.obstacles.empty()
        self.cloud_list.empty()
