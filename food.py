# from turtle import Turtle
# import random
# class food(Turtle):
#     def __init__(self):
#         super().__init__()
#         self.shape("circle")
#         self.penup()
#         self.shapesize(stretch_len=0.5,stretch_wid=0.5)
#         self.color("red")
#         self.speed("fastest")
#         self.refresh()
#     def refresh(self):
#         random_x = random.randint(-280, 280)
#         random_y = random.randint(-280, 280)
#         self.goto(random_x, random_y)
from turtle import Turtle
import random
# Used inheritance to access some methods in the Turtle class such as Shape, Shape size, speed...
class food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.penup()
        self.refresh()

    #Refresh method when there is collision between snake item and the food.
    def refresh(self):
        random_x = random.randint(-280,280)
        random_y = random.randint(-280, 280)
        self.goto(random_x,random_y)

