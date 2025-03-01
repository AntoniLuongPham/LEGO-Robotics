#!/usr/bin/env pybricks-micropython


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, InfraredSensor
from pybricks.media.ev3dev import SoundFile
from pybricks.parameters import Direction, Port, Stop


BRICK = EV3Brick()

MEDIUM_MOTOR = Motor(port=Port.A, 
                     positive_direction=Direction.CLOCKWISE)
GO_MOTOR = Motor(port=Port.B,
                 positive_direction=Direction.CLOCKWISE)
STING_MOTOR = Motor(port=Port.D,
                    positive_direction=Direction.CLOCKWISE)

IR_SENSOR = InfraredSensor(port=Port.S4)


MEDIUM_MOTOR.run_time(
    speed=500,
    time=1000,
    then=Stop.HOLD,
    wait=True)

MEDIUM_MOTOR.run_time(
    speed=-500,
    time=0.3 * 1000,
    then=Stop.HOLD,
    wait=True)

STING_MOTOR.run_time(
    speed=400,
    time=1000,
    then=Stop.HOLD,
    wait=True)

for i in range(3):
    GO_MOTOR.run(speed=-1000)

    BRICK.speaker.play_file(file=SoundFile.ERROR_ALARM)

    while IR_SENSOR.distance() >= 40:
        pass

    GO_MOTOR.run(speed=250)

    BRICK.speaker.play_file(file=SoundFile.ERROR_ALARM)

    STING_MOTOR.run_angle(
        speed=-750,
        rotation_angle=220,
        then=Stop.HOLD,
        wait=True)

    BRICK.speaker.play_file(file=SoundFile.ERROR_ALARM)
    
    STING_MOTOR.run_time(
        speed=-1000,
        time=1000,
        then=Stop.HOLD,
        wait=True)

    BRICK.speaker.play_file(file=SoundFile.ERROR_ALARM)

    MEDIUM_MOTOR.run_time(
        speed=750,
        time=0.2 * 1000,
        then=Stop.HOLD,
        wait=True)

    MEDIUM_MOTOR.run_time(
        speed=-750,
        time=0.2 * 1000,
        then=Stop.HOLD,
        wait=True)

    GO_MOTOR.run_angle(
        speed=-1000,
        rotation_angle=2 * 360,
        then=Stop.HOLD,
        wait=True)

    STING_MOTOR.run_time(
        speed=400,
        time=1000,
        then=Stop.HOLD,
        wait=True)

    GO_MOTOR.run_angle(
        speed=1000,
        rotation_angle=2 * 360,
        then=Stop.HOLD,
        wait=True)
