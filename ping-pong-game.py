import turtle

class Paddle(turtle.Turtle):
    def __init__(self, x, y, color):
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_wid=8, stretch_len=1)
        self.penup()
        self.goto(x, y)

    def move_up(self):
        y = self.ycor()
        y += 30
        self.sety(y)

    def move_down(self):
        y = self.ycor()
        y -= 30
        self.sety(y)

class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.shape("circle")
        self.color("white")
        self.penup()
        self.dx = 1.5  # Lower speed
        self.dy = 1.5  # Lower speed

    def move(self):
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)

    def bounce_y(self):
        self.dy *= -1

    def bounce_x(self):
        self.dx *= -1

def update_score():
    score.clear()
    score.write(
        f"Player 1 => [{score1}]  Player 2 => [{score2}]", align="center", font=("Courier", 30, "normal")
    )

# Set up the screen
wind = turtle.Screen()
wind.title(" - Ping Pong By Mohamed - ")
wind.bgcolor("black")
wind.setup(width=1400, height=900)
wind.tracer(0)

# Paddles and Ball
paddle1 = Paddle(-680, 0, "blue")
paddle2 = Paddle(680, 0, "red")
ball = Ball()

# Score
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("yellow")
score.penup()
score.hideturtle()
score.goto(0, 370)
update_score()

# Center Line
center_line = turtle.Turtle()
center_line.color("yellow")
center_line.penup()
center_line.hideturtle()
center_line.goto(0, -450)
center_line.pendown()
center_line.setheading(90)

for _ in range(18):  # Creating a dashed line
    center_line.forward(25)
    center_line.penup()
    center_line.forward(25)
    center_line.pendown()

# Keyboard bindings
wind.listen()
wind.onkeypress(paddle1.move_up, "w")
wind.onkeypress(paddle1.move_down, "s")
wind.onkeypress(paddle2.move_up, "Up")
wind.onkeypress(paddle2.move_down, "Down")

# Main game loop
while True:
    wind.update()
    ball.move()

    # Border collision
    if ball.ycor() > 405 or ball.ycor() < -405:
        ball.bounce_y()

    # Scoring
    if ball.xcor() > 800:
        ball.goto(0, 0)
        ball.bounce_x()
        score1 += 1
        update_score()

    if ball.xcor() < -800:
        ball.goto(0, 0)
        ball.bounce_x()
        score2 += 1
        update_score()

    # Paddle collision
    if (650 < ball.xcor() < 700 and paddle2.ycor() - 100 < ball.ycor() < paddle2.ycor() + 100) or \
       (-700 < ball.xcor() < -650 and paddle1.ycor() - 100 < ball.ycor() < paddle1.ycor() + 100):
        ball.bounce_x()
