import pygame
import time
import random
import sys
   
pygame.init()
   
intro = True
  
WIDTH = 800
HEIGHT = 600
   
BLACK = (0,0,0)
WHITE = (255,255,255)
RED_B = (255,0,0)
GREEN_B = (0,255,0)
YELLOW = (255,255,0)
BLUE_B = (0,0,255)
RED = (200,0,0)
BLUE = (0,0,200)
GREEN = (0,200,0)
  
  
middle_line_pos = [0, HEIGHT/2]
  
player_size = 46
player_pos = [WIDTH/2-player_size/2, HEIGHT-2*player_size]
player_x = player_pos[0]
player_y = player_pos[1]
  
enemy_size = 46
enemy_pos = [random.randint(0, WIDTH-enemy_size), 0]
enemy_list = [enemy_pos]
  
  
game_over = False
  
SCORE = 0
SPEED = 10
  
myFont = pygame.font.SysFont("monospace", 35)
  
   
gameDisplay = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Уклоняйтесь от блоков')
clock = pygame.time.Clock()
  
   
  
def set_level(SCORE, SPEED):
  
    SPEED = SCORE/15 + 5
  
    return SPEED
  
  
def drop_enemies(enemy_list):
    delay = random.random()
    if len(enemy_list) < 10 and delay < 0.1:
        x_pos = random.randint(0, WIDTH-enemy_size)
        y_pos = 0
        enemy_list.append([x_pos, y_pos])
  
  
def draw_enemies(enemy_list):
    for enemy_pos in enemy_list:
        pygame.draw.rect(gameDisplay, BLACK, (enemy_pos[0]-2, enemy_pos[1]-2, 50, 50))
        pygame.draw.rect(gameDisplay, RED, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))
  
  
def update_enemy_positions(enemy_list, SCORE, SPEED, player_pos_y, enemy_List):
    for idx, enemy_pos in enumerate(enemy_List):
        if enemy_pos[1] >= 0 and enemy_pos[1] < HEIGHT:
            enemy_pos[1] += SPEED
        else:
            if player_pos_y < HEIGHT/2:
                SCORE += 2
  
            else:
                SCORE += 1
            enemy_List.pop(idx)
    return SCORE, enemy_List
  
def detect_collision(player_pos, enemy_pos):
  
    p_x = player_pos[0]
    p_y = player_pos[1]
    e_x = enemy_pos[0]
    e_y = enemy_pos[1]
  
    if ((e_x >= p_x and e_x <= (p_x + player_size)) or (p_x >= e_x and p_x <= (e_x + enemy_size))):
        if (e_y >= p_y and e_y <= (p_y + player_size) or (p_y >= e_y and p_y <= (e_y + enemy_size))):
            return True
    return False
  
def collision_check(enemy_list, player_pos):
    for enemy_pos in enemy_list:
        if detect_collision(enemy_pos, player_pos):
            return True
    return False
  
def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()
   
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',75)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((HEIGHT/2),(WIDTH/2))
    gameDisplay.blit(TextSurf, TextRect)
   
    pygame.display.update()
   
    time.sleep(2)
   
    pygame.quit()
    quit()
def button(msg,x,y,w,h,ic,ac,action=None):
      
    mouse = pygame.mouse.get_pos()
  
    click = pygame.mouse.get_pressed()
  
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
  
            if action == "play":
                game_loop()
            elif action == "quit":
                pygame.quit()
                quit()
  
def game_intro():
  
    intro = True
  
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                  
        gameDisplay.fill(BLUE)
        largeText = pygame.font.Font('freesansbold.ttf',60)
        TextSurf, TextRect = text_objects("Уклоняйтесь от блоков)", largeText)
        TextRect.center = ((WIDTH/2),(HEIGHT/4))
        gameDisplay.blit(TextSurf, TextRect)
  
        mouse = pygame.mouse.get_pos()
        if 150+150 > mouse[0] > 125 and 350+50 > mouse[1] > 350:
            pygame.draw.rect(gameDisplay, GREEN_B,(125,350,150,50))
        else:
             pygame.draw.rect(gameDisplay, GREEN,(125,350,150,50))
        if 150+525 > mouse[0] > 525 and 350+50 > mouse[1] > 350:
            pygame.draw.rect(gameDisplay, RED_B,(525,350,150,50))
        else:
            pygame.draw.rect(gameDisplay, RED,(525,350,150,50))
  
        button("Singleplayer", 125, 350, 150, 50, GREEN, GREEN_B, "play")
        button("Multiplayer", 525, 350, 150, 50, RED, RED_B, "quit")
  
        smallText = pygame.font.Font("freesansbold.ttf",20)
        textSurf, textRect = text_objects("Singleplayer", smallText)
        textRect.center = ( (150+(100/2)), (350+(50/2)) )
        gameDisplay.blit(textSurf, textRect)
  
        smallText = pygame.font.Font("freesansbold.ttf",20)
        textSurf, textRect = text_objects("Multiplayer", smallText)
        textRect.center = ( (75+(525)), (350+(50/2)) )
        gameDisplay.blit(textSurf, textRect)
  
  
        pygame.display.update()
        clock.tick(15)
  
def game_loop():
  
    game = True
  
    middle_line_pos = [0, HEIGHT/2]
  
    player_size = 46
    player_pos = [WIDTH/2-player_size/2, HEIGHT-2*player_size]
    player_x = player_pos[0]
    player_y = player_pos[1]
  
    enemy_size = 46
    enemy_pos = [random.randint(0, WIDTH-enemy_size), 0]
    enemy_list = [enemy_pos]
     
    SPEED = 5
  
    SCORE = 0
  
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
  
            if event.type == pygame.KEYDOWN:
  
                x = player_pos[0]
                y = player_pos[1]
  
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    x -= player_size
  
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    x += player_size
  
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    y -= player_size
  
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    y += player_size
  
                player_pos = [x, y]
  
  
        gameDisplay.fill(WHITE)
  
        if detect_collision(player_pos, enemy_pos):
  
            message_display('Game Over!')
  
        elif (player_pos[0] < 0) or (player_pos[0] > WIDTH-player_size) or (player_pos[1] < 0) or (player_pos[1] > HEIGHT-player_size):
  
            message_display('Game Over!')
  
        drop_enemies(enemy_list)
  
        output = update_enemy_positions(enemy_list, SCORE, SPEED, player_pos[1], enemy_list)
        SCORE = output[0]
        enemy_list = output[1]
  
        SPEED = set_level(SCORE, SPEED)
  
  
        text = "Счёт:" + " " + str(SCORE)
        label = myFont.render(text, 1, BLACK)
        gameDisplay.blit(label, (WIDTH-200, HEIGHT-40))
  
  
        if collision_check(enemy_list, player_pos):
            message_display('Game Over!')
  
        draw_enemies(enemy_list)
  
        pygame.draw.rect(gameDisplay, BLACK, (player_pos[0]-2, player_pos[1]-2, 50, 50))
        pygame.draw.rect(gameDisplay, GREEN, (player_pos[0], player_pos[1], player_size, player_size))
        pygame.draw.rect(gameDisplay, BLUE, (middle_line_pos[0], middle_line_pos[1], WIDTH, 2))
  
        clock.tick(30)
  
        pygame.display.update()
  
game_intro()
  
pygame.quit()
quit()
