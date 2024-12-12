import turtle
t = turtle
c = t.color
def losango(tamanho, zoom: int = 1, posx=1, posy=1):
    c("navy")
    turtle.penup()
    turtle.goto(posx*60, posy*60)
    turtle.pendown()
    for _ in range(2):
        turtle.forward(tamanho*zoom)
        turtle.left(60)
        turtle.forward(tamanho*zoom)
        turtle.left(120)
        pass
        
def floco(tamanho_losango):
    turtle.speed(2)
    for _ in range(5):
        losango(zoom=9, tamanho=20)
        losango(tamanho_losango)
        turtle.right(72)  
        pass

floco (100)

turtle.done
