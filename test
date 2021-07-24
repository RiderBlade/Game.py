import pygame, time, math, random, sys
from pygame.locals import *

background = pygame.image.load("MarioBackground.png")

def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

W, H = 640, 400
HW, HH = W / 2, H / 2
AREA = W * H
FPS = 60
bg_x = 0
isJump = False
jumpCount = 10

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((W,H))
pygame.display.set_caption("Mario")

class Mario():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.rect(screen, (255,0,0), (self.x, self.y, 40, 40))

    def move(self):
        global bg_x
        if pressed_keys[K_RIGHT] and bg_x > -920:
            if self.x > 490:
                bg_x -= 5
            else:
                self.x += 5
        if pressed_keys[K_LEFT] and self.x > 5:
            self.x -= 5

    def jump(self):
        global jumpCount, isJump
        if pressed_keys[K_SPACE]:
            if jumpCount >= -10:
                isJump = True
                neg = 1
                if jumpCount < 0:
                    neg = -1
                self.y -= (jumpCount ** 2) * 0.1 * neg
                jumpCount -= 1
            else:
                isJump = False
                jumpCount = 10




mario = Mario(50, 270)

while True:
    clock.tick(FPS)
    events()
    pressed_keys = pygame.key.get_pressed()

    screen.blit(background, (bg_x,0))


    mario.move()
    mario.draw()
    mario.jump()



    pygame.display.update()
