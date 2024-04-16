import pygame

#initiliasing pygame 
pygame.init()

# setting the secreen
screen = pygame.display.set_mode((800,600))

#setting the title for window
pygame.display.set_caption("First Game")

# setting the icon of the window
# logo = pygame.image.load("tempPython\space-invader.png")
logo = pygame.image.load("space-invaders (1).png").convert()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
    