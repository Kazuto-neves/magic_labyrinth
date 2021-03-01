
import pygame
from random import *
import time
from pygame.locals import *
import os

try:
    pygame.init()
    pygame.mixer.init()
except:print("O jogo deu erro")

diretorio_principal = os.path.dirname(__file__)
diretorio_sons = os.path.join(diretorio_principal, 'audio')

def random_Color():
    r=randrange(0,255)
    g=randrange(0,255)
    b=randrange(0,255)
    return (r,g,b)
    #r= randint(0,255)
    #return(r)

def passou():
    pygame.mixer.music.load(os.path.join(diretorio_sons,'Arcade_Power_Up_01.mp3'))
    pygame.mixer.music.play()

def colidiu():
    pygame.mixer.music.load(os.path.join(diretorio_sons,'colidiu.mp3'))
    pygame.mixer.music.play()

def music():
    pygame.mixer.music.load(os.path.join(diretorio_sons,'musica.ogg'))
    pygame.mixer.music.play()
    pygame.mixer.music.rewind()

l=500
a=500
tela = pygame.display.set_mode([l, a])
pygame.display.set_caption('Labirinto magico')
time = pygame.time.Clock()
color_red = (255,0,0)
color_branco =(255,255,255)
color_preto =(0,0,0)
color_amarelo=(255,255,0)
color_verde=(0,128,0)

def pecm(pec,color):
    (pec.left, pec.top) = pygame.mouse.get_pos()
    pec.left -= pec.width/2
    pec.top -= pec.height/2
    pygame.draw.rect(tela,(color), pec)

def pos(A,B):pygame.mouse.set_pos([A, B])

#*def inv(o,l,v):
#*    if o.colliderect(l):v*=-1
    


def placar(lf,pts,lv):
    texto("Vidas:"+str(lf),color_red,20,30,10)
    texto("Pontuação:"+str(pts),color_branco,20,300,10)
    texto("Level:"+str(lv),color_branco,20,150,10)

def go(pts):
    tela.fill(color_branco)
    texto("Game Over",color_red,100,l/8,a/8)
    texto("Pontuação:"+str(pts),color_preto,50,l/4, a/3)
    pygame.draw.rect(tela,color_preto, [60,210,150,50])
    texto("Continuar",color_branco,30,85,210)
    texto("(ESPAÇO)",color_branco,30,85,240)
    pygame.draw.rect(tela,color_preto, [260,210,150,50])
    texto("Sair",color_branco,30,305,210)
    texto("(Esc)",color_branco,30,305,240)
    pygame.display.update()

def texto(msg, cor, t,x,y):
    fonte = pygame.font.SysFont(None, t)
    texto1 = fonte.render(msg, True, cor)
    tela.blit(texto1, [x, y])

def vel(t):return (4*t)

def bg(bg):
    if bg == True:return (color_preto)
    else:return (color_branco)

def fc(fc):
    if fc == True:return (color_branco)
    else:return (color_preto)

def bc(bc):
    if bc == True:return (color_amarelo)
    else:return (color_red)

def bt(bt):
    if bt == True:return (color_verde)
    else:return (color_preto)

def fcb(fcb):
    if fcb == True:return (color_amarelo)
    else:return (color_branco)

def img(tl):
    if tl == True:sl = pygame.image.load("sol.png")
    else:sl = pygame.image.load("lua.png") 
    tela.blit(sl, [19, 19])

def velO(v):return v+2

def tema(tm,bg,fc,bc,bt,fcb,tl):
    if tm == False:
        bg=True
        fc=True
        bc=True
        bt=True
        fcb=True
        tl=True
        tm=True
    else:
        bg=False
        fc=False
        bc=False
        bt=False
        fcb=False
        tl=False
        tm=False

Bg = True
Fc=True
Bc=True
Bt=True
Fcb=True
Tl=True
Tm=True

def glob():
    global Bg,Fc,Bc,Bt,Fcb,Tl,Tm
    Bg = True
    Fc=True
    Bc=True
    Bt=True
    Fcb=True
    Tl=True
    Tm=True

