import pygame as pg
import random
import math as mt
# import Sys
# import os
pg.init()
display= pg.display.set_mode((700,700))
pg.display.set_caption("ASTEROID")
x=350
y=600
width=25
height=50
vel=10
vel_new=10
###################
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
player_health=200
################################
w1=700
h1=700
DS=pg.display.set_mode((w1,h1))
background=pg.image.load("background2.jpg").convert()
background2=pg.image.load("background4.jpg").convert()
asteroid1=pg.image.load("asteroid1.jpg").convert()
asteroid2=pg.image.load("asteroid2.jpg").convert()
spaceship=pg.image.load("spaceship4.jpg").convert()    # creating an game icon(image) along with game name
retrymenu=pg.image.load("RETRYMENU.jpg").convert() 
pg.display.set_icon(spaceship)
y1=0
asteroid=[asteroid1,asteroid2]
asteroid_new=asteroid1
#################################
blue = (0, 0, 255) 
tl_x = 50
tl_y = 50
h = 50
w = 20
height_obstacle=700
speed = 5
score=0     # score counter depends on how long you play
font=pg.font.Font('freesansbold.ttf',32)
score_x=10
score_y=10
health=5
health_new=3
health_x=10
health_y=45
def show_score(x,y):
    score_val=font.render("SCORE :" + str(score),True,(255,255,255))
    display.blit(score_val,(x,y))
def show_health(x,y):
    health_val=font.render("HEALTH :" + str(health),True,(255,255,255))
    display.blit(health_val,(x,y))
###############################
#pg.time.clock()
clock=pg.time.Clock()
current_time=0
current_time=pg.time.get_ticks()

run=True
menu=False # mouse down to umpause and p to pause
mainmenu=False
gameover=False
while run:
    distance=mt.sqrt(pow((tl_x-x),2)+pow((tl_y-y),2))
    if mt.sqrt(pow((tl_x-x),2)+pow((tl_y-y),2)) <120:
        tl_y  = 0
        tl_x = random.randrange(25,675)
        asteroid_new=random.choice(asteroid)
        health-=1
    #if health==0:
       # gameover = True
    while menu:  # pause menu
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()
            elif event.type==pg.MOUSEBUTTONDOWN:
                if event.button==1:
                    menu=False
        display.fill((0,0,0))
        clock.tick(30)
        display.blit(background2,(0,0)) # for the main menu use another background with instructions on it (photoshoped)
        pg.display.update()
    while mainmenu:
        for event in pg.event.get():
            if event.type==pg.QUIT:
                quit()
            elif event.type==pg.MOUSEBUTTON:
                if event.button==1:
                    mainmenu =False    #if health>1 other wise mainmennu=True
        display.fill((0,0,0))
        clock.tick(30)
        display.blit(retrymenu,(0,0))
        pg.display.update
    while gameover:         # health=0 then gameover = true
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()
            elif event.type==pg.MOUSEBUTTONDOWN:
                if event.button==1:
                    gameover=False
                    mainmenu=True
        display.fill((0,0,0))
        clock.tick(30)
        display.blit(retrymenu,(0,0))
        pg.display.update
    pg.time.delay(10)


    for event in pg.event.get():
        if event.type == pg.QUIT:
            run=False
    keys = pg.key.get_pressed()
    clock.tick(45)
    current_time=pg.time.get_ticks()
    if (current_time%1000==0 and vel_new<40):
        vel_new+=vel*0.75
        #score*=1.20
        
    if current_time%10==0 :
        score+=5
    
    if (current_time<100):
        if keys[pg.K_p]:
            menu = True
    if keys[pg.K_LEFT] and x>0:
        x-=vel_new
    elif keys[pg.K_RIGHT] and x<=667:
        x+=vel_new
    elif keys[pg.K_UP] and y>0:
        y-=vel_new
    elif keys[pg.K_DOWN] and y<=645:
        y+=vel_new
    # elif event.type==pg.KEYDOWN:
 
    elif keys[pg.K_p]:
            menu=True
      
    #pg.ScreenText(f"SCORE {score}",blue,10,40,size=20)
    rel_y = y1%background.get_rect().height
    DS.blit(background , (0,rel_y - background.get_rect().height))
    if  rel_y < h1 :
        DS.blit(background,(0,rel_y))
    y1 += 2
    rect = pg.draw.rect(display,("red"),(x,y,width,height))
    DS.blit(asteroid_new,(tl_x,tl_y))
    DS.blit(spaceship,(x,y))
    #pg.draw.rect(display, blue, (tl_x , tl_y, w, h))
    
    y_change = speed
    #pg.draw.rect(display,red,(10,45,200,5))
    #pg.draw.rect(display,red,(10,45,player_health,5))

    if tl_y == height_obstacle:
        tl_y  = 0
        tl_x = random.randrange(25,675)
        w=75
        h=50
        asteroid_new=random.choice(asteroid) 
        #w=random.randrange(30,70,15)
        #h=random.randrange(30,70,15)
        #blue=random.choice(colour)
        # speed=random.randint(5,25)
    # if tl_y >= 400 :
        
    #     pg.draw.rect(display, blue, (tl_x , tl_y, w, h))
    
    tl_y += y_change
    
    # if tl_y >=400:
    #     pg.draw.rect(display, blue, (tl_x , tl_y, w, h))
         
    # speed=random.randrange(5,20,5)  
    show_score(score_x,score_y)
    show_health(health_x,health_y)
    pg.display.update()
    
    
    #print(current_time)
pg.quit()
