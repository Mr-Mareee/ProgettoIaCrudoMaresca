from threading import Thread
from time import sleep
from typing import List
import pygame
pygame.init()
class archi():
    def __init__(self):
        pass
class Node(Thread):
    def __init__(self,adiacent : List,x,y,screen):
        super().__init__()
        self.truppe=0
        self.adiacenti=adiacent
        self.x=x
        self.y=y
        self.scr=screen
    def run(self):
        sleep(0.1)
        size=30
        ydraw=self.y
        while True:
            pygame.draw.circle(self.scr,(255,255,255),(self.x,self.y),10)
            score_obj=pygame.font.SysFont("comicsans",size,True)
            score_txt=score_obj.render(str(self.truppe),1,(0,0,0))
            self.scr.blit(score_txt,(self.x-5,ydraw-10))
            self.truppe+=1
            if (self.truppe==10):
                size=15
                ydraw+=5
            sleep(1)

width=612
height=382
scr=pygame.display.set_mode((width,height))
running=True
x=100
y=50
element=[]
nodi=[]
for i in range(16):
        nodo=Node(element,x,y,scr)
        nodo.start()
        nodi.append(nodo)
        y+=80
        if (y>=350):
            y=50
            x+=130
for i in range(15):
    pygame.draw.line(scr,(255,0,0),(nodi[i].x,nodi[i].y),(nodi[i+1].x,nodi[i+1].y),2)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    pygame.display.flip()
pygame.quit()

