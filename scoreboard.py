from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 14, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt") as f:
            self.high_score = int(f.read())
        self.ht()
        self.color("white")
        self.penup()
        self.setposition(0, 280)
        self.pendown()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Score: {self.score} High Score: {self.high_score}",
            False,
            ALIGN,
            font=FONT,
        )

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open("high_score.txt", "w") as f:
            f.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()
