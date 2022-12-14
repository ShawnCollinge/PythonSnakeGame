from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Curior", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.pu
        self.score = 0
        with open("scores.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.ht()
        self.goto(0,280)
        self.speed("fastest")
        self.color("white")
        self.update_scoreboard()

    def add_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("scores.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()
    