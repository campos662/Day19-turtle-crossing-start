from turtle import Turtle
FONT = ("Courier", 24, "normal")
FONT_GAME_OVER = ("Courier", 48, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.ht()
        self.color("black")

    def score_refresh(self,nivel):
        self.clear()
        self.goto(-280, 260)
        self.write(f"Level {nivel}", align="left", font=FONT)

    def game_over(self):
        self.clear()
        self.home()
        self.write("Game over!!!", align="center", font=FONT_GAME_OVER)

