edubitSoundBit.onEvent(SoundSensorCompareType.LessThan, 802, function () {
    radio.sendNumber(0)
})
edubitSoundBit.onEvent(SoundSensorCompareType.MoreThan, 802, function () {
    turtle.setSpeed(50)
    turtle.turnLeft()
    turtle.turnRight()
    turtle.turnLeft()
    turtle.turnRight()
    turtle.turnRight()
    turtle.turnLeft()
    turtle.turnLeft()
})
input.onButtonPressed(Button.A, function () {
    turtle.turnLeft()
})
input.onGesture(Gesture.TiltLeft, function () {
    turtle.forward(1)
})
input.onButtonPressed(Button.AB, function () {
    turtle.turnRight()
})
input.onButtonPressed(Button.B, function () {
    turtle.setSpeed(3)
    turtle.back(1)
    turtle.back(1)
})
input.onGesture(Gesture.Shake, function () {
    turtle.setSpeed(3)
    turtle.forward(1)
    turtle.forward(1)
})
input.onGesture(Gesture.TiltRight, function () {
    turtle.back(1)
})
