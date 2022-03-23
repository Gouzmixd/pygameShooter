import pygame
import os

WIDTH,HEIGHT = 900,500
WIND = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("First Shooter")

BORDER= pygame.Rect(WIDTH/2 - 5, 0, 10, HEIGHT)

FPS = 60
VEL = 5

YELLOW_SPACESHIP_IMG = pygame.image.load(os.path.join('Assets','yellow_spaceship.png'))
YELLOW_SPACESHIP = pygame.transform.scale(YELLOW_SPACESHIP_IMG,(50,50))

RED_SPACESHIP_IMG = pygame.image.load(os.path.join('Assets','red_spaceship.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMG,(50,50)),180)

def draw_wind(red, yellow):
    WIND.fill((0,0,0))
    pygame.draw.rect(WIND,(255,255,255),BORDER)
    WIND.blit(YELLOW_SPACESHIP,(yellow.x,yellow.y))
    WIND.blit(RED_SPACESHIP,(red.x,red.y))
    pygame.display.update()

def move_red(red):
    if pygame.key.get_pressed()[pygame.K_UP] and red.y - VEL > 0:       #Red Spaceship goes up
        red.y -= VEL
    if pygame.key.get_pressed()[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT - 5:     #Red Spaceship goes down
        red.y += VEL
    if pygame.key.get_pressed()[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width:     #Red Spaceship goes left
        red.x -= VEL
    if pygame.key.get_pressed()[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH:    #Red Spaceship goes right
        red.x += VEL

def move_yellow(yellow):
    if pygame.key.get_pressed()[pygame.K_z] and yellow.y - VEL > 0:       #Yellow Spaceship goes up
        yellow.y -= VEL
    if pygame.key.get_pressed()[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT - 5:     #Yellow Spaceship goes down
        yellow.y += VEL
    if pygame.key.get_pressed()[pygame.K_q] and yellow.x - VEL > 0:     #Yellow Spaceship goes left
        yellow.x -= VEL
    if pygame.key.get_pressed()[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x:    #Yellow Spaceship goes right
        yellow.x += VEL

def main():
    red = pygame.Rect(700, 250, 50, 50)
    yellow = pygame.Rect(200, 250, 50, 50)

    clock = pygame.time.Clock()

    running = True
    
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False

        move_red(red)
        move_yellow(yellow)

        draw_wind(red, yellow)
    pygame.quit()

if __name__ == "__main__":
    main()