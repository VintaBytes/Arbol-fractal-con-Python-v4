import turtle
import random
import time

#Variables globales
ANG = 15       #ángulo de inclinación para las ramas
RAND = 5      #factor de aleatoriedad del ángulo de inclinación (grados)
REL = 4/5      #relación entre la rama y las sub ramas
RANDT = 60     #factor de aleatoriedad en el tamaño de las ramas (%)
GROSORTRONCO = 0        #pixeles que se le suman al grosor del árbol
TAMINIC = 100           #tamaño del tronco inicial en pixeles
TAMHOJA = 28             #tamaño de la hoja
ANGHOJA = 60    #ángulo de las puntas de las hojas (180 = círculos)
PROF = 11        #cantidad de niveles en el árbol (más de 10 puede durar mucho dibujándose)

CTRONCO = (165,42,42)  #color del tronco. tres números entre 0 y 255
CTRONCOVAR = 15         #factor de aleatoriedad en el color del tronco
CHOJAS =  (250,140,30)  #color de las hojas
CHOJASVAR = 80         #factor de aleatoriedad en el color de las hojas
CFONDO = (255,255,255)  #color de fondo

# Función que dibuja un árbol fractal
# Entradas:
#   t: tamaño del segmento inicial en pixeles
#   d: profundidad total del árbol
# Salidas:
#   Dibujo del árbol en pantalla
# Restricciones: no
def arbol(t, d):
    if d==0:
        turtle.forward(t)
        hoja(TAMHOJA, ANGHOJA)
        turtle.penup()
        turtle.back(t)
        turtle.pendown()
        turtle.color(CTRONCO)
        return
    else:
        if  (random.randrange(1,100) > 10) or (d > random.randrange(7,PROF)):
            angulo1 = ANG + random.randrange(-RAND, RAND+1)
            angulo2 = ANG + random.randrange(-RAND, RAND+1)
            tamano = t + t*random.randrange(-RANDT, RANDT+1)/100
            colortronco = variacioncolor(CTRONCO, CTRONCOVAR)
            turtle.color(colortronco)
            turtle.pensize(d+GROSORTRONCO)
            turtle.forward(tamano)
            turtle.left(angulo1)
            arbol(t*REL, d-1)
            turtle.right(angulo1+angulo2)
            arbol(t*REL, d-1)
            turtle.color(colortronco)
            turtle.left(angulo2)
            turtle.penup()
            turtle.back(tamano)
            turtle.pendown()

# Función que dibuja una hoja
# Entradas:
#   t: tamaño de la hoja
#   a: ángulo de las puntas de las hojas
# Salidas:
#   Dibujo de una hoja en la posición actual de la tortuga
# Restricciones: no
def hoja(t, a):
    turtle.color(variacioncolor(CHOJAS, CHOJASVAR))
    turtle.begin_fill()
    turtle.right(a/2)
    turtle.circle(t, a)
    turtle.left(180-a)
    turtle.circle(t, a)
    turtle.left(180-a/2)
    turtle.end_fill()

# Función que genera una variación de un color en RGB
# Entradas:
#   color: tupla con tres valores enteros entre 0 y 255
#   var: cantidad máxima de variación permitida en los valores RGB
# Salidas:
#   Tupla de tres valores enteros entre 0 y 255 que es una variación
#   del color original.
# Restricciones: no
def variacioncolor(color, var):
    Rd = random.randrange(-var, var+1)
    Gd = random.randrange(-var, var+1)
    Bd = random.randrange(-var, var+1)
    R, G, B = color
    R += Rd
    G += Gd
    B += Bd
    if R > 255:
        R = 255
    elif R < 0:
        R = 0
    if G > 255:
        G = 255
    elif G < 0:
        G = 0
    if B > 255:
        B = 255
    elif B < 0:
        B = 0
    return R, G, B

# Función que inicializa la posición de la tortuga e invoca a la función
# de dibujar árbol fractal.
def init():
    turtle.speed(0)
    turtle.colormode(255)
    turtle.clear()
    turtle.penup()
    turtle.home()
    #turtle.goto(0,-350)
    turtle.left(90)
    turtle.back(200)
    turtle.pendown()
    turtle.hideturtle()
    turtle.color(CTRONCO)
    turtle.bgcolor(CFONDO)
    arbol(TAMINIC, PROF)
    turtle.done()


turtle.setup(1024, 800, 0, 0)
turtle.penup()
turtle.pendown()
time.sleep(1)          
init()
turtle.exitonclick()
