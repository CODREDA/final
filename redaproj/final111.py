import pygame
import pdb
from random import randint
pygame.init()

pygame.mixer.music.load('music/totztot.mp3')
pygame.mixer.music.play(5)

win = pygame.display.set_mode((500,480))

pygame.display.set_caption("First Game")

char = pygame.image.load('reda.png')
char=pygame.transform.scale(char,(70,70))

walkRight = [char]
walkLeft = [char]

bg = pygame.image.load('bg.jpg')

char2 = pygame.image.load('garbage.png')
char2=pygame.transform.scale(char2,(40,40))

clock = pygame.time.Clock()
x = 250
y = 400
restart = 0
vel = 10
isJump = False
jumpCount = 10
left = False
right = False
walkCount = 0
lteht = 0
jnab = randint(0, 430)
count=0
zgel = 0

myfont = pygame.font.SysFont("monospace", 15)

label = myfont.render(str(count), 1, (0,0,0))

def redrawGameWindow():
    global walkCount, lteht, jnab, label
    win.blit(bg, (0,0))

    if zgel == 4:
        win.blit(label, (250, 200))
        label = myfont.render("Game Over", 1, (0,0,0))
        
    else:
        label = myfont.render(str(count), 1, (255,255,0))
        win.blit(label, (0, 0))
    
    
    lteht = lteht + 10
    if lteht > 500:
        lteht = 0
        jnab = randint(0, 430)
                        
    win.blit(char2, (jnab,lteht))
                        
    if walkCount + 1 >= 3:
        walkCount = 0

    if left:
        win.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount//3], (x,y))
        walkCount +=1
    else:
        win.blit(char, (x,y))
    
    pygame.display.update()

def gameOverWindow():
    win.blit(bg, (x,y))
    pygame.display.update()
    

#mainloop

def mainLoop():
    global count, zgel, isJump, run, left, right, x, y, walkCount, keys, jumpCount, label, jnab, lteht, restart
   
    run = True
    while run:
        clock.tick(27)

        if zgel >= 4:
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and x >=0:
            x -= vel
            left = True
            right = False
        elif keys[pygame.K_RIGHT] and x < 430:
            x += vel
            right = True
            left = False
        else:
            right = False
            left = False
            walkCount = 0
            
        if not(isJump):
            if keys[pygame.K_SPACE]:
                isJump = True
                right = False
                left = False
                walkCount = 0
        else:
            if jumpCount >= -10:
                neg = 1
                if jumpCount < 0:
                    neg = -1
                y -= (jumpCount ** 2) * 0.5 * neg
                jumpCount -= 1
            else:
                isJump = False
                jumpCount = 10

        if (x <= jnab and x >= jnab - 40) and lteht >= y and lteht <= y + 70:
            jnab = randint(0, 430)
            lteht = 0
            count=count+1
            print(count)

        if lteht == 500:
            zgel = zgel + 1

        redrawGameWindow()
    
    label2 = pygame.font.SysFont("monospace", 15)
    label2 = myfont.render("Press the Spacebar to Replay or Escape to Quit", 1, (0,0,0))
    win.blit(label2, (60, 200))

    while True:
        gameOverWindow()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_SPACE]:
            restart = 1
            break
        if keys[pygame.K_ESCAPE]:
            break

mainLoop()
while True:
    if restart == 1:
        x = 250
        y = 400
        restart = 0
        vel = 10
        isJump = False
        jumpCount = 10
        left = False
        right = False
        walkCount = 0
        lteht = 0
        jnab = randint(0, 430)
        count=0
        zgel = 0

        myfont = pygame.font.SysFont("monospace", 15)

        label = myfont.render(str(count), 1, (0,0,0))


        restart = 0
        mainLoop()
    else:
        break
#Game Over
#Show score
#Click on any key to replay


#pygame.quit()


pygame.quit()
