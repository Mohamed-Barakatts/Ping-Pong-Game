from browser import document, timer

canvas = document["gameCanvas"]
context = canvas.getContext("2d")

class Paddle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self):
        context.fillStyle = self.color
        context.fillRect(self.x, self.y, 20, 150)  # Paddle size

    def move_up(self):
        self.y -= 30
        self.y = max(self.y, 0)

    def move_down(self):
        self.y += 30
        self.y = min(self.y, 750)  # Ensure paddle stays within the canvas

class Ball:
    def __init__(self):
        self.x = canvas.width / 2
        self.y = canvas.height / 2
        self.dx = 1.5  # Lower speed
        self.dy = 1.5  # Lower speed

    def move(self):
        self.x += self.dx
        self.y += self.dy

        if self.y < 0 or self.y > canvas.height:
            self.dy = -self.dy

    def draw(self):
        context.beginPath()
        context.arc(self.x, self.y, 15, 0, 2 * 3.14159)
        context.fillStyle = "white"
        context.fill()

paddle1 = Paddle(30, canvas.height / 2 - 75, "blue")
paddle2 = Paddle(canvas.width - 50, canvas.height / 2 - 75, "red")
ball = Ball()

def draw_center_line():
    context.strokeStyle = "yellow"
    context.setLineDash([15, 10])  # Dotted line
    context.beginPath()
    context.moveTo(canvas.width / 2, 0)
    context.lineTo(canvas.width / 2, canvas.height)
    context.stroke()

def update(*args):
    context.clearRect(0, 0, canvas.width, canvas.height)
    draw_center_line()
    paddle1.draw()
    paddle2.draw()
    ball.move()
    ball.draw()
    timer.set_timeout(update, 10)

def keydown(event):
    if event.key == "w":
        paddle1.move_up()
    elif event.key == "s":
        paddle1.move_down()
    elif event.key == "ArrowUp":
        paddle2.move_up()
    elif event.key == "ArrowDown":
        paddle2.move_down()

document.bind("keydown", keydown)
timer.set_timeout(update, 10)
