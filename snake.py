from turtle import Turtle

MOVE_DISTANCE = 20

class Snake:
    '''Creates the snake segnments for the snake game'''
    def __init__(self):
        self.replit()
        self.snakes = [] 
        self.create_snake()
        self.head = self.snakes[0]
        
    def move(self):
        for i in range(len(self.snakes) - 1, 0, -1):
            position = self.snakes[i-1].position()
            self.snakes[i].goto(position)
        self.head.forward(MOVE_DISTANCE)

    def create_snake(self):
        for i in range(3):
            turtle = Turtle("square")
            turtle.pu()
            turtle.setx(-20 * i)
            turtle.color("white")
            self.snakes.append(turtle)

    def add_segment(self):
        position = self.snakes[-1].position()
        turtle = Turtle("square")
        turtle.pu()
        turtle.color("white")
        turtle.goto(position)
        self.snakes.append(turtle)

    def left(self):
        if self.head.heading() != 0.0:
            self.head.seth(180)
    
    def right(self):
        if self.head.heading() != 180.0:
            self.head.seth(0)

    def up(self):
        if self.head.heading() != 270.0:
            self.head.seth(90)

    def reset(self):
        for snake in self.snakes:
            snake.goto(1000,1000)
        self.snakes.clear()
        self.create_snake()
        self.head = self.snakes[0]

    def down(self):
        if self.head.heading() != 90.0:
            self.head.seth(270)

    def collision(self):
        for segment in self.snakes[1:]:
            if self.head.distance(segment) <= 15:
                return True
        if self.head.xcor() >= 300 or self.head.xcor() <= -300 or self.head.ycor() >= 300 or self.head.ycor() <= -300:
            return True
        else:
            return False

    def replit(self):
        tim = Turtle()
        tim.pu()
        tim.ht()
        tim.speed("fastest")
        tim.goto(-300,-300)
        tim.pd()
        tim.fillcolor("black")
        tim.begin_fill()
        tim.seth(90)
        for i in range(4):
            tim.forward(600)
            tim.right(90)
        tim.end_fill()