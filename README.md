# Arbol Fractal en Python (L-System) V4.

Otro script que utiliza la librería `turtle` en Python para dibujar un árbol "otoñal" fractal. 
Para ejecutarlo, simplemente guarda el código en un archivo y ejecútalo en un entorno de Python que soporte la librería `turtle`.

<span><img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue"/></span>
<span><img src="https://img.shields.io/badge/VSCode-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white"/></span>

## Resultado
<img src="https://github.com/VintaBytes/Arbol-fractal-con-Python-v4/blob/main/lsystem-23.png?raw=true" width="640px">

## Descripción del Código

### Importaciones y Variables Globales

El código comienza importando las librerías necesarias:
```python
import turtle
import random
import time
```
Luego, se definen varias variables globales que controlan los parámetros del dibujo:
```python
ANG = 15       # ángulo de inclinación para las ramas
RAND = 5       # factor de aleatoriedad del ángulo de inclinación (grados)
REL = 4/5      # relación entre la rama y las sub ramas
RANDT = 60     # factor de aleatoriedad en el tamaño de las ramas (%)
GROSORTRONCO = 0   # píxeles que se le suman al grosor del árbol
TAMINIC = 100  # tamaño del tronco inicial en píxeles
TAMHOJA = 28   # tamaño de la hoja
ANGHOJA = 60   # ángulo de las puntas de las hojas (180 = círculos)
PROF = 11      # cantidad de niveles en el árbol (más de 10 puede durar mucho dibujándose)

CTRONCO = (165, 42, 42)  # color del tronco
CTRONCOVAR = 15          # factor de aleatoriedad en el color del tronco
CHOJAS = (250, 140, 30)  # color de las hojas
CHOJASVAR = 80           # factor de aleatoriedad en el color de las hojas
CFONDO = (255, 255, 255) # color de fondo
```

### Función `arbol`

Esta función dibuja un árbol fractal utilizando recursión:
```python
def arbol(t, d):
    if d == 0:
        turtle.forward(t)
        hoja(TAMHOJA, ANGHOJA)
        turtle.penup()
        turtle.back(t)
        turtle.pendown()
        turtle.color(CTRONCO)
        return
    else:
        if (random.randrange(1, 100) > 10) or (d > random.randrange(7, PROF)):
            angulo1 = ANG + random.randrange(-RAND, RAND + 1)
            angulo2 = ANG + random.randrange(-RAND, RAND + 1)
            tamano = t + t * random.randrange(-RANDT, RANDT + 1) / 100
            colortronco = variacioncolor(CTRONCO, CTRONCOVAR)
            turtle.color(colortronco)
            turtle.pensize(d + GROSORTRONCO)
            turtle.forward(tamano)
            turtle.left(angulo1)
            arbol(t * REL, d - 1)
            turtle.right(angulo1 + angulo2)
            arbol(t * REL, d - 1)
            turtle.color(colortronco)
            turtle.left(angulo2)
            turtle.penup()
            turtle.back(tamano)
            turtle.pendown()
```

### Función `hoja`

Dibuja una hoja en la posición actual del turtle:
```python
def hoja(t, a):
    turtle.color(variacioncolor(CHOJAS, CHOJASVAR))
    turtle.begin_fill()
    turtle.right(a / 2)
    turtle.circle(t, a)
    turtle.left(180 - a)
    turtle.circle(t, a)
    turtle.left(180 - a / 2)
    turtle.end_fill()
```

### Función `variacioncolor`

Genera una variación de un color en RGB:
```python
def variacioncolor(color, var):
    Rd = random.randrange(-var, var + 1)
    Gd = random.randrange(-var, var + 1)
    Bd = random.randrange(-var, var + 1)
    R, G, B = color
    R += Rd
    G += Gd
    B += Bd
    R = min(max(0, R), 255)
    G = min(max(0, G), 255)
    B = min(max(0, B), 255)
    return R, G, B
```

### Función `init`

Inicializa la posición del turtle e invoca la función de dibujar el árbol fractal:
```python
def init():
    turtle.speed(0)
    turtle.colormode(255)
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.left(90)
    turtle.back(200)
    turtle.pendown()
    turtle.hideturtle()
    turtle.color(CTRONCO)
    turtle.bgcolor(CFONDO)
    arbol(TAMINIC, PROF)
    turtle.done()
```

### Configuración y Ejecución

Configura el entorno del turtle y llama a la función de inicialización:
```python
turtle.setup(1024, 800, 0, 0)
turtle.penup()
turtle.pendown()
time.sleep(1)          
init()
turtle.exitonclick()
```

