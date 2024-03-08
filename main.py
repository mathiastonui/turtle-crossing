import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move, "Up")

game_is_on = True
loop_count = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move_car()

    loop_count += 1  # Increment the counter

    if loop_count == 6:  # Check if it's the 6th iteration
        car_manager.create_car()
        loop_count = 0  # Reset the counter for future car creations

    for car in car_manager.cars:
        if player.detect_collision(car):
            game_is_on = False
            scoreboard.collision()

    if player.detect_finish_line():
        car_manager.increase_speed()
        scoreboard.increase_level()


screen.exitonclick()
