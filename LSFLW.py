from threading import Thread
from time import sleep
from typing import List
import math
import pygame
image = pygame.image.load(r"sfondo.jpg")
MAX_TRUPPE = 98
PLAYER_COLOR = (102,102,255)
ENEMY_COLOR = (255,178,102)
NEUTRAL_COLOR = (255,255,255) #colore dei nodi neutrali
TEXT_COLOR = (0,0,0)
SELECTED_NODE = (0,255,0)
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("colonna_sonora.mp3")
pygame.mixer.music.play(loops = -1)  #decommentare se si vuole la musica
class archi():
    def __init__(self):
        pass
class Node(Thread):
    def __init__(self,name:str,color,x,y,screen):
        super().__init__()
        self.truppe=0
        self.x=x
        self.y=y
        self.xdraw=self.x
        self.ydraw = self.y
        self.scr=screen
        self.color = color
        self.name = name
        self.size = 30
        self.counter = 0
        self.running = True

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getName(self):
        return self.name
    
    def isAllied(self):
        if(self.color == PLAYER_COLOR):
            return True
        else:
            return False

    def termina(self):
        self.running = False

    def setColor(self,v):
        self.color = v

    def getColor(self):
        return self.color

    def sommaTruppe(self,t:int,chiManda):
        if(chiManda == 1 and self.color == PLAYER_COLOR):
            if(self.truppe + t < MAX_TRUPPE):
                self.truppe += t
            else:
                self.truppe = MAX_TRUPPE
        elif(chiManda == 1 and self.color == NEUTRAL_COLOR):
            self.color = PLAYER_COLOR
            if(self.truppe + t < MAX_TRUPPE):
                self.truppe += t
            else:
                self.truppe = MAX_TRUPPE
        elif(chiManda == 1 and self.color == ENEMY_COLOR):
            if(t - self.truppe >= 0):
                self.truppe = t - self.truppe
                self.color = PLAYER_COLOR
            else:
                self.truppe -= t
    
    def azzeraTruppe(self):
        self.truppe = 0

    def getTruppe(self):
        return int(self.truppe)

    def run(self):
        while self.running:
                pygame.draw.circle(self.scr,self.color,(self.x,self.y),25)
                score_obj=pygame.font.SysFont("comicsans",self.size,True)
                if(self.color == NEUTRAL_COLOR):
                    score_txt=score_obj.render(str(int(self.truppe)),1,TEXT_COLOR)
                if(self.color == PLAYER_COLOR or self.color == ENEMY_COLOR or self.color == SELECTED_NODE):
                    score_txt=score_obj.render(str(int(self.truppe +1)),1,TEXT_COLOR)
                self.scr.blit(score_txt,(self.xdraw-5,self.ydraw-10))
                if(self.truppe<MAX_TRUPPE and self.color != NEUTRAL_COLOR): #massimo 99 truppe per nodo
                    self.truppe += 0.10 #aumento le truppe di 0.25 ogni 0.25 secondi quindi di 1 al secondo
                #if (self.truppe==10):
                    #self.size=25
                    #self.xdraw-=5
                sleep(0.10)

width=1280
height=720
scr=pygame.display.set_mode((width,height))
pygame.display.set_caption('Little Stars For Little Wars')
scr.blit(image, (0, 0))
running=True
adiacenze=[[],[],[],[],[],[],[],[],[],[],[]]
nodi=[]
# Testi di fine gioco
fontWinLose = pygame.font.SysFont("comicsans",160,True)
    #Testo di vittoria