def main ():
    inicio = True
    while inicio:
        #music()
        tela.fill(bg(Bg))
        texto("Labirinto magico",fc(Fc),60,l/6, a/6)
        pygame.draw.rect(tela,bc(Bc), [80, 140, 150, 300], 5, border_radius=15)
        texto("Teclado",fc(Fc),50,90,150)
        pygame.draw.rect(tela,bt(Bt), [90,200,130,50])
        texto("Medio(1)",fcb(Fcb),30,125,215)
        pygame.draw.rect(tela,bt(Bt), [90,260,130,50])
        texto("Dificil(2)",fcb(Fcb),30,125,275)
        pygame.draw.rect(tela,bt(Bt), [90,380,130,50])
        texto("Insano(3)",fcb(Fcb),30,125,400)
        pygame.draw.rect(tela, bc(Bc), [250,140,150,300], 5, border_radius=15)
        texto("Mouse",fc(Fc),50,270,150)
        pygame.draw.rect(tela,bt(Bt), [260,200,130,50])
        texto("Medio(4)",fcb(Fcb),30,270,215)
        pygame.draw.rect(tela,bt(Bt), [260,260,130,50])
        texto("Dificil(5)",fcb(Fcb),30,270,275)
        pygame.draw.rect(tela,bt(Bt), [260,380,130,50])
        texto("Insano(6)",fcb(Fcb),30,270,400)
        pygame.draw.rect(tela,color_red, [350,0,150,50])
        texto("Sair",color_branco,30,415,5)
        texto("(esc)",color_branco,30,415,30)
        #*pygame.draw.rect(tela,bt(Bt), [12,12,44,44], border_radius=15)
        #*pygame.draw.rect(tela,bc(Bc), [10, 10, 50, 50], 5, border_radius=15)
        #*img(Tl)
        pygame.display.update()
        for event in pygame.event.get():
                if event.type == pygame.QUIT:pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        inicio = False
                        t=1
                        i=2
                        jogo1(i,t)
                    if event.key == pygame.K_2:
                        inicio = False
                        t=1
                        i=1
                        jogo1(i,t)
                    if event.key == pygame.K_3:
                        inicio = False
                        t=2
                        i=1
                        jogo1(i)
                    if event.key == pygame.K_4:
                        inicio = False
                        t=1
                        i=2
                        jogo2(i,t)
                    if event.key == pygame.K_5:
                        inicio = False
                        t=1
                        i=1
                        jogo2(i,t)
                    if event.key == pygame.K_6:
                        inicio = False
                        t=2
                        i=1
                        jogo2(i,t)
                    #*if event.key == pygame.K_TAB:
                    #*    tema(Tm,Bg,Fc,Bc,Bt,Fcb,Tl)
                    #*    pygame.display.update()
                        
                    if event.key == pygame.K_ESCAPE:pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    if x > 90 and y > 200 and x < 220 and y < 250:
                        inicio = False
                        t=1
                        i=2
                        jogo1(i,t)
                    if x > 90 and y > 260 and x < 220 and y < 310:
                        inicio = False
                        t=1
                        i=1
                        jogo1(i,t)
                    if x > 90 and y > 380 and x < 220 and y < 430:
                        inicio = False
                        t=2
                        i=1
                        jogo1(i,t)
                    if x > 260 and y > 200 and x < 390 and y < 250:
                        inicio = False
                        t=1
                        i=2
                        jogo2(i,t)
                    if x > 260 and y > 260 and x < 390 and y < 310:
                        inicio = False
                        t=1
                        i=1
                        jogo2(i,t)
                    if x > 260 and y > 380 and x < 390 and y < 430:
                        inicio = False
                        t=2
                        i=1
                        jogo2(i,t)
                    #*if x > 10 and y > 10 and x < 60 and y < 60:
                    #*    tema(Tm,Bg,Fc,Bc,Bt,Fcb,Tl)
                    if x > 350 and y > 0 and x < 500 and y < 50:pygame.quit()
