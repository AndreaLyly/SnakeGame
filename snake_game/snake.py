import pygame
import random
import time

pygame.init()

width = 400
height = 400

black = (0,0,0)
white = (255,255,255)
purple = (220,0,200)
purple2 = (220,0,140)
grey = (51,0,0)

scl = 20
pause = False

display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

pelaaja = pygame.image.load("ruoka.png")
food = pygame.image.load("hahmo.png")
bg = pygame.image.load("tausta.png")

class Snake:
    x = [0]
    y = [0]
    
    def __init__(self, x_p, y_p, x_s, y_s, pict):
        self.x[0] = x_p
        self.y[0] = y_p
        self._speedx = x_s
        self._speedy = y_s
        self.pic = pict
        self.total = 1
        
    def get_startx(self):
        return self._startx
    def get_starty(self):
        return self._starty
    def get_speedx(self):
        return self._speedx
    def get_speedy(self):
        return self._speedy
    def get_pic(self):
        return self._picture
        
    def up_xy(self, x,y):
        self.x.append(x)
        self.y.append(y)
        
    def up_tot(self, tot):
        self.total = tot
        
    def update(self, dirx, diry):
        for i in range(self.total-1, 0, -1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]
            
        if dirx == 1:
            self.x[0] = self.x[0] + 20
        elif dirx == -1:
            self.x[0] = self.x[0] - 20
        elif diry == 1:
            self.y[0] = self.y[0] + 20
        elif diry == -1:
            self.y[0] = self.y[0] - 20
            
    def draw(self):
        for i in range(0, self.total):
            display.blit(self.pic,(self.x[i],self.y[i])) 

class Food:
    def __init__(self, x, y, pic):
        self._locx = x 
        self._locy = y 
        self._foodpic = pic
    
    def get_locx(self):
        return self._locx
    def get_locy(self):
        return self._locy
    def get_foodpic(self):
        return self._foodpic
    def drawfood(self):
        display.blit(self._foodpic, (self._locx, self._locy))
    def change_loc(self, x, y):
        self._locx = x 
        self._locy = y
        
    
def picklocation():
    global scl 
    cols = width / scl
    rows = height / scl 
    a = random.randint(0, cols-1) * scl
    b = random.randint(0, rows-1) * scl
    return a, b

def background():
    display.blit(bg, (0,0))
    
def text_objects(text, font):    
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
    
def button(msg, x, y, w, h, ic, ac, action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(display, ac, (x,y,w,h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(display, ic, (x,y,w,h))
            
    smallText = pygame.font.SysFont("comicsansms", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x + (w / 2)), (y + (h / 2))  )
    display.blit(textSurf, textRect)

def endpause():
    global pause
    pause = False

def paused():
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    endpause()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()  
        background()
        largeText = pygame.font.SysFont("comicsansms", 50)
        TextSurf, TextRect = text_objects('Paused', largeText)
        TextRect.center = ((width / 2), (height / 5))
        display.blit(TextSurf, TextRect)
        button("Continue", 150, 200, 100, 50, purple2, purple, endpause)
        button("Quit", 150, 300, 100, 50, purple2, purple, quit_game)
        pygame.display.update()
        clock.tick(15)
    
    
def crashed(score):
    str_score = str(score)
    crash = True
    while crash:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_loop()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()  
        background()
        largeText = pygame.font.SysFont("comicsansms", 50)
        TextSurf, TextRect = text_objects('Score: '+str_score, largeText)
        TextRect.center = ((width / 2), (height / 5))
        
        #largeText2 = pygame.font.SysFont("comicsansms", 50)
        #TextSurf2, TextRect2 = text_objects('Highscore: ', largeText2)
        #TextRect2.center = ((width / 2), (height / 2.7))
        
        display.blit(TextSurf, TextRect)
        #display.blit(TextSurf2, TextRect2)
        button("Replay", 150, 200, 100, 50, purple2, purple, game_loop)
        button("Quit", 150, 300, 100, 50, purple2, purple, quit_game)
        pygame.display.update()
        clock.tick(15)
    
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_loop()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()  
        background()
        largeText = pygame.font.SysFont("comicsansms", 50)
        TextSurf, TextRect = text_objects('Snake', largeText)
        TextRect.center = ((width / 2), (height / 5))
        display.blit(TextSurf, TextRect)
        button("Play", 150, 200, 100, 50, purple2, purple, game_loop)
        button("Quit", 150, 300, 100, 50, purple2, purple, quit_game)
        pygame.display.update()
        clock.tick(15)
        
def quit_game():
    pygame.quit()
    quit()

def game_loop():
    global scl
    global pause
    x = random.randint(0, (width / scl) - 1) * scl
    y = random.randint(0, (height / scl) - 1) * scl
    xspeed = 0
    yspeed = 0
    total = 1
    
    s = Snake(x, y, xspeed, yspeed, pelaaja)
    a, b = picklocation()
    f = Food(a, b, food)
    
    s.up_tot(total)
    s.up_xy(x, y)
    
    gameExit = False
    
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause = True
                    paused()
                    
                if event.key == pygame.K_UP:
                    if xspeed == 0 and yspeed == 1:
                        xspeed = 0
                        yspeed = 1
                    else:
                        xspeed = 0
                        yspeed = -1  
                elif event.key == pygame.K_DOWN:
                    if xspeed == 0 and yspeed == -1:
                        xspeed = 0
                        yspeed = -1
                    else:
                        xspeed = 0
                        yspeed = 1                
                elif event.key == pygame.K_RIGHT:
                    if xspeed == -1 and yspeed == 0:
                        xspeed = -1
                        yspeed = 0
                    else:
                        xspeed = 1
                        yspeed = 0      
                elif event.key == pygame.K_LEFT:
                    if xspeed == 1 and yspeed == 0:
                        xspeed = 1
                        yspeed = 0
                    else:
                        xspeed = -1
                        yspeed = 0
                               
        x += xspeed * scl
        y += yspeed * scl
        background()
        f.drawfood()
        s.update(xspeed, yspeed)
        s.draw()
        
        d1 = abs(f.get_locx() - s.x[0])
        d2 = abs(f.get_locy() - s.y[0])
        if d1 < 1 and d2 == 0 or d1 == 0 and d2 < 1:
            a, b = picklocation()
            for i in range(len(s.x)):
                while a == s.x[i] and b == s.y[i]:
                    a, b = picklocation()
            f.change_loc(a, b)
            total += 1
            s.up_tot(total)
            s.up_xy(x, y)
            
        if s.x[0] < 0 or s.x[0] > 380 or s.y[0] < 0 or s.y[0] > 380:
            time.sleep(1)
            crashed(total)
        
        if total > 1:
            for part in range(1, total):
                posx = s.x[part]
                posy = s.y[part]
                dist1 = abs(s.x[0] - posx)
                dist2 = abs(s.y[0] - posy)
                if dist1 < 1 and dist2 == 0 or dist1 == 0 and dist2 < 1:
                    time.sleep(1)
                    crashed(total)
            
        pygame.display.update()
        clock.tick(10)
    
game_intro()
                
                
                
                

