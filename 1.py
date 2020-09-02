import pygame
import time
import random
pygame.init()
grey=(199, 194, 181)
black=(0,0,0)
red=(200,0,0)
green=(0,200,0)
blue=(0,0,200)
bright_red=(255,0,0)
bright_green=(0,255,0)
bright_blue=(0,0,255)


display_width=800
display_height=600
car_width=56
pause=False

gamedisplays=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Car game")
clock=pygame.time.Clock()
carimg=pygame.image.load('car1.png')
backgroundpic=pygame.image.load("grass.jpg")
yellow_strip=pygame.image.load("yellow strip.png")
strip=pygame.image.load("strip.jpg")
intro_bg=pygame.image.load("intro_bg.jpg")
instruction_bg=pygame.image.load("instruction_bg.jpg")


def intro_loop():
    intro=True
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()

        gamedisplays.blit(intro_bg,(0,0))
        largetext=pygame.font.Font('freesansbold.ttf',115)
        textsurf,textrect=text_objects("CAR GAME",largetext)
        textrect.center=(400,100)
        gamedisplays.blit(textsurf,textrect)
        button("START",150,520,100,50,green,bright_green,"play")
        button("QUIT",550,520,100,50,red,bright_red,"quit")
        button("INSTRUCTION",300,520,200,50,blue,bright_blue,"intro")
        pygame.display.update()
        clock.tick(50)

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x+w>mouse[0]>x and y+h>mouse[1]>y:
        pygame.draw.rect(gamedisplays,ac,(x,y,w,h))
        if click[0]==1 and action!=None:
            if action=="play":
                countdown()
            elif action=="quit":
                pygame.quit()
                quit()
                sys.exit()
            elif action=="intro":
                introduction()
            elif action=="menu":
                intro_loop()
            elif action=="pause":
                paused()
            elif action=="unpause":
                unpaused()

    else:
        pygame.draw.rect(gamedisplays,ic,(x,y,w,h))
    smalltext=pygame.font.Font("freesansbold.ttf",20)
    textsurf,textrect=text_objects(msg,smalltext)
    textrect.center= ((x+(w/2)),(y+(h/2)))
    gamedisplays.blit(textsurf,textrect)



def introduction():
    introduction=True
    while introduction:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gamedisplays.blit(instruction_bg,(0,0))
        largetext=pygame.font.Font('freesansbold.ttf',80)
        smalltext=pygame.font.Font('freesansbold.ttf',20)
        mediumtext=pygame.font.Font('freesansbold.ttf',40)
        textsurf,textrect=text_objects("This is a car game in which you need to dodge the coming cars",smalltext)
        textrect.center=((350),(200))
        TextSurf,TextRect=text_objects("INSTRUCTION",largetext)
        TextRect.center=((400),(100))
        gamedisplays.blit(TextSurf,TextRect)
        gamedisplays.blit(textsurf,textrect)
        stextsurf,stextrect=text_objects("ARROW LEFT : LEFT TURN",smalltext)
        stextrect.center=((150),(400))
        htextsurf,htextrect=text_objects("ARROW RIGHT : RIGHT TURN",smalltext)
        htextrect.center=((150),(450))
        atextsurf,atextrect=text_objects("W : ACCELERATE",smalltext)
        atextrect.center=((150),(500))
        rtextsurf,rtextrect=text_objects("S : DECELERATE",smalltext)
        rtextrect.center=((150),(550))
        ptextsurf,ptextrect=text_objects("P : PAUSE",smalltext)
        ptextrect.center=((150),(350))
        sTextSurf,sTextRect=text_objects("CONTROLS",mediumtext)
        sTextRect.center=((350),(300))
        gamedisplays.blit(sTextSurf,sTextRect)
        gamedisplays.blit(stextsurf,stextrect)
        gamedisplays.blit(htextsurf,htextrect)
        gamedisplays.blit(atextsurf,atextrect)
        gamedisplays.blit(rtextsurf,rtextrect)
        gamedisplays.blit(ptextsurf,ptextrect)
        button("BACK",600,450,100,50,blue,bright_blue,"menu")
        pygame.display.update()
        clock.tick(30)

def paused():
    global pause

    while pause:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()

        gamedisplays.blit(instruction_bg,(0,0))
        largetext=pygame.font.Font('freesansbold.ttf',115)
        TextSurf,TextRect=text_objects("PAUSED",largetext)
        TextRect.center=((display_width/2),(display_height/2))
        gamedisplays.blit(TextSurf,TextRect)
        button("RESUME",150,450,150,50,green,bright_green,"unpause")
        button("RESTART",350,450,150,50,blue,bright_blue,"play")
        button("MAIN MENU",550,450,200,50,red,bright_red,"menu")
        pygame.display.update()
        clock.tick(30)


