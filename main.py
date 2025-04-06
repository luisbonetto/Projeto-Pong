from turtle import Screen
from raquete import Raquete
from ball import Ball
from scoreboard import Scoreboard
import time

game_is_on = True

screen = Screen()
screen.bgcolor("black")
screen.setup(width= 800, height= 600)
screen.title("My Pong Game")
screen.tracer(0) #Ao usar o "tracer" devemos usar o "update"

r_rqt = Raquete((350, 0))
l_rqt = Raquete((-350, 0))

ball = Ball()
score = Scoreboard()
screen.listen()
screen.onkey(r_rqt.up, "Up")
screen.onkey(r_rqt.down, "Down")

screen.onkeyrelease(l_rqt.up, "w")
screen.onkey(l_rqt.down, "s")

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detecta colisão com a parede
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()

    #Detecta colisão com a raquete direita
    if ball.distance(r_rqt) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    #Detecta colisão com a raquete esquerda
    if ball.distance(l_rqt) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Ponto para esquerda
    if ball.xcor() > 400:
        ball.reset_ball()
        score.l_point()

    #Ponto para direita
    if ball.xcor() < -400:
        ball.reset_ball()
        score.r_point()

screen.exitonclick()