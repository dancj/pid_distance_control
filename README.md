# PID Distance Control
RPi Demo using Python3 that shows a sensor sensing and a motor moving using a Proportional-Integral-Derivative (PID) controller.

## Getting Started
1. Flash Raspbian lite to SD card, current version is Raspbian Buster
1. Add empty file named "ssh" to root directory of SD card, to enable ssh
1. Insert card into RPi and boot up for the first time
1. Use another computer to SSH into RPi, *ssh pi@192.168.1.[rpi_ip]*. Default password is *raspberry* and it's always a good idea to change that right away with *passwd* command
1. Update things with **sudo apt update && sudo apt upgrade*
1. *sudo apt install git*
1. *git clone https://github.com/dancj/pid_distance_control.git*
1. Now this project is on the RPi, just need to set up virtual environment and download dependencies
    1. *cd pid_distance_control/*
    1. *sudo apt install python3-venv*
    1. *python3 -m venv venv*
    1. *source venv/bin/activate*
    1. *pip install -r requirements.txt*
    
## Running
Just need to run the main python routine
1. *cd pid_distance_control/*
1. *source venv/bin/activate*
1. *python run.py*

## Hardware
1. Raspberry Pi (RPi) 1 model B (could use any model)
1. Ultrasonic distance sensor (HC-SR04)
1. Servo motor
1. Cobbler Pi breakout board
1. Half size 
1. Jumper wires
1. Resistors: 330 and 470 Ohm

## Software


## Wiring


## Testing


## References
1. [Using a Raspberry Pi distance sensor](https://tutorials-raspberrypi.com/raspberry-pi-ultrasonic-sensor-hc-sr04/)
1. [Raspberry Pi Servo Motor control](https://tutorials-raspberrypi.com/raspberry-pi-servo-motor-control/)

## License

This is for a class extra credit project, but mostly just for fun.

Put out there to the world "as is" with MIT license.