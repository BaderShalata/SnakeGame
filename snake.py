MOVING_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
from turtle import Turtle
POSITION = [(0,0),(-20,0),(-40,0)]
class snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    def create_snake(self):
        for position in POSITION:
            self.add_new_segment(position)
    def add_new_segment(self,position):
        new_segment = Turtle("square")
        new_segment.color("green")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
    #adds new segment using the add_new_segment method once collision between food and snake
    def extend(self):
        self.add_new_segment(self.segments[-1].position())
    def move(self):
        for seg in range(len(self.segments) -1,0,-1):
            if self.segments[seg] != self.head:
                new_x = self.segments[seg - 1].xcor()
                new_y = self.segments[seg - 1].ycor()
                self.segments[seg].goto(new_x,new_y)
        self.head.forward(MOVING_DISTANCE)
    #Move Up
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    #Move Down
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    #Move Left
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    #Move Right
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


