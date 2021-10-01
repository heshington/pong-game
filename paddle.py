from turtle import Turtle
UP = 90
DOWN = 270


class Paddle(Turtle):

    def __init__(self, coordinates):
        super().__init__()
        self.shape("square")
        self.penup()
        self.coordinates = coordinates
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.setheading(UP)
        self.color("white")
        self.create_paddle()


    def create_paddle(self):
        # self.position(x = self.coordinates[0], y= self.coordinates[1])
        self.setx(self.coordinates[0])
        self.sety(self.coordinates[1])

    def up(self):

        self.setheading(UP)
        self.forward(20)
    def down(self):
        self.setheading(DOWN)
        self.forward(20)