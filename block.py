import pygame
import sys
import random
import time

pygame.init()

# constants:
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

FPS = 50

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

skier = pygame.Rect(SCREEN_WIDTH // 2, 500, 30, 30)

obstacles = [] # array for obstacles
# ---------------------

def move(keys): # move the block side to side
    if keys[pygame.K_LEFT] and skier.left > 0:
        skier.x -= 6
    if keys[pygame.K_RIGHT] and skier.right < 800:
        skier.x += 6

def generateObstacles(): # make the obstacles and populate the array
    x = random.randint(0, 750)

    if score < 300:
        theObstacle = pygame.Rect(x, -50, 50, 50)
        obstacles.append(theObstacle)

    if score > 300:
        theObstacle = pygame.Rect(x, -50, 60, 50)
        obstacles.append(theObstacle)

    if score > 1000:
        theObstacle = pygame.Rect(x, -50, 70, 50)
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

    screen.fill((0, 0, 0)) # green background

    pygame.draw.rect(screen, (57, 255, 20), skier) # draw player

    for obstacle in obstacles:
        pygame.draw.rect(screen, (128, 0, 128), obstacle)  # obstacles drawm

    
    font = pygame.font.Font(None, 36) # render text
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    fpsText = font.render(f"FPS: {"{:.2f}".format(FPS)}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    screen.blit(fpsText, (10, 40))

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

    obstacleCall = 1
    x = 2
    
    if score < 100:
        if spawn_timer == 0:  # Generate obstacles based on 30 frames
            generateObstacles()
    else:
        if spawn_timer == 0:  
            if score < 300:
                generateObstacles()
            elif score > 300:
                generateObstacles()
                generateObstacles()
            elif score > 1000:
                generateObstacles()
                generateObstacles()

        if score % 100 == 0:
            
            FPS += .025
            
        
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