def jogo1(i,t):
    run = True
    fimdejogo = False
    lf=3
    lv=1
    pts=0
    color_obj=random_Color()
    mov_x=223
    imov_x=223
    w=40
    w2=476
    tam=20
    h2=100
    h=10
    color_obt=random_Color()
    color_fin=random_Color()
    xF=13
    yF=376
    color_cnt=random_Color()
    vel1=2
    vel2=2
    if t==2:
        vel1=vel(vel1)
        vel2=vel(vel2)
    A=50
    B=70
    velo=2
    Lv=1
    while run:
        while fimdejogo:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    fimdejogo = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        run = True
                        fimdejogo = False
                        lf=3
                        lv=1
                        pts=0
                        color_obj=random_Color()
                        mov_x=223
                        imov_x=223
                        w=40
                        w2=476
                        tam=20
                        h2=100
                        h=10
                        color_obt=random_Color()
                        color_fin=random_Color()
                        xF=13
                        yF=376
                        color_cnt=random_Color()
                        vel1=2
                        vel2=2
                        if t==2:
                            vel1=vel(vel1)
                            vel2=vel(vel2)
                        velo=2
                        A=50
                        B=70
                        Lv=1
                    if event.key == pygame.K_ESCAPE:
                        run = False
                        fimdejogo = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    if x > 60 and y > 210 and x < 210 and y < 260:
                        run = True
                        fimdejogo = False
                        lf=3
                        lv=1
                        pts=0
                        color_obj=random_Color()
                        mov_x=223
                        imov_x=223
                        w=40
                        w2=476
                        tam=20
                        h2=100
                        h=10
                        color_obt=random_Color()
                        color_fin=random_Color()
                        xF=13
                        yF=376
                        color_cnt=random_Color()
                        vel1=2
                        vel2=2
                        if t==2:
                            vel1=vel(vel1)
                            vel2=vel(vel2)
                        velo=2
                        A=50
                        B=70
                        Lv=1
                    if x > 260 and y > 210 and x < 410 and y < 260:
                        run = False
                        fimdejogo = False
                go(pts)
        for event in pygame.event.get():
            #music()
            tela.fill((20,25,6))
            placar(lf,pts,lv)
            if event.type == pygame.QUIT:run = False
            if lf==0: fimdejogo = True
            if pygame.key.get_pressed()[K_a]:A-=velo
            if pygame.key.get_pressed()[K_d]:A+=velo
            if pygame.key.get_pressed()[K_w]:B-=velo
            if pygame.key.get_pressed()[K_s]:B+=velo
            mov_x+=vel1
            imov_x-=vel2
            pec = pygame.draw.rect(tela,(color_obj), (A,B, tam,tam))
            obt1 = pygame.draw.rect(tela, (color_obt), (mov_x,100,w,h))
            obt2 = pygame.draw.rect(tela, (color_obt), (imov_x-10,150,w,h))
            obt3 = pygame.draw.rect(tela, (color_obt), (mov_x,200,w,h))
            obt4 = pygame.draw.rect(tela, (color_obt), (imov_x-10,250,w,h))
            obt5 = pygame.draw.rect(tela, (color_obt), (mov_x,300,w,h))
            obt6 = pygame.draw.rect(tela, (color_obt), (imov_x-10,350,w,h))
            fin = pygame.draw.rect(tela,(color_fin),(xF,yF,w2,h2))
            li= pygame.draw.line(tela, (color_cnt), (490,480), (490,0), 5)
            lu= pygame.draw.line(tela, (color_cnt), (10,0), (10,480), 5)
            la= pygame.draw.line(tela, (color_cnt), (8,2), (490,2), 5)
            le= pygame.draw.line(tela, (color_cnt), (8,480), (490,480), 5)
            lt= pygame.draw.line(tela, (color_cnt), (8,50), (490,50), 5)
            pygame.display.update()

            if Lv == 10:
                Lv=1
                tam=20

            if pec.colliderect( fin):
                    passou()
                    pts+=100
                    lf+=1
                    lv+=1
                    w+=10
                    tam-=1.5
                    w2-=3
                    h2-=3
                    yF+=3
                    h+=2
                    colorcnt=random_Color()
                    colorobt=random_Color()
                    colorfin=random_Color()
                    colorobj=random_Color()
                    Lv+=1
                    if t==1:
                        vel1+=4
                        vel2+=4
                    else:
                        vel1=vel(vel1)
                        vel2=vel(vel2)
                    A=50
                    B=70
                    movx=223
                    imovx=223
                    velo=velO(velo)

            if i==1:
                if pec.colliderect( li):
                    colidiu()
                    pts-=10
                    lf-=1
                    A=50
                    B=70

                if pec.colliderect( lu):
                    colidiu()
                    pts-=10
                    lf-=1
                    A=50
                    B=70

                if pec.colliderect( la):
                    #colidiu()
                    pts-=10
                    lf=lf-1
                    A=50
                    B=70

                if pec.colliderect( lt):
                    colidiu()
                    pts-=10
                    lf-=1
                    A=50
                    B=70
            else:
                if pec.colliderect( li):
                    A-=2
                    B-=2

                if pec.colliderect( lu):
                    A+=2
                    B+=2

                if pec.colliderect( la):
                    A+=2
                    B-=2

                if pec.colliderect( lt):
                    A-=2
                    B+=2

            if pec.colliderect( obt1):
                colidiu()
                pts-=10
                lf-=1
                A=50
                B=70

            if pec.colliderect( obt2):
                colidiu()
                pts-=10
                lf-=1
                A=50
                B=70

            if pec.colliderect( obt3):
                colidiu()
                pts-=10
                lf-=1
                A=50
                B=70

            if pec.colliderect( obt4):
                colidiu()
                pts-=10
                lf-=1
                A=50
                B=70

            if pec.colliderect( obt5):
                colidiu()
                pts-=10
                lf-=1
                A=50
                B=70

            if pec.colliderect( obt6):
                colidiu()
                pts-=10
                lf-=1
                A=50
                B=70

            if obt1.colliderect(li):vel1*=-1
            if obt1.colliderect(lu):vel1*=-1
            if obt2.colliderect(li):vel2*=-1
            if obt2.colliderect(lu):vel2*=-1
            if obt3.colliderect(li):vel1*=-1
            if obt3.colliderect(lu):vel1*=-1
            if obt4.colliderect(li):vel2*=-1
            if obt4.colliderect(lu):vel2*=-1
            if obt5.colliderect(li):vel1*=-1
            if obt5.colliderect(lu):vel1*=-1
            if obt6.colliderect(li):vel2*=-1
            if obt6.colliderect(lu):vel2*=-1

            #*inv(obt1,li,vel1)
            #*inv(obt1,lu,vel1)
            #*inv(obt2,li,vel2)
            #*inv(obt2,lu,vel2)
            #*inv(obt3,li,vel1)
            #*inv(obt3,lu,vel1)
            #*inv(obt4,li,vel2)
            #*inv(obt4,lu,vel2)
            #*inv(obt5,li,vel1)
            #*inv(obt5,lu,vel1)
            #*inv(obt6,li,vel2)
            #*inv(obt6,lu,vel2)
            
