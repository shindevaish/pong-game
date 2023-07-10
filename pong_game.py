import turtle

#screen
screen=turtle.Screen()
screen.bgcolor("cadet blue")
screen.setup(width=1000, height=800)

p=turtle.Turtle()
p.speed(0)
p.penup()
p.color("white")
p.goto(0,180)
p.write("WELCOME TO PONG GAME.",align="center",font=("forte",27,"bold"))
p.hideturtle()

p5=turtle.Turtle()
p5.speed(0)
p5.penup()
p5.color("white")
p5.goto(0,60)
p5.write("                             RULES:\nTo move right paddle up and down - 'i' and 'm' \nTo move left paddle up and down - 'e' and 'x' ",align="center",font=("forte",24,"bold"))
p5.hideturtle()

p1=turtle.Turtle()
p1.penup()
p1.pencolor("white")
p1.goto(0,-200)
p1.write("PRESS SPACE TO TRY A DEMO.\n                     OR\nPRESS 'a' TO START THE GAME",align="center",font=("forte",25,"bold"))
p1.hideturtle()

p2=turtle.Turtle()
p3=turtle.Turtle()
leftpaddle=turtle.Turtle()
rightpaddle=turtle.Turtle()
ball=turtle.Turtle()
p4=turtle.Turtle()

#demo
def pong_demo():
    p.clear()
    p1.clear()
    p5.clear()
    
    #screen
    screen=turtle.Screen()
    screen.title("PONG GAME")
    screen.bgcolor("midnightblue")
    screen.setup(width=1000,height=800)

    leftpaddle.shape('square')
    leftpaddle.color('white')
    leftpaddle.speed(0)
    leftpaddle.shapesize(stretch_len=1.5,stretch_wid=8)
    leftpaddle.penup()
    leftpaddle.goto(-485,0)

    rightpaddle.shape('square')
    rightpaddle.color('white')
    rightpaddle.speed(0)
    rightpaddle.shapesize(stretch_len=1.5,stretch_wid=8)
    rightpaddle.penup()
    rightpaddle.goto(480,0)

    p2.speed(0)
    p2.penup()
    p2.color("Yellow")
    p2.goto(0,360)
    p2.write("PONG DEMO" , align="Center", font=("Forte", 29, "bold"))
    p2.hideturtle()
 
##creating ball
    ball.shape('circle')
    ball.color('yellow')
    ball.penup()

    p3.speed(0)
    p3.penup()
    p3.goto(0,150)
    p3.color("White")
    p3.write(" PRESS 'i'\n PRESS 'm'\n PRESS 'e'\n PRESS 'x' ",align="Center",font=("Forte",27,"bold"))
    p3.hideturtle()
    
    p4.speed(0)
    p4.penup()
    p4.goto(0,-200)
    p4.color("White")
    p4.write("PRESS 'a'  TO START THE GAME.", align="Center",font=("Forte",25,"bold"))
    p4.hideturtle()
    
    def pressi():
        l=rightpaddle.ycor()
        l+=30
        if l<335:
            rightpaddle.sety(l)

    def pressm():
        l=rightpaddle.ycor()
        l-=30
        if l>-335:
            rightpaddle.sety(l)

    def presse():
        l=leftpaddle.ycor()
        l+=30
        if l<335:
            leftpaddle.sety(l)

    def pressx():
        l=leftpaddle.ycor()
        l-=30
        if l>-335:
            leftpaddle.sety(l)
    
    screen.listen()
    screen.onkeypress(pressi,"i")
    screen.onkeypress(pressm,"m")
    screen.onkeypress(presse,"e")
    screen.onkeypress(pressx,"x")



def pong_game():
    p.clear()
    p1.clear()
    p2.clear()
    p3.clear()
    p4.clear()
    p5.clear()
    ##screen2
    sc=turtle.Screen()
    sc.title("PONG GAME")
    sc.bgcolor("midnightblue")
    sc.setup(width=1000, height=800)

    #creating left paddle
    leftpaddle.shape('square')
    leftpaddle.color('white')
    leftpaddle.speed(0)
    leftpaddle.shapesize(stretch_len=1.5, stretch_wid=8)
    leftpaddle.penup()
    leftpaddle.goto(-485,0)
    

    #creating right paddle
    rightpaddle.shape('square')
    rightpaddle.color('white')
    rightpaddle.speed(0)
    rightpaddle.shapesize(stretch_len=1.5, stretch_wid=8)
    rightpaddle.penup()
    rightpaddle.goto(480,0)

    #scoring
    pen=turtle.Turtle()
    pen.speed(0)
    pen.penup()
    pen.color("Yellow")
    pen.pensize(5)
    pen.goto(0,360)
    pen.write("Left_Player : 0   Right_Player : 0 " , align="Center", font=("Forte", 30, "bold"))
    pen.hideturtle()
    leftplayer,rightplayer=0,0

    #creating ball
    ball.shape('circle')
    ball.color('yellow')
    ball.speed(100)
    ball.penup()

    ball.dx=3
    ball.dy=6

    #movement of the paddle
    def leftpaddle_up():
        l=leftpaddle.ycor()
        l+=30
        if l<335:
            leftpaddle.sety(l)

    def leftpaddle_down():
        l=leftpaddle.ycor()
        l-=30
        if l>-335:
            leftpaddle.sety(l)

    def rightpaddle_up():
        l=rightpaddle.ycor()
        l+=30
        if l<335:
            rightpaddle.sety(l)

    def rightpaddle_down():
        l=rightpaddle.ycor()
        l-=30
        if l>-335:
            rightpaddle.sety(l)

    #movement of paddles
    sc.listen()
    sc.onkeypress(leftpaddle_up,"e")
    sc.onkeypress(leftpaddle_down,"x")
    sc.onkeypress(rightpaddle_up,"i")
    sc.onkeypress(rightpaddle_down,"m")

    #movement of ball

    while True:
        sc.update()

        ball.setx(ball.xcor()+ball.dx)
        ball.sety(ball.ycor()+ball.dy)

        if ball.ycor()>400:
            ball.sety(400)
            ball.dy *=-1
            
        if ball.ycor()<-400:
            ball.sety(-400)
            ball.dy *=-1

        if ball.xcor()>500:
            ball.hideturtle()
            ball.goto(0,0)
            ball.showturtle()
            ball.dx *=-1
            rightplayer +=1
            pen.clear()
            pen.write("Left_Player : {}   Right_Player : {}".format (leftplayer, rightplayer), align="center", font=("Forte",30 ,"normal"))
            pen.hideturtle()
            
        if ball.xcor()<-500:
            ball.hideturtle()
            ball.goto(0,0)
            ball.showturtle()
            ball.dx *=-1
            leftplayer +=1
            pen.clear()
            pen.write("Left_Player : {}   Right_Player : {}".format(leftplayer, rightplayer), align="center", font=("Forte",30 ,"normal"))
            pen.hideturtle()

    #ball and paddle collision        
        if (ball.xcor()>460) and (ball.ycor()>rightpaddle.ycor() - 70) and (ball.ycor()<rightpaddle.ycor() + 70):
            ball.dx *= -1

        if (ball.xcor()<-460) and (ball.ycor()>leftpaddle.ycor() - 70) and (ball.ycor()<leftpaddle.ycor() + 70):
            ball.dx *= -1

screen.listen()
screen.onkeypress(pong_demo,"space")
screen.onkeypress(pong_game,"a")
