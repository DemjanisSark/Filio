import pygame
import random
pygame.init()
sc=pygame.display.set_mode((500, 650))

clock=pygame.time.Clock()
FPS=60

Nebo=(0,139,139)
Zemla=(0,128,0)
Luna=(255,255,250)
Oblaka1=(128,128,128)
Oblaka2=(105,105,105)
Lampocki_tarelki=(245,245,245)
Tarelka=(192,192,192)
Kabina_tarelki=(212,212,212)
Svet=(255,250,205)
Dibil=(250,250,210)
Red=(250,0,0)
Black=(0,0,0)
White=(255,255,255)
Green=(0,255,0)

pygame.draw.rect(sc, Nebo, (0, 0, 500, 325))
pygame.draw.rect(sc, Zemla, (0,328,500,355))

pygame.draw.circle(sc, Luna, (350,170),50)

for i in range(3):
    x=random.randint(50,450)
    y=random.randint(40,300)
    pygame.draw.ellipse(sc, Oblaka1, (x,y,300,50))
for i in range(5):
    x=random.randint(50,450)
    y=random.randint(40,250)
    pygame.draw.ellipse(sc, Oblaka2, (x,y,300,50))

pygame.draw.polygon(sc, Svet, [(80,510),(180,300),(280,510)])
pygame.draw.ellipse(sc, Tarelka, (50,270,250,80))
pygame.draw.ellipse(sc, Kabina_tarelki, (90,260,170,60))
#pygame.draw.ellipse(sc,Lampocki_tarelki, (60,300,30,20))
x=20
y=287
k=140
j=339
for i in range(3):
    x +=40
    y +=13
    pygame.draw.ellipse(sc,Lampocki_tarelki, (x,y,30,20))
for i in range(3):
    k +=40
    j +=-13
    pygame.draw.ellipse(sc,Lampocki_tarelki, (k,j,30,20))

pygame.draw.ellipse(sc, Dibil, (400, 450, 50, 100))
#Ruka pravaja
pygame.draw.circle(sc, Dibil, (400,480),10)
pygame.draw.ellipse(sc, Dibil, (385,485,15,10))
pygame.draw.ellipse(sc, Dibil, (380,500,7,12))
#Ruka Levaja+jabloko
pygame.draw.circle(sc, Dibil, (455,480),10)
pygame.draw.ellipse(sc, Dibil, (460,480,15,10))
pygame.draw.ellipse(sc, Dibil, (475,483,15,10))

pygame.draw.circle(sc, Red, (487,470),12)
pygame.draw.line(sc, Black, (487, 450),(490,460))
pygame.draw.ellipse(sc, Green, (490,450,7,10))

#nogaa pravaja
pygame.draw.ellipse(sc, Dibil, (395,525,20,30))
pygame.draw.ellipse(sc, Dibil, (390,550,15,35))
pygame.draw.circle(sc, Dibil, (385,580),10)

#noga levaja
pygame.draw.ellipse(sc, Dibil, (435,530,20,30))
pygame.draw.ellipse(sc, Dibil, (445,555,15,35))
pygame.draw.circle(sc, Dibil, (467,580),10)

#golova
pygame.draw.polygon(sc, Dibil, [(390,455),(460,455),(420,380)])
#glaz
pygame.draw.circle(sc, Black, (425,430),15)
pygame.draw.circle(sc, White, (425,430),5)
#Antena
pygame.draw.ellipse(sc, Dibil, (425,380,40,30))
pygame.draw.ellipse(sc, Dibil, (380,380,40,30))

pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
