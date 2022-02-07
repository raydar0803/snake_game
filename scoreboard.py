from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0

    def keep_score(self):
        self.hideturtle()
        self.penup()
        self. goto(0, 260)
        self.color("white")
        self.write(f"Score: {self.score}", move=False, align="center", font=("Arial", 18, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", move=False, align="center", font=("Arial", 18, "normal"))