def unpaused():
    global pause
    pause=False

def countdown_bg():
    font=pygame.font.SysFont(None,25)
    x=(display_width*0.45)
    y=(display_height*0.8)
    gamedisplays.blit(backgroundpic,(0,0))
    gamedisplays.blit(backgroundpic,(0,200))
    gamedisplays.blit(backgroundpic,(0,400))
    gamedisplays.blit(backgroundpic,(700,0))
    gamedisplays.blit(backgroundpic,(700,200))
    gamedisplays.blit(backgroundpic,(700,400))

    gamedisplays.blit(yellow_strip,(400,100))
    gamedisplays.blit(yellow_strip,(400,200))
    gamedisplays.blit(yellow_strip,(400,300))
    gamedisplays.blit(yellow_strip,(400,400))
    gamedisplays.blit(yellow_strip,(400,100))
    gamedisplays.blit(yellow_strip,(400,500))
    gamedisplays.blit(yellow_strip,(400,0))
    gamedisplays.blit(yellow_strip,(400,600))


    gamedisplays.blit(strip,(120,200))
    gamedisplays.blit(strip,(120,0))
    gamedisplays.blit(strip,(120,100))
    gamedisplays.blit(strip,(680,100))
    gamedisplays.blit(strip,(680,0))
    gamedisplays.blit(strip,(680,200))

    gamedisplays.blit(carimg,(x,y))
    text=font.render("DODGED : 0",True,black)
    score=font.render("SCORE : 0",True,red)
    gamedisplays.blit(text,(0,50))
    gamedisplays.blit(score,(0,30))
    button("Pause",650,0,150,50,blue,bright_blue,"pause")


def countdown():
    countdown=True

    while countdown:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gamedisplays.fill(grey)
        countdown_bg()
        largetext=pygame.font.Font('freesansbold.ttf',115)
        TextSurf,TextRect=text_objects("3",largetext)
        TextRect.center=((display_width/2),(display_height/2))
        gamedisplays.blit(TextSurf,TextRect)
        pygame.display.update()
        clock.tick(1)
        gamedisplays.fill(grey)
        countdown_bg()
        largetext=pygame.font.Font('freesansbold.ttf',115)
        TextSurf,TextRect=text_objects("2",largetext)
        TextRect.center=((display_width/2),(display_height/2))
        gamedisplays.blit(TextSurf,TextRect)
        pygame.display.update()
        clock.tick(1)
        gamedisplays.fill(grey)
        countdown_bg()
        largetext=pygame.font.Font('freesansbold.ttf',115)
        TextSurf,TextRect=text_objects("1",largetext)
        TextRect.center=((display_width/2),(display_height/2))
        gamedisplays.blit(TextSurf,TextRect)
        pygame.display.update()
        clock.tick(1)
        gamedisplays.fill(grey)
        countdown_bg()
        largetext=pygame.font.Font('freesansbold.ttf',115)
        TextSurf,TextRect=text_objects("GO!!!",largetext)
        TextRect.center=((display_width/2),(display_height/2))
        gamedisplays.blit(TextSurf,TextRect)
        pygame.display.update()
        clock.tick(1)
        game_loop()


def obstacle(obs_startx,obs_starty,obs):
    if obs==0:
        obs_pic=pygame.image.load("car100.png")
    elif obs==1:
        obs_pic=pygame.image.load("car100.png")
    elif obs==2:
        obs_pic=pygame.image.load("car100.png")
    elif obs==3:
        obs_pic=pygame.image.load("car100.png")
    elif obs==4:
        obs_pic=pygame.image.load("car100.png")

    gamedisplays.blit(obs_pic,(obs_startx,obs_starty))

def score_system(passed,score):
    font=pygame.font.SysFont(None,25)
    text=font.render("Passed"+str(passed),True,black)
    score=font.render("Score"+str(score),True,red)
    gamedisplays.blit(text,(0,50))
    gamedisplays.blit(score,(0,30))


def text_objects(text,font):
    textsurface=font.render(text,True,black)
    return textsurface,textsurface.get_rect()

def message_display(text):
    largetext=pygame.font.Font("freesansbold.ttf",80)
    textsurf,textrect=text_objects(text,largetext)
    textrect.center=((display_width/2),(display_height/2))
    gamedisplays.blit(textsurf,textrect)
    pygame.display.update()
    time.sleep(3)
    game_loop()

