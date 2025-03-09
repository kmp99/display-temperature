let temp = 0
input.onButtonPressed(Button.A, function () {
    basic.showString("" + temp + "C")
})
input.onButtonPressed(Button.B, function () {
    basic.showString("" + (temp + 274.15) + "K")
})
basic.forever(function () {
    temp = input.temperature()
})
