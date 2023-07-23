import pygame
import os

# WINDOW
WIDTH, HEIGHT = 1700, 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Brawler")


# VARIABLE
WHITE = (255, 255, 255)
FPS = 60
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 110, 80

#IMAGES
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets","spaceship_yellow.png"))
YELLOW_SPACESHIP = pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets","spaceship_red.png"))
RED_SPACESHIP = pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
BACKGROUND_IMAGE = pygame.image.load(os.path.join("Assets", "space.png"))

# FUNCTION
def draw_window():
    WIN.fill(WHITE)
    WIN.blit(BACKGROUND_IMAGE, (0, 0))
    WIN.blit(YELLOW_SPACESHIP, (300, 100))
    WIN.blit(RED_SPACESHIP, (300, 300))
     
    pygame.display.update()
    
def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        draw_window()

   
    pygame.quit()
    
if __name__ == "__main__":
    main()