def jogo2(i,t):
    run = True
    fimdejogo = False
    lf=3
    lv=1
    pts=0
    color_obj=random_Color()
    mov_x=223
    imov_x=223
    w=40
    w2=476
    tam=20
    h2=100
    h=10
    color_obt=random_Color()
    color_fin=random_Color()
    xF=13
    yF=376
    color_cnt=random_Color()
    vel1=2
    vel2=2
    if t==2:
        vel1=vel(vel1)
        vel2=vel(vel2)
    A=50
    B=70
    Lv=1
    pos(A,B)
    while run:
        while fimdejogo:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    fimdejogo = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        run = True
                        fimdejogo = False
                        lf=3
                        lv=1
                        pts=0
                        color_obj=random_Color()
                        mov_x=223
                        imov_x=223
                        w=40
                        w2=476
                        tam=20
                        h2=100
                        h=10
                        color_obt=random_Color()
                        color_fin=random_Color()
                        xF=13
                        yF=376
                        color_cnt=random_Color()
                        vel1=2
                        vel2=2
                        if t==2:
                            vel1=vel(vel1)
                            vel2=vel(vel2)
                        A=50
                        B=70
                        Lv=1
                        pos(A,B)
                    if event.key == pygame.K_ESCAPE:
                        run = False
                        fimdejogo = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    if x > 60 and y > 210 and x < 210 and y < 260:
                        run = True
                        fimdejogo = False
                        lf=3
                        lv=1
                        pts=0
                        color_obj=random_Color()
                        mov_x=223
                        imov_x=223
                        w=40
                        w2=476
                        tam=20
                        h2=100
                        h=10
                        color_obt=random_Color()
                        color_fin=random_Color()
                        xF=13
                        yF=376
                        color_cnt=random_Color()
                        vel1=2
                        vel2=2
                        if t==2:
                            vel1=vel(vel1)
                            vel2=vel(vel2)
                        A=50
                        B=70
                        Lv=1
                        pos(A,B)
                    if x > 260 and y > 210 and x < 410 and y < 260:
                        run = False
                        fimdejogo = False
                go(pts)
        for event in pygame.event.get():
            tela.fill(bg(Bg))
            placar(lf,pts,lv)
            if event.type == pygame.QUIT:run = False
            if lf==0: fimdejogo = True
            mov_x+=vel1
            imov_x-=vel2
            pec = pygame.Rect(A,B,tam,tam)
            pecm(pec,color_obj)
            obt1 = pygame.draw.rect(tela, (color_obt), (mov_x,100,w,h))
            obt2 = pygame.draw.rect(tela, (color_obt), (imov_x,150,w,h))
            obt3 = pygame.draw.rect(tela, (color_obt), (mov_x,200,w,h))
            obt4 = pygame.draw.rect(tela, (color_obt), (imov_x,250,w,h))
            obt5 = pygame.draw.rect(tela, (color_obt), (mov_x,300,w,h))
            obt6 = pygame.draw.rect(tela, (color_obt), (imov_x,350,w,h))
            fin = pygame.draw.rect(tela,(color_fin),(xF,yF,w2,h2))
            li= pygame.draw.line(tela, (color_cnt), (490,480), (490,1), 5)
            lu= pygame.draw.line(tela, (color_cnt), (10,0), (10,480), 5)
            la= pygame.draw.line(tela, (color_cnt), (8,2), (490,2), 5)
            le= pygame.draw.line(tela, (color_cnt), (8,480), (490,480), 5)
            lt= pygame.draw.line(tela, (color_cnt), (8,50), (490,50), 5)
            pygame.display.update()

            if Lv == 10:
                Lv=1
                tam=20

            if pec.colliderect( fin):
                passou()
                pts+=100
                lf+=1
                lv+=1
                w+=10
                tam-=1.5
                w2-=3
                h2-=3
                yF+=3
                h+=2
                color_cnt=random_Color()
                color_obt=random_Color()
                color_fin=random_Color()
                color_obj=random_Color()
                Lv+=1

                if t==1:
                    vel1+=4
                    vel2+=4
                else:
                    vel1=vel(vel1)
                    vel2=vel(vel2)
                pos(A,B)
                mov_x=250
                imov_x=250

            if i==1:
                if pec.colliderect( li):
                    colidiu()
                    pts-=10
                    lf-=1
                    pos(A,B)

                if pec.colliderect( lu):
                    colidiu()
                    pts-=10
                    lf-=1
                    pos(A,B)

                if pec.colliderect( la):
                    colidiu()
                    pts-=10
                    lf-=1
                    pos(A,B)

                if pec.colliderect( lt):
                    colidiu()
                    pts-=10
                    lf-=1
                    pos(A,B)

            else:
                if pec.colliderect( li):
                    A-=2
                    B-=2
                    pos(A,B)

                if pec.colliderect( lu):
                    A+=2
                    B+=2
                    pos(A,B)

                if pec.colliderect( la):
                    A+=2
                    B-=2
                    pos(A,B)

                if pec.colliderect( lt):
                    A-=2
                    B+=2
                    pos(A,B)

            if pec.colliderect( obt1):
                colidiu()
                pts-=10
                lf-=1
                pos(A,B)

            if pec.colliderect( obt2):
                colidiu()
                pts-=10
                lf-=1
                pos(A,B)

            if pec.colliderect( obt3):
                colidiu()
                pts-=10
                lf-=1
                pos(A,B)

            if pec.colliderect( obt4):
                colidiu()
                pts-=10
                lf-=1
                pos(A,B)

            if pec.colliderect( obt5):
                colidiu()
                pts-=10
                lf-=1
                pos(A,B)

            if pec.colliderect( obt6):
                colidiu()
                pts-=10
                lf-=1
                pos(A,B)
            
            if obt1.colliderect(li):vel1*=-1
            if obt1.colliderect(lu):vel1*=-1
            if obt2.colliderect(li):vel2*=-1
            if obt2.colliderect(lu):vel2*=-1
            if obt3.colliderect(li):vel1*=-1
            if obt3.colliderect(lu):vel1*=-1
            if obt4.colliderect(li):vel2*=-1
            if obt4.colliderect(lu):vel2*=-1
            if obt5.colliderect(li):vel1*=-1
            if obt5.colliderect(lu):vel1*=-1
            if obt6.colliderect(li):vel2*=-1
            if obt6.colliderect(lu):vel2*=-1

            #*inv(obt1,li,vel1)
            #*inv(obt1,lu,vel1)
            #*inv(obt2,li,vel2)
            #*inv(obt2,lu,vel2)
            #*inv(obt3,li,vel1)
            #*inv(obt3,lu,vel1)
            #*inv(obt4,li,vel2)
            #*inv(obt4,lu,vel2)
            #*inv(obt5,li,vel1)
            #*inv(obt5,lu,vel1)
            #*inv(obt6,li,vel2)
            #*inv(obt6,lu,vel2)
main()
pygame.quit()
