def on_button_pressed_a():
    turtle.turn_left()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_tilt_left():
    turtle.forward(1)
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def on_button_pressed_ab():
    turtle.turn_right()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    turtle.set_speed(3)
    turtle.back(1)
    turtle.back(1)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    turtle.set_speed(3)
    turtle.forward(1)
    turtle.forward(1)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_gesture_tilt_right():
    turtle.back(1)
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

def on_forever():
    if edubitIrBit.is_ir_sensor_triggered():
        turtle.set_speed(50)
        turtle.turn_left()
        turtle.turn_right()
        turtle.turn_left()
        turtle.turn_right()
        turtle.turn_right()
        turtle.turn_left()
        turtle.turn_left()
basic.forever(on_forever)
