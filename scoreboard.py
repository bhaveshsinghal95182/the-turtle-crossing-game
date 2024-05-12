from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "left"

class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.update_scoreboard()

    def increasse_level(self):
        self.level += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"level: {self.level}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)