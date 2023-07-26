# from turtle import Turtle
# ALIGN = "center"
# FONT = ("Courier",24,"normal")
# class scoreboard(Turtle):
#         def __init__(self):
#             super().__init__()
#             self.score = 0
#             self.color("white")
#             #Hides the arrow(turtle)
#             self.hideturtle()
#             self.penup()
#             self.goto(0, 270)
#             self.updates_score()
#         def updates_score(self):
#             self.write(f"Score: {self.score}", align=ALIGN, font=FONT)
#         def increase_score(self):
#             self.clear()
#             self.score += 1
#             self.updates_score()
#         def game_over(self):
#             self.goto(0,0)
#             self.write("GAME OVER", align=ALIGN, font=FONT)
from turtle import Turtle
ALIGN = "center"
FONT = ("Courier",24,"normal")
class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        #Hides the arrow(turtle)
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.update_score()
    def update_score(self):
        self.write(f"Score: {self.score}", align=ALIGN,font= FONT)
    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGN,font=FONT)