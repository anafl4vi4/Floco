import turtle
t = turtle 
t.pensize(5)
c: str = t.color
t.speed(3)

# 4 segmentos de reta
def losango(tamanho, zoom: int = 1, posx=1, posy=1):
    t.up()
    c("navy")
    t.goto(posx*60, posy*60) 
    t.down()

    for _ in range(2):
        t.fd(tamanho*zoom)
        turtle.left(60)
        t.fd(tamanho*zoom)
        t.left(120)
        pass
    pass

# Os args zoom, x e y também deveriam aparecer aqui
def flor_losango(t_losango):
    for _ in range(5):
        losango(t_losango)
        t.right(72)
        pass
input("pressione enter ")

flor_losango(150)
losango(30, 0.5, -50, -50)
t.done()