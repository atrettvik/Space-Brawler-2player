import pygame
import os

# WINDOW
WIDTH, HEIGHT = 1000, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Brawler")


# VARIABLE
WHITE = (255, 255, 255)
FPS = 60
VEL = 5
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

#IMAGES
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets","spaceship_yellow.png"))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets","spaceship_red.png"))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

BACKGROUND_IMAGE = pygame.image.load(os.path.join("Assets", "space.png"))

# FUNCTION
def laser_shoot():
    

def draw_window(red, yellow):
    WIN.fill(WHITE)
    WIN.blit(BACKGROUND_IMAGE, (0, 0))
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
     
    pygame.display.update()
    
def main(): 
    
    red = pygame.Rect(800, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(200, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    
    
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
       
       
       # YELLOW_SHIP KEYS       
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_a]: # LEFT
            yellow.x -= VEL
        if keys_pressed[pygame.K_d]: # RIGHT
            yellow.x += VEL
        if keys_pressed[pygame.K_w]: # UP
            yellow.y -= VEL           
        if keys_pressed[pygame.K_s]: # DOWN
            yellow.y += VEL
         ## if keys_pressed[pygame.K_a]: # SHOOT
            
            
            
        draw_window(red, yellow)

   
    pygame.quit()
    
if __name__ == "__main__":
    main()