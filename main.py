import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

merki = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(key="Up", fun=merki.go_up)


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()

    if merki.is_at_finish_line():
        merki.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

    for car in car_manager.all_cars:
        if merki.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
