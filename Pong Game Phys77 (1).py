import turtle
import random
import winsound

#Screen set-up
window = turtle.Screen()
window.title("Pong Game")
window.bgcolor("blue")
window.setup(width=600, height=400)


#Paddle initialization
left_paddle = turtle.Turtle()
left_paddle.shape("circle")
left_paddle.color("red")
left_paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle.penup() #Lifts pen off of screen so it doesn't create weird lines
left_paddle.goto(-250, 0)

right_paddle = turtle.Turtle()
right_paddle.shape("circle")
right_paddle.color("red")
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.penup()
right_paddle.goto(250, 0)

#Creating the ball
ball = turtle.Turtle()
ball.speed(1)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 4
ball.dy = -4

#Score creation
score_a = 0
score_b = 0
score = turtle.Turtle()
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 150)
score.write("Player A:" + str(score_a) + "Player B:" + str(score_b), align="center", font=("Courier", 18, "normal"))

#Lets you choose how long the game will go on
L=turtle.numinput("Best of how many?", "input a number to set the score", default=3, minval=1, maxval=10)

#Paddle movement
def left_paddle_up():
    if left_paddle.ycor() < 150:
        y = left_paddle.ycor()
        y += 10
        left_paddle.sety(y)

def left_paddle_down():
    if left_paddle.ycor() > -150:
        y = left_paddle.ycor()
        y -= 10
        left_paddle.sety(y)

def right_paddle_up():
    if right_paddle.ycor() < 150:
        y = right_paddle.ycor()
        y += 10
        right_paddle.sety(y)

def right_paddle_down():
    if right_paddle.ycor() > -150:
        y = right_paddle.ycor()
        y -= 10
        right_paddle.sety(y)

#Keyboard bindings
window.listen()
window.onkeypress(left_paddle_up, "w")
window.onkeypress(left_paddle_down, "s")
window.onkeypress(right_paddle_up, "Up")
window.onkeypress(right_paddle_down, "Down")


#Game sound effects
def bounce():
    winsound.PlaySound('mixkit-game-ball-tap-2073.wav', winsound.SND_ASYNC)
def begin():
    winsound.PlaySound('mixkit-unlock-game-notification-253.wav',winsound.SND_ASYNC)
def end():
    winsound.PlaySound('mixkit-player-losing-or-failing-2042.wav',winsound.SND_ASYNC)
begin()
while True: #Game loop to keep game running and updated
    window.update() #Updates screen


    #Move ball
    ball.setx(ball.xcor() + (ball.dx) * 2)
    ball.sety(ball.ycor() + (ball.dy) * 2)

    #Collisions with walls and direction of ball
    if ball.ycor() > 200 or ball.ycor() < -200:
        ball.dy *= -1
        bounce()

    rando = [1, -1]
    if ball.xcor() > 300 or ball.xcor() < -300:
        ball.goto(0, 0)
        num = random.choice(rando)
        ball.dx *= num

    #Collisions with paddles
    if (ball.xcor() > 240 and ball.xcor() < 250) and (ball.ycor() < right_paddle.ycor() + 50 and ball.ycor() > right_paddle.ycor() - 50):
        ball.dx *= -1
        score_b += 1
        bounce()
        score.clear()
        score.write("Player A: " + str(score_a) +  " Player B: " + str(score_b), align="center", font=("Courier", 18, "normal"))

    if (ball.xcor() < -240 and ball.xcor() > -250) and (ball.ycor() < left_paddle.ycor() + 50 and ball.ycor() > left_paddle.ycor() - 50):
        ball.dx *= -1
        score_a += 1
        bounce()
        score.clear()
        score.write("Player A: " + str(score_a) +  " Player B: " + str(score_b), align="center", font=("Courier", 18, "normal"))
    
    if score_a == L or score_b == L:
        score.clear()
        score.write("Game Over", align="center", font=("Courier", 24, "normal"))
        score.goto(0, 130)
        score.write("Close screen to leave", align="center", font=("Courier", 15, "normal"))
        end()
        ball.goto(0, 0)
        ball.dx = 0
        ball.dy = 0
        window.exitonclick()
        

        