import turtle
import winsound

win = turtle.Screen()
win.title("Pong by Matthew")
win.bgcolor("midnight blue")
win.setup(width=800,height=600)
win.tracer(0)

#paddel a
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)
#paddle b
paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.30
ball.dy = 0.30

#score
scoreA = 0
scoreB = 0

#scoreLabel
pen = turtle.Turtle()
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write(" Player 1: 0      Player 2: 0 ", align="center",font=("Courier",24,"bold"))

#Field
circle = turtle.Turtle()
circle.color("white")
circle.penup()
circle.pensize(8)
circle.goto(0,-70)
circle.pendown()
circle.circle(60)
circle.left(90)
circle.goto(0,300)
circle.right(180)
circle.goto(0,-600)
circle.penup



#functions
def paddle_a_up():
    y = paddle_a.ycor()
    y+=20
    paddle_a.sety(y)
def paddle_a_down():
    y = paddle_a.ycor()
    y-=20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y+=20
    paddle_b.sety(y)
def paddle_b_down():
    y = paddle_b.ycor()
    y-=20
    paddle_b.sety(y)




#keyboardBinding
win.listen()
win.onkeypress(paddle_a_up,'w')
win.onkeypress(paddle_a_down,"s")
win.onkeypress(paddle_b_up,'Up')
win.onkeypress(paddle_b_down,"Down")



#main game loop
while True:
    win.update()

    #move ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #check borders
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*=-1
        winsound.PlaySound("C:\\Users\\matti\\.vscode\\Projects\\pong\\bounce.wav",  winsound.SND_ASYNC)
    
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy*=-1
        winsound.PlaySound("C:\\Users\\matti\\.vscode\\Projects\\pong\\bounce.wav",  winsound.SND_ASYNC)
    
    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx *=-1
        winsound.PlaySound("C:\\Users\\matti\\.vscode\\Projects\\pong\\cling_1.wav",  winsound.SND_ASYNC)
        scoreA+=1
        pen.clear()
        pen.write(f" Player 1: {scoreA}      Player 2: {scoreB} ", align="center",font=("Courier",24,"bold"))

        #game over
        if(scoreA==3):
            win.clear()
            win.bgcolor("midnight blue")
            pen.clear()
            pen.color("white")
            pen.goto(0,0)
            pen.write("Game Over, Player 1 Wins!!",align="center",font=("Courier",30,"bold"))

    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx *=-1
        winsound.PlaySound("C:\\Users\\matti\\.vscode\\Projects\\pong\\cling_2.wav",  winsound.SND_ASYNC)
        scoreB+=1
        pen.clear()
        pen.write(f" Player 1: {scoreA}      Player 2: {scoreB} ", align="center",font=("Courier",24,"bold"))
        
        #game over
        if(scoreB==3):
            win.clear()
            win.bgcolor("midnight blue") 
            pen.clear()
            pen.goto(0,0)
            pen.color("white")
            pen.write("Game Over, Player 2 Wins!!",align="center",font=("Courier",30,"bold"))

    #paddel check collision
    if (ball.xcor() > 340 and ball.xcor() <350) and (ball.ycor() < paddle_b.ycor()+40 and ball.ycor()> paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *=-1
        winsound.PlaySound("C:\\Users\\matti\\.vscode\\Projects\\pong\\bounce.wav",  winsound.SND_ASYNC)
    
    if (ball.xcor() < -340 and ball.xcor() >-350) and (ball.ycor() < paddle_a.ycor()+40 and ball.ycor()> paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *=-1
        winsound.PlaySound("C:\\Users\\matti\\.vscode\\Projects\\pong\\bounce.wav",  winsound.SND_ASYNC)


    