ev3.motorOn(forSeconds: 1, on: .a, withPower: -50)
ev3.playSound(file: .blip, atVolume: 100, withStyle: .playOnce)
ev3.motorOn(forSeconds: 1, on: .a, withPower: 50)
ev3.waitFor(seconds: 1)
ev3.playSound(file: .blip, atVolume: 100, withStyle: .playOnce)
ev3.motorOn(forSeconds: 1, on: .a, withPower: -50)
