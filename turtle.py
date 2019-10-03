
from turtle import *
from random import randint

speed(0)
penup()
goto(-140, 140)

for step in range(15):
    write(step, align='center')
    right(90)
    for num in range(8):
        penup()
        forward(10)
        pendown()
        forward(10)
    penup()
    backward(160)
    left(90)
    forward(20)

cat = Turtle()
cat.color('red')
cat.shape('turtle')

cat.penup()
cat.goto(-160, 100)
cat.pendown()

for turn in range(10):
    cat.right(36)

dog = Turtle()
dog.color('blue')
dog.shape('turtle')

dog.penup()
dog.goto(-160, 70)
dog.pendown()

for turn in range(72):
    dog.left(5)

mouse = Turtle()
mouse.shape('turtle')
mouse.color('green')

mouse.penup()
mouse.goto(-160, 40)
mouse.pendown()

for turn in range(60):
    mouse.right(6)

snake = Turtle()
snake.shape('turtle')
snake.color('orange')

snake.penup()
snake.goto(-160, 10)
snake.pendown()

for turn in range(30):
    snake.left(12)

for turn in range(100):
    cat.forward(randint(1, 5))
    dog.forward(randint(1, 5))
    mouse.forward(randint(1, 5))
    snake.forward(randint(1, 5))
