from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

# Create cars that are 20px high by 40px wide that are randomly generated along the y-axis and move to the left edge
# of the screen. No cars should be generated in the top and bottom 50px of the screen (think of it as a safe zone for
# our little turtle). Hint: generate a new car only every 6th time the game loop runs.


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.create_car()

    def create_car(self):
        new_car = Turtle()
        new_car.shape("square")
        new_car.penup()
        new_car.shapesize(stretch_len=2, stretch_wid=1)
        new_car.color(random.choice(COLORS))
        new_car.goto(x=300, y=random.randint(-240, 240))
        self.cars.append(new_car)

    def move_car(self):
        for car in self.cars:
            new_x = car.xcor() - MOVE_DISTANCE
            car.goto(new_x, car.ycor())

    def increase_speed(self):
        global MOVE_DISTANCE
        MOVE_DISTANCE += MOVE_INCREMENT
        # for car in self.cars:
        #     new_x = car.xcor() - (STARTING_MOVE_DISTANCE + MOVE_INCREMENT)
        #     car.goto(new_x, car.ycor())

