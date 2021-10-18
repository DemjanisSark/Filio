import pygame
import random
import math

pygame.init()
sc=pygame.display.set_mode((800, 700))
clock=pygame.time.Clock()
FPS=60

#Список цветов
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

#Функция окружения: земля, небо, Луна, облака
def Earth():
    pygame.draw.rect(sc, Nebo, (0, 0, 800, 350))
    pygame.draw.rect(sc, Zemla, (0,330,800,350))
    pygame.draw.circle(sc, Luna, (600,150),50)
    for i in range(3):
        x=random.randint(50,450)
        y=random.randint(40,300)
        pygame.draw.ellipse(sc, Oblaka1, (x,y,300,50))
    for i in range(5):
        x=random.randint(50,450)
        y=random.randint(40,250)
        pygame.draw.ellipse(sc, Oblaka2, (x,y,300,50))


#Большая тарелка
def UFO1(u,p,b):
    pygame.draw.polygon(sc, Svet, [(u+40,p+140),(u+80,p+30),(u+140,p+140)])
    pygame.draw.ellipse(sc, Tarelka, (u,p,b*25,b*8))
    pygame.draw.ellipse(sc, Kabina_tarelki, (u+40-10,p-10,b*17,b*6))

    x=u-20
    y=p+17
    k=u+65
    j=p+45
    for i in range(3):
        x +=b*4
        y +=7
        pygame.draw.ellipse(sc,Lampocki_tarelki, (x,y,b*3,b*2))
    for i in range(3):
        k +=b*4
        j +=-7
        pygame.draw.ellipse(sc,Lampocki_tarelki, (k,j,b*3,b*2))

#Маленькая тарелка
def UFO2(u,p,b):
    pygame.draw.polygon(sc, Svet, [(u+40,p+240),(u+120,p+30),(u+190,p+240)])
    pygame.draw.ellipse(sc, Tarelka, (u,p,b*25,b*8))
    pygame.draw.ellipse(sc, Kabina_tarelki, (u+40,p-10,b*17,b*6))

    x=u-30
    y=p+20
    k=u+90
    j=p+69
    for i in range(3):
        x +=b*4
        y +=13
        pygame.draw.ellipse(sc,Lampocki_tarelki, (x,y,b*3,b*2))
    for i in range(3):
        k +=b*4 
        j +=-13 
        pygame.draw.ellipse(sc,Lampocki_tarelki, (k,j,b*3,b*2))

#Инопланетянин с яблокомв левой руке
def Alien1(x,y,m):
    n=10*math.fabs(m-5)
    p=n/2
#Торс 1
    pygame.draw.ellipse(sc, Dibil, (x,y,m*10,m*20))
#Правая рука 1
    pygame.draw.circle(sc, Dibil, (x-n/5,y+30-p),2*m)
    pygame.draw.ellipse(sc, Dibil, (x-15,y+35-p,3*m,2*m))
    pygame.draw.ellipse(sc, Dibil, (x-20+n/3,y+50-p*1.5,2*m,3*m))
#Левая рука 1
    pygame.draw.circle(sc, Dibil, (x+55-n,y+30-p),2*m)
    pygame.draw.ellipse(sc, Dibil, (x+60-n,y+30-p,3*m,2*m))
    pygame.draw.ellipse(sc, Dibil, (x+75-n*1.5,y+30-p,3*m,2*m))
#Правая нога 1
    pygame.draw.ellipse (sc, Dibil,(x-5,y+75-p*2 ,m*4,m*6))
    pygame.draw.ellipse(sc, Dibil, (x-10,y+100-p*3,m*3,m*7))
    pygame.draw.circle(sc, Dibil, (x-15,y+130-p*4),m*2)
#Левая нога 1
    pygame.draw.ellipse(sc, Dibil, (x+30-n/2,y+80-p*2,m*4,m*6))
    pygame.draw.ellipse(sc, Dibil, (x+45-n,y+105-p*3,m*3,m*7))
    pygame.draw.circle(sc, Dibil, (x+65-n*1.5,y+130-p*4),m*2)