def crash():
    message_display("You Crashed")

def background():
    gamedisplays.blit(backgroundpic,(0,0))
    gamedisplays.blit(backgroundpic,(0,200))
    gamedisplays.blit(backgroundpic,(0,400))
    gamedisplays.blit(backgroundpic,(700,0))
    gamedisplays.blit(backgroundpic,(700,200))
    gamedisplays.blit(backgroundpic,(700,400))

    gamedisplays.blit(yellow_strip,(400,0))
    gamedisplays.blit(yellow_strip,(400,100))
    gamedisplays.blit(yellow_strip,(400,200))
    gamedisplays.blit(yellow_strip,(400,300))
    gamedisplays.blit(yellow_strip,(400,400))
    gamedisplays.blit(yellow_strip,(400,500))

    gamedisplays.blit(strip,(120,0))
    gamedisplays.blit(strip,(120,100))
    gamedisplays.blit(strip,(120,200))
    gamedisplays.blit(strip,(680,0))
    gamedisplays.blit(strip,(680,100))
    gamedisplays.blit(strip,(680,200))



def car(x,y):
    gamedisplays.blit(carimg,(x,y))

def game_loop():
    global pause
    pause=True
    x=(display_width*0.45)
    y=(display_height*0.8)
    x_change=0

    obstacle_speed=9
    obs=0
    y_change=0
    obs_startx=random.randrange(200,(display_width-200))
    obs_starty=-750
    obs_width=56
    obs_height=125
    passed=0
    level=0
    score=0
    y2=7



    bumped= False
    while not bumped:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x_change=-5
                if event.key==pygame.K_RIGHT:
                    x_change=5
                if event.key==pygame.K_w:
                    obstacle_speed+=2
                if event.key==pygame.K_s:
                    obstacle_speed-=2

            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    x_change=0

        x+=x_change
        gamedisplays.fill(grey)

        rel_y=y2%backgroundpic.get_rect().width
        gamedisplays.blit(backgroundpic,(0,rel_y-backgroundpic.get_rect().width))
        gamedisplays.blit(backgroundpic,(700,rel_y-backgroundpic.get_rect().width))

        if rel_y<800:
            gamedisplays.blit(backgroundpic,(0,rel_y))
            gamedisplays.blit(backgroundpic,(700,rel_y))
            gamedisplays.blit(yellow_strip,(400,rel_y))
            gamedisplays.blit(yellow_strip,(400,rel_y+100))
            gamedisplays.blit(yellow_strip,(400,rel_y+200))
            gamedisplays.blit(yellow_strip,(400,rel_y+300))
            gamedisplays.blit(yellow_strip,(400,rel_y+400))
            gamedisplays.blit(yellow_strip,(400,rel_y+500))
            gamedisplays.blit(yellow_strip,(400,rel_y-100))
            gamedisplays.blit(strip,(120,rel_y-200))
            gamedisplays.blit(strip,(120,rel_y+20))
            gamedisplays.blit(strip,(120,rel_y+30))
            gamedisplays.blit(strip,(680,rel_y-100))
            gamedisplays.blit(strip,(680,rel_y+20))
            gamedisplays.blit(strip,(680,rel_y+30))

            y2+=obstacle_speed



        obs_starty-=obstacle_speed/4
        obstacle(obs_startx,obs_starty,obs)
        obs_starty+=obstacle_speed

        car(x,y)
        score_system(passed,score)
        if x>690-car_width or x<110:
            crash()

        if x>display_width-(car_width+110) or x<110:
            crash()
        if obs_starty>display_height:
            obs_starty=0-obs_height
            obs_startx=random.randrange(170,(display_width-170))
            obs=random.randrange(0,4)
            passed=passed+1
            score=passed*10
            if int(passed)%10==0:
                level=level+1
                obstacle_speed+2
                largetext=pygame.font.Font("freesansbold.ttf",80)
                textsurf,textrect=text_objects("LEVEL"+str(level),largetext)
                textrect.center=((display_width/2),(display_height/2))
                gamedisplays.blit(textsurf,textrect)
                pygame.display.update()
                time.sleep(1)

        if y<obs_starty+obs_height:
            if x>obs_startx and x<obs_startx+obs_width or x+car_width> obs_startx and x+car_width< obs_startx+ obs_width:
                crash()
        button("Pause",650,0,150,50,blue,bright_blue,"pause")
        pygame.display.update()
        clock.tick(60)
intro_loop()
game_loop()
pygame.quit()
quit()
