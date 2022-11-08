from gpiozero import Button
from signal import pause
from display_muni_data import display_muni_data

# Button assignments
green_button = Button(2, hold_time=2)
blue_button = Button(22)
yellow_button = Button(5)
red_button = Button(26)


def simple_message(message):
    output(4, -90, 2, False, message)


def stream(loops):
    loop_count = 0
    stop_ids = ["15539", "15540"]
    for _ in range(loops):
        print("Loop Count: ", loop_count)
        for stop_id in stop_ids:
            display_muni_data(stop_id)
        loop_count += 1


def single_stream(stop_id):
    if not green_button.was_held:
        display_muni_data(stop_id)
    green_button.was_held = False
  

green_button.when_released = lambda: display_muni_data("15539")
blue_button.when_released = lambda: display_muni_data("15540")
yellow_button.when_pressed = lambda: display_muni_data("17129")
red_button.when_pressed = lambda: display_muni_data("15537")

pause()