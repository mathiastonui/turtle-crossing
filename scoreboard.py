from turtle import Turtle
FONT = ("Courier", 24, "normal")
LEVEL = 1


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-250, 250)
        self.write(f"Level: {LEVEL}")

    def collision(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)

    def increase_level(self):
        global LEVEL
        LEVEL += 1
        self.update_scoreboard()



