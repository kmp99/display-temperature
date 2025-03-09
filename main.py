temp = 0

def on_button_pressed_a():
    basic.show_string("" + str(temp) + "C")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_string("" + str((temp + 274.15)) + "K")
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    global temp
    temp = input.temperature()
basic.forever(on_forever)
