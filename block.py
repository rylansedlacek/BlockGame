import pygame
import sys
import random
import time

pygame.init()

# constants:
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

skier = pygame.Rect(SCREEN_WIDTH // 2, 500, 50, 50)

obstacles = [] # array for obstacles
# ---------------------

def move(keys): # move the block side to side
    if keys[pygame.K_LEFT] and skier.left > 0:
        skier.x -= 5
    if keys[pygame.K_RIGHT] and skier.right < 800:
        skier.x += 5

def generateObstacles(): # make the obstacles and populate the array
    x = random.randint(0, 750)
    theObstacle = pygame.Rect(x, -50, 50, 50)
    obstacles.append(theObstacle)

def moveObstacles():
    for theObstacle in obstacles: # move em
        theObstacle.y += 5

    for theObstacle in obstacles[:]: # remove them once they go off screen 
        if theObstacle.top > SCREEN_HEIGHT:
            obstacles.remove(theObstacle)

def collisions(): # checking for collisions
    for obstacle in obstacles:
        if skier.colliderect(obstacle):
            return True
    return False


score = 0
def updateScore():
    global score
    for obstacle in obstacles:
        if obstacle.bottom > 600:
            score += 1

def draw_game():

    screen.fill((135, 206, 235)) # green background

    pygame.draw.rect(screen, (0, 128, 0), skier) # draw player

    for obstacle in obstacles:
        pygame.draw.rect(screen, (123, 128, 125), obstacle)  # obstacles drawm

    
    font = pygame.font.Font(None, 36) # render text
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

# game loop

spawn_timer = 0

while True:
    for event in pygame.event.get(): # quit check simple
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    keys = pygame.key.get_pressed() # press a key call move
    move(keys)

    
    if spawn_timer == 0: # generate obstacles based on 30 frames
        generateObstacles()
    spawn_timer = (spawn_timer + 1) % 30  

    moveObstacles() # move them around
    if collisions(): # check for any collisions
        
        time.sleep(3)
        print(f"Final Score: {score}")
        pygame.quit()
        sys.exit()

    updateScore()
    draw_game()
    clock.tick(FPS)

#-----------------------
