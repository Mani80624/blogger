
from graphics import*

# Se crea una nueva ventana con el nombre de graficador y dimesiones 200*200
win = GraphWin("Graficador", width = 200, height = 200)
# Se cambia el color de fondo
win.setBackground(color_rgb(128,128,255))

"""Establece el sistema de coordenadas de la ventana.
La esquina inferior izquierda es (-10,-10) y la esquina superior derecha es(10,10)"""
win.setCoords(-10,-10,10,10)

# Definimos la coordenada del punto
punto = Point(0,0)
# Mostramos el punto en la ventana
punto.draw(win)

"""
# Función Circle(Point(coordenadas), radio)
cir = Circle(punto,3)
#cir = Circle(Point(0,0),3)
# Color de la circunferencia
cir.setOutline(color_rgb(255,255,0))
# Color del circulo
cir.setFill(color_rgb(63,72,204))
# Dibujamos el circulo de radio 3
cir.draw(win)


# Creación de un poligono
poli = Polygon(Point(-3,0), Point(0,3), Point(3,0), Point(0,-3))
poli.setFill(color_rgb(255,0,255))
poli.setOutline(color_rgb(0,255,255))
# Ancho del contorno en px
poli.setWidth(3)
poli.draw(win)

# Creación de lineas
pt1 = Point(-10,-10)
pt2 = Point(10,10)
lin = Line(pt1, pt2)
lin.setOutline(color_rgb(255,0,0))
lin.draw(win)

# Creación del rectangulo
rectangul = Rectangle(Point(0,0), Point(9,9)) # Se  crea un rectángulo desde (0,0) a (9,9)
rectangul.setFill(color_rgb(255,100,50))
rectangul.draw(win)
"""

# Trazar los ejes coordenados
ejex = Line(Point(-10,0), Point(10,0))
ejex.draw(win)
ejey = Line(Point(0,-10), Point(0,10))
ejey.draw(win)


# Graficando una función en el intervalo -3,3
a = -3
b = 3
n = 100
inc = (b-a)/n
x = a
while x<b:
    punto = Point(x,x*x)
    x += inc
    punto.draw(win)
    
# Detiene la ventana después de cerrar
win.getMouse()
win.close()



