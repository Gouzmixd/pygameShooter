import pygame
import os
pygame.font.init()

WIDTH,HEIGHT = 900,500
WIND = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("First Shooter")

BORDER= pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)

FPS = 60
VEL = 5

MAX_BULLETS = 4
BULL_VEL = 7

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

HEALTH_FONT = pygame.font.SysFont('comicsansms', 30)
WINNER_FONT = pygame.font.SysFont('comicsansms', 100)

YELLOW_SPACESHIP_IMG = pygame.image.load(os.path.join('Assets','yellow_spaceship.png'))
YELLOW_SPACESHIP = pygame.transform.scale(YELLOW_SPACESHIP_IMG,(50,50))

RED_SPACESHIP_IMG = pygame.image.load(os.path.join('Assets','red_spaceship.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMG,(50,50)),180)

def draw_wind(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    WIND.fill((0,0,0))
    pygame.draw.rect(WIND,(255,255,255),BORDER)

    red_health_text= HEALTH_FONT.render("Health: " + str(red_health), 1, (255,255,255))
    WIND.blit(red_health_text, (750,HEIGHT - 50))
    yellow_health_text= HEALTH_FONT.render("Health: " + str(yellow_health), 1, (255,255,255))
    WIND.blit(yellow_health_text, (10,HEIGHT - 50))

    WIND.blit(YELLOW_SPACESHIP,(yellow.x,yellow.y))
    WIND.blit(RED_SPACESHIP,(red.x,red.y))

    for bullet in red_bullets:
        pygame.draw.rect(WIND, (255,0,0), bullet)
    for bullet in yellow_bullets:
        pygame.draw.rect(WIND, (255,255,0), bullet)

    pygame.display.update()

def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, (255,255,255))
    WIND.blit(draw_text, (WIDTH//2 - draw_text.get_width()//2, HEIGHT//2 - draw_text.get_height()//2))
    pygame.display.update()
    pygame.time.delay(5000)

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

def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += BULL_VEL
        if red.colliderect(bullet):
            yellow_bullets.remove(bullet)
            pygame.event.post(pygame.event.Event(RED_HIT))
        if bullet.x > WIDTH:
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x -= BULL_VEL
        if yellow.colliderect(bullet):
            red_bullets.remove(bullet)
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
        if bullet.x < 0:
            red_bullets.remove(bullet)



def main():
    red = pygame.Rect(700, 250, 50, 50)
    yellow = pygame.Rect(200, 250, 50, 50)

    red_bullets = []
    yellow_bullets = []

    red_health = 10
    yellow_health = 10

    clock = pygame.time.Clock()

    running = True
    
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 + 2, 10, 5)
                    yellow_bullets.append(bullet)
                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + red.height//2 + 2, 10, 5)
                    red_bullets.append(bullet)
            if event.type == YELLOW_HIT:
                yellow_health -= 1
            if event.type == RED_HIT:
                red_health -= 1

        winner_text = ""
        if red_health <=0:
            winner_text= "Yellow wins !"
        if yellow_health <=0:
            winner_text= "Red wins !"
        if winner_text != "":
            draw_winner(winner_text)
            break
            
        

        move_red(red)
        move_yellow(yellow)

        handle_bullets(yellow_bullets, red_bullets, yellow, red)

        draw_wind(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health)
    main()

if __name__ == "__main__":
    while True:
        main()