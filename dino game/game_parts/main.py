import pygame, pymunk
import random
from dino import Dino
from obstacle import Obstacle
from cloud import Cloud
from ground import Ground
from bird import Bird
from game_manager import GameManager

pygame.init()

# Screen stats
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Weird Dino")

dead_dino_sprite = pygame.image.load('C:/MASTER FOLDER/wierd-dino/dino game/assets/dino/hurt_dino.png')

# Colors
WHITE = (255, 255, 255)

def main():
    run = True
    clock = pygame.time.Clock()

    moving_sprites = pygame.sprite.Group()
    obstacles = pygame.sprite.Group()
    cloud_list = pygame.sprite.Group()
    birds = pygame.sprite.Group()
    ground = Ground()

    # variables
    jump_force = 15
    dx = 0.2
    game_speed = 10

    dino = Dino(100, 100, moving_sprites, HEIGHT)
    moving_sprites.add(dino)

    obstacle_spawned = False

    game_manager = GameManager(dino, obstacles, cloud_list, birds, moving_sprites, obstacle_spawned, WIDTH, HEIGHT)

    BIRD_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(BIRD_EVENT, 15000)

    while run:
        clock.tick(60)
        WIN.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    dino.jump(jump_force)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if game_manager.restart_button_clicked(mouse_pos):
                    game_manager.reset_game_state()
            elif event.type == BIRD_EVENT: 
                new_bird = Bird(WIDTH, 460)
                birds.add(new_bird)

        # Draw ground
        ground.draw(WIN)

        # Update and draw sprites and gameover logic
        if dino.collided_with_obstacle or dino.collided_with_bird:
            WIN.blit(dead_dino_sprite, dino.rect)
            game_manager.show_game_over(WIN)
        else:
            moving_sprites.update(dx)
            dino.animate()
            moving_sprites.draw(WIN)

        # Obstacle logic
        if not game_manager.obstacle_spawned:
            obstacle = Obstacle(WIDTH, HEIGHT - ground.height + 20, game_speed)
            obstacles.add(obstacle)
            game_manager.obstacle_spawned = True
        obstacles.update()
        obstacles.draw(WIN)
        if obstacle.rect.x + 50 < 0:
            obstacles.remove(obstacle)
            game_manager.obstacle_spawned = False

        # Cloud logic
        if not dino.collided_with_obstacle and not dino.collided_with_bird:
            cloud = Cloud(WIDTH, random.randint(40, 100), game_speed)
            if random.randint(0, 100) < 3:
                cloud_list.add(cloud)
        cloud_list.update()
        cloud_list.draw(WIN)

        # Bird logic
        for bird in birds:
            bird.move(game_speed * 1.5)
            birds.update(dx)
            birds.draw(WIN)

        # Die logic
        dino.die(obstacles, cloud_list, birds)

        # Update the screen
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
