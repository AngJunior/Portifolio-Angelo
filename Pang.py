import turtle

# Janela
win = turtle.Screen()
win.title("Pang")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# Raquete A
raquete_a = turtle.Turtle()
raquete_a.speed(0)
raquete_a.shape("square")
raquete_a.color("red")
raquete_a.shapesize(stretch_wid=6, stretch_len=1)
raquete_a.penup()
raquete_a.goto(-350, 0)

# Raquete B
raquete_b = turtle.Turtle()
raquete_b.speed(0)
raquete_b.shape("square")
raquete_b.color("blue")
raquete_b.shapesize(stretch_wid=6, stretch_len=1)
raquete_b.penup()
raquete_b.goto(350, 0)

# Bola
bola = turtle.Turtle()
bola.speed(1)
bola.shape("circle")
bola.color("white")
bola.penup()
bola.goto(0, 0)
bola.dx = 0.2
bola.dy = 0.2

# Placar
placar_a = 0
placar_b = 0
placar = turtle.Turtle()
placar.speed(0)
placar.color("white")
placar.penup()
placar.hideturtle()
placar.goto(0, 260)
placar.write("Player 1: 0  Player 2: 0", align="center", font=("Courier", 20, "normal"))

# Funções
def raquete_a_cima():
    y = raquete_a.ycor()
    if y < 250:
        raquete_a.sety(y + 20)

def raquete_a_baixo():
    y = raquete_a.ycor()
    if y > -250:
        raquete_a.sety(y - 20)

def raquete_b_cima():
    y = raquete_b.ycor()
    if y < 250:
        raquete_b.sety(y + 20)

def raquete_b_baixo():
    y = raquete_b.ycor()
    if y > -250:
        raquete_b.sety(y - 20)

# Controles
win.listen()
win.onkeypress(raquete_a_cima, "w")
win.onkeypress(raquete_a_baixo, "s")
win.onkeypress(raquete_b_cima, "Up")
win.onkeypress(raquete_b_baixo, "Down")

# Loop principal
while True:
    win.update()

    # Movimento da bola
    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)

    # Bordas
    if bola.ycor() > 290:
        bola.sety(290)
        bola.dy *= -1

    if bola.ycor() < -290:
        bola.sety(-290)
        bola.dy *= -1

    if bola.xcor() > 390:
        bola.goto(0, 0)
        bola.dx *= -1
        placar_a += 1
        placar.clear()
        placar.write(f"Player 1: {placar_a}  Player 2: {placar_b}", align="center", font=("Courier", 20, "normal"))

    if bola.xcor() < -390:
        bola.goto(0, 0)
        bola.dx *= -1
        placar_b += 1
        placar.clear()
        placar.write(f"Player 1: {placar_a}  Player 2: {placar_b}", align="center", font=("Courier", 20, "normal"))

    # Colisão com as raquetes
    if (340 < bola.xcor() < 350) and (raquete_b.ycor() - 50 < bola.ycor() < raquete_b.ycor() + 50):
        bola.setx(340)
        bola.dx *= -1

    if (-350 < bola.xcor() < -340) and (raquete_a.ycor() - 50 < bola.ycor() < raquete_a.ycor() + 50):
        bola.setx(-340)
        bola.dx *= -1
