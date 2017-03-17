# Imports//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
import pygame
import math

# Initialize game engine///////////////////////////////////////////////////////////////////////////////////////////////////////////////
pygame.init()


# Window//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
HEIGHT = 700
WIDTH = 1300
SIZE = (WIDTH, HEIGHT)
TITLE = "MAZE"

pygame.display.set_caption(TITLE)
screen = pygame.display.set_mode(SIZE)

# Timer//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
clock = pygame.time.Clock()
refresh_rate = 60


# maze image to be deleted later*****************************************************************************************************
maze = pygame.image.load("mazeDiagram.jpg")
maze = pygame.transform.scale(maze, [WIDTH, HEIGHT])


# Colors//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
GRAY = (191, 191, 191)
GREEN = (0, 51, 0)
BLACK = (0, 0, 0)
CREAM = (153, 102, 51)

    
# walls man//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
wall1 = [0, 0, 25, 700]
wall2 = [0, 0, 1300, 25]
wall3 = [0, 675, 1300, 25]
wall4 = [1275, 0, 25, 325]
wall5 = [1275, 350, 25, 325]
wall6 = [50, 50, 25, 600]
wall7 = [75, 350, 200, 25]
wall8 = [75, 50, 275, 25]
wall9 = [75, 625, 275, 25]
wall10 = [350, 50, 25, 125]
wall11 = [100, 100, 25, 225]
wall12 = [125, 100, 200, 25]

walls = [wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9, wall10, wall11, wall12]




# Game loop/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    # Game logic (Check for collisions, update points, etc.)
     

    # Drawing code (Describe the picture. It isn't actually drawn yet.)
            # x, y, width, length

    # draw *************************************************************************************************************************
    screen.fill(GRAY)
    screen.blit(maze, (0, 0))   

    
    
    # grid   
    for y in range(0, HEIGHT, 25):
        pygame.draw.line(screen, BLACK, [0, y], [WIDTH, y])

    for x in range(0, WIDTH, 25):
        pygame.draw.line(screen, BLACK, [x, 0], [x, HEIGHT])


    # draw wall loop
    for w in walls:
        pygame.draw.rect(screen, GREEN, w)
    

    # Update window
    pygame.display.update()
    clock.tick(refresh_rate)


# Close window and quit//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
pygame.quit()
