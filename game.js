const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");

const paddleWidth = 20;
const paddleHeight = 160;
const ballSize = 10; // Reduced size
const paddleSpeed = 8;
let ballSpeedX = 2; // Reduced speed
let ballSpeedY = 2; // Reduced speed

let paddle1Y = (canvas.height - paddleHeight) / 2;
let paddle2Y = (canvas.height - paddleHeight) / 2;
let ballX = canvas.width / 2;
let ballY = canvas.height / 2;

let score1 = 0;
let score2 = 0;

function drawRect(x, y, width, height, color) {
    ctx.fillStyle = color;
    ctx.fillRect(x, y, width, height);
}

function drawCircle(x, y, size, color) {
    ctx.fillStyle = color;
    ctx.beginPath();
    ctx.arc(x, y, size, 0, Math.PI * 2);
    ctx.fill();
}

function drawText(text, x, y, color) {
    ctx.fillStyle = color;
    ctx.font = "30px Courier";
    ctx.fillText(text, x, y);
}

function drawDashedLine() {
    ctx.setLineDash([10, 10]);
    ctx.beginPath();
    ctx.moveTo(canvas.width / 2, canvas.height / 4); // Shortened line
    ctx.lineTo(canvas.width / 2, (canvas.height / 4) * 3); // Shortened line
    ctx.strokeStyle = "yellow";
    ctx.stroke();
}

function draw() {
    drawRect(0, 0, canvas.width, canvas.height, "black");
    drawRect(10, paddle1Y, paddleWidth, paddleHeight, "blue");
    drawRect(canvas.width - paddleWidth - 10, paddle2Y, paddleWidth, paddleHeight, "red");
    drawCircle(ballX, ballY, ballSize, "white");
    drawText(`Player 1: ${score1}`, canvas.width / 4, 50, "yellow");
    drawText(`Player 2: ${score2}`, (canvas.width / 4) * 3, 50, "yellow");
    drawDashedLine();
}

function moveBall() {
    ballX += ballSpeedX;
    ballY += ballSpeedY;

    if (ballY < 0 || ballY > canvas.height) {
        ballSpeedY = -ballSpeedY;
    }

    if (ballX < 0) {
        if (ballY > paddle1Y && ballY < paddle1Y + paddleHeight) {
            ballSpeedX = -ballSpeedX;
        } else {
            score2++;
            resetBall();
        }
    }

    if (ballX > canvas.width) {
        if (ballY > paddle2Y && ballY < paddle2Y + paddleHeight) {
            ballSpeedX = -ballSpeedX;
        } else {
            score1++;
            resetBall();
        }
    }
}

function resetBall() {
    ballX = canvas.width / 2;
    ballY = canvas.height / 2;
    ballSpeedX = (Math.random() > 0.5 ? 1 : -1) * 2; // Restart with the same speed but random direction
    ballSpeedY = (Math.random() > 0.5 ? 1 : -1) * 2; // Restart with the same speed but random direction
}

function movePaddle(event) {
    const key = event.key;
    if (key === "w" && paddle1Y > 0) {
        paddle1Y -= paddleSpeed;
    }
    if (key === "s" && paddle1Y < canvas.height - paddleHeight) {
        paddle1Y += paddleSpeed;
    }
    if (key === "ArrowUp" && paddle2Y > 0) {
        paddle2Y -= paddleSpeed;
    }
    if (key === "ArrowDown" && paddle2Y < canvas.height - paddleHeight) {
        paddle2Y += paddleSpeed;
    }
}

document.addEventListener("keydown", movePaddle);

// Prevent scrolling when using arrow keys
window.addEventListener("keydown", function(e) {
    if(["ArrowUp", "ArrowDown"].indexOf(e.key) > -1) {
        e.preventDefault();
    }
}, false);

function gameLoop() {
    moveBall();
    draw();
    requestAnimationFrame(gameLoop);
}

gameLoop();