#Голова 1
    pygame.draw.polygon(sc, Dibil, [(x-10,y+5),(x+60-n,y+5),(x+20,y-70+3*p)])
#Глаз 1
    pygame.draw.circle(sc, Black, (x+25-n/2,y-20+p),m*3)
    pygame.draw.circle(sc, White, (x+25-n/2,y-20+p),m)
#Ухи 1
    pygame.draw.ellipse(sc, Dibil, (x+25,y-70+p*3,m*8,m*6))
    pygame.draw.ellipse(sc, Dibil, (x-20+n/2,y-70+p*3,m*8,m*6))
#Яблоко 1
    pygame.draw.circle(sc, Red, (x+85-n*1.5,y+20),m*2)
    pygame.draw.line(sc, Black, (x+85-n*2, y),(x+90-n*2,y+10))
    pygame.draw.ellipse(sc, Green, (x+90-n*2,y,m,m*2))
        
#Инопланетянин с яблоком в правой руке
def Alien2(k,j,h):
   l=10*math.fabs(h-5)
   d=l/2
#Торс 2
   pygame.draw.ellipse(sc, Dibil, (k,j,10*h,20*h))
#Правая рука 2
   pygame.draw.circle(sc, Dibil, (k+55-l,j+30-d),2*h)
   pygame.draw.ellipse(sc, Dibil, (k+55-l,j+35-d,3*h,2*h))
   pygame.draw.ellipse(sc, Dibil, (k+65-l,j+50-d*2,2*h,3*h))
#Левая рука 2
   pygame.draw.circle(sc, Dibil, (k-l/2,j+30-d),2*h)
   pygame.draw.ellipse(sc, Dibil, (k-25+l/2,j+30-d,3*h,2*h))
   pygame.draw.ellipse(sc, Dibil, (k-40+l,j+30-d,3*h,2*h))
#Правая нога 2
   pygame.draw.ellipse(sc, Dibil, (k+35-l,j+75-d*2,4*h,6*h))
   pygame.draw.ellipse(sc, Dibil, (k+45-l,j+100-d*3,3*h,7*h))
   pygame.draw.circle(sc, Dibil, (k+60-l,j+130-d*4),2*h)
#Левая нога 2
   pygame.draw.ellipse(sc, Dibil, (k-5+l/2,j+80-d*2,4*h,6*h))
   pygame.draw.ellipse(sc, Dibil, (k-10+l,j+105-d*2,3*h,7*h))
   pygame.draw.circle(sc, Dibil, (k-15+l,j+120-d*2),2*h)
#Голова 2
   pygame.draw.polygon(sc, Dibil, [(k-10,j+5),(k+60-l,j+5),(k+20,j-70+d*3)])
#Глаз 2
   pygame.draw.circle(sc, Black, (k+25-l/2,j-20+d),3*h)
   pygame.draw.circle(sc, White, (k+25-l/2,j-20+d),h)
#Ухи 2
   pygame.draw.ellipse(sc, Dibil, (k+20+l/2,j-70+d*3,8*h,6*h))
   pygame.draw.ellipse(sc, Dibil, (k-20+l/2,j-70+d*3,8*h,6*h))
#Яблоко 2
   pygame.draw.circle(sc, Red, (k-35,j+20),2*h)
   pygame.draw.line(sc, Black, (k-30, j+d),(k-40,j+10+d))
   pygame.draw.ellipse(sc, Green, (k-42,j+d,h,2*h))

#Функция вызывающая все функции
def main():
    Earth()
    UFO2(200,150,10)
    UFO1(400,230,7)
    Alien1(60,400,5)
    Alien1(400,450,4)
    Alien2(600,300,5)
    Alien2(200,500,4)
main()


pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