textWin = fontWinLose.render("HAI VINTO!", True, (255,255,0))
textRectWin = textWin.get_rect()
textRectWin.center = (width // 2, height - 520)
    #Testo di Sconfitta
textLose = fontWinLose.render("HAI PERSO!", True, (255,255,0))
textRectLose = textLose.get_rect()
textRectLose.center = (width // 2, height - 520)

# fine dichiarazione testi di fine gioco 

# Creo tutti i nodi
nodo = Node("0",PLAYER_COLOR,30,360,scr)
nodo.start()
nodi.append(nodo)
nodo = Node("1",PLAYER_COLOR,236,120,scr)
nodo.start()
nodi.append(nodo)
nodo = Node("2",PLAYER_COLOR,436,360,scr)
nodo.start()
nodi.append(nodo)
nodo = Node("3",PLAYER_COLOR,236,600,scr)
nodo.start()
nodi.append(nodo)
nodo = Node("4",NEUTRAL_COLOR,640,120,scr)
nodo.start()
nodi.append(nodo)
nodo = Node("5",NEUTRAL_COLOR,640,360,scr)
nodo.start()
nodi.append(nodo)
nodo = Node("6",NEUTRAL_COLOR,640,600,scr)
nodo.start()
nodi.append(nodo)
nodo = Node("7",ENEMY_COLOR,1044,120,scr)
nodo.start()
nodi.append(nodo)
nodo = Node("8",ENEMY_COLOR,832,360,scr)
nodo.start()
nodi.append(nodo)
nodo = Node("9",ENEMY_COLOR,1044,600,scr)
nodo.start()
nodi.append(nodo)
nodo = Node("10",ENEMY_COLOR,1250,360,scr)
nodo.start()
nodi.append(nodo)

# Fine creazione nodi a schermo

# Creo le adiancenze: la posizione della riga nella matrice delle adiacenze indica il nodo partenza

adiacenze[0] = ["1","2","3"]
adiacenze[1] = ["0"]
adiacenze[2] = ["4","5","6"]
adiacenze[3] = ["0"]
adiacenze[4] = ["2","8"]
adiacenze[5] = ["2","8"]
adiacenze[6] = ["2","8"]
adiacenze[7] = ["10"]
adiacenze[8] = ["4","5","6","10"]
adiacenze[9] = ["10"]
adiacenze[10] = ["7","8","9"]

#Fine creazione adiacenze

# Creazione archi
pygame.draw.line(scr,(255,0,0),(nodi[0].x,nodi[0].y),(nodi[0+1].x,nodi[0+1].y),2)
pygame.draw.line(scr,(255,0,0),(nodi[0].x,nodi[0].y),(nodi[0+2].x,nodi[0+2].y),2)
pygame.draw.line(scr,(255,0,0),(nodi[0].x,nodi[0].y),(nodi[0+3].x,nodi[0+3].y),2)
pygame.draw.line(scr,(255,0,0),(nodi[2].x,nodi[2].y),(nodi[2+2].x,nodi[2+2].y),2)
pygame.draw.line(scr,(255,0,0),(nodi[2].x,nodi[2].y),(nodi[2+3].x,nodi[2+3].y),2)
pygame.draw.line(scr,(255,0,0),(nodi[2].x,nodi[2].y),(nodi[2+4].x,nodi[2+4].y),2)
pygame.draw.line(scr,(255,0,0),(nodi[5].x,nodi[5].y),(nodi[5+3].x,nodi[5+3].y),2)
pygame.draw.line(scr,(255,0,0),(nodi[4].x,nodi[4].y),(nodi[4+4].x,nodi[4+4].y),2)
pygame.draw.line(scr,(255,0,0),(nodi[6].x,nodi[6].y),(nodi[6+2].x,nodi[6+2].y),2)
pygame.draw.line(scr,(255,0,0),(nodi[8].x,nodi[8].y),(nodi[8+2].x,nodi[8+2].y),2)
pygame.draw.line(scr,(255,0,0),(nodi[7].x,nodi[7].y),(nodi[7+3].x,nodi[7+3].y),2)
pygame.draw.line(scr,(255,0,0),(nodi[9].x,nodi[9].y),(nodi[9+1].x,nodi[9+1].y),2)
# Fine creazione archi
nodiCliccati = []
while running:
    cP = 0
    cE = 0
    for i in nodi:
        if(i.getColor() == PLAYER_COLOR):
            cP += 1
        elif(i.getColor() == ENEMY_COLOR):
            cE += 1
            
    if(cE == 0):
        scr.blit(image, (0, 0))
        scr.blit(textWin, textRectWin)
        for i in nodi:
            i.termina()

    elif(cP == 0):
        scr.blit(image, (0, 0))
        scr.blit(textLose, textRectLose)
        for i in nodi:
            i.termina()

    if(len(nodiCliccati) == 2): #azzero la coppia di nodi cliccati se la lunghezza è due
        nodiCliccati = []    #se sono arrivato qui con len = 2 sono sicuro di aver compiuto l'azione di spostamento truppe
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        if pygame.mouse.get_pressed()[0]:
            for i in nodi:
                #La formula sottostante calcola la distanza geometrica del punto cliccato
                #rispetto alla posizione del nodo che si desidera cliccare
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                sqx = (x - i.getX())**2
                sqy = (y - i.getY())**2
                pygame.time.wait(2)


                if math.sqrt(sqx + sqy) < 100: #se la distanza è < 100 ho beccato il nodo
                    if len(nodiCliccati) == 0 and i.isAllied(): # primo nodo selezionato deve essere del player
                        nodiCliccati.append(i.getName())
                        i.setColor(SELECTED_NODE)
                        
                    if (i.getName() not in nodiCliccati) and (len(nodiCliccati) <2 and len(nodiCliccati) >=1): #secondo nodo selezionato può essere qualsiasi nodo adiacente
                        if len(nodiCliccati) == 1:
                            if(i.getName() in adiacenze[int(nodiCliccati[0])]): # Gestisco le adiacenze
                                #se non sono nodi adiacenti non immagazino il nodo bersaglio
                                #prendo la coppia di nodi cliccati evitando i duplicati
                                nodiCliccati.append(i.getName())
                                if(len(nodiCliccati) == 2): # se ho esattamente 2 nodi
                                    print(nodiCliccati)
                                     #faccio l'azione di spostamento truppe
                                    t = 0  #variabile di appoggio per il numero di truppe da trasportare
                                    for i in nodi:
                                        if(i.getName() == nodiCliccati[0]):
                                            t = i.getTruppe()
                                            i.azzeraTruppe() 
                                            i.setColor(PLAYER_COLOR)
                                    for i in nodi:
                                        if(i.getName() == nodiCliccati[1]):
                                            i.sommaTruppe(t,1)
                            

    pygame.display.flip()
pygame.quit()

