import time
import sys
import os
import turtle

sys.path.append("/home/rvr/turtle-rvr")

from sphero_sdk import SpheroRvrObserver
from sphero_sdk import DriveFlagsBitmask
from sphero_sdk import InfraredCodes
from sphero_sdk import Colors


def infrared_message_received_handler(infrared_message):
    print(infrared_message)


class MyRVR:
    def __init__(self):
        self.rvr = SpheroRvrObserver()

    def connect(self):
        self.rvr.wake()
        time.sleep(2)

    def close(self):
        try:
            self.rvr.led_control.turn_leds_off()
        finally:
            self.rvr.close()

    def set_all_leds(self, color):
        self.rvr.led_control.set_all_leds_color(color=color)

    def flash_all_leds(self, color, times):
        for times in range(times):
            self.rvr.led_control.set_all_leds_color(color=color)
            time.sleep(1)
            self.rvr.led_control.turn_leds_off()

    def flash_all_leds_duel(self, color1, color2, times):
        for times in range(times):
            self.rvr.led_control.set_all_leds_color(color=color1)
            time.sleep(0.5)
            self.rvr.led_control.set_all_leds_color(color=color2)
            time.sleep(0.5)

    def turn_leds_off(self):
        self.rvr.led_control.turn_leds_off()

    def forward(self, speed, seconds):
        self.rvr.reset_yaw()
        self.rvr.drive_control.drive_forward_seconds(
            speed=speed, heading=0, time_to_drive=seconds
        )

    def back(self, speed, seconds):
        self.rvr.reset_yaw()
        self.rvr.drive_control.drive_backward_seconds(
            speed=speed, heading=0, time_to_drive=seconds
        )

    def left(self):
        self.rvr.drive_control.turn_left_degrees(heading=0)

    def right(self):
        self.rvr.drive_control.turn_right_degrees(heading=0)

    def infrared_listen(self):
        self.rvr.infrared_control.listen_for_infrared_message(
            handler=infrared_message_received_handler
        )
