import os
import sys
import time
from turtle import left

sys.path.append("/home/rvr/turtle-rvr")

from sphero_sdk import SpheroRvrObserver
from sphero_sdk import RvrLedGroups
from sphero_sdk import Colors


rvr = SpheroRvrObserver()


def main():

    try:
        rvr.wake()
        time.sleep(2)

        for i in range(5):

            for i in range(100):
                rvr.led_control.turn_leds_off()

                time.sleep(0.2)

                rvr.led_control.set_led_color(
                    led=RvrLedGroups.headlight_left, color=Colors.yellow
                )

                time.sleep(0.2)

                rvr.led_control.turn_leds_off()

                time.sleep(0.2)

                rvr.led_control.set_led_color(
                    led=RvrLedGroups.headlight_right, color=Colors.green
                )

                time.sleep(0.2)

                rvr.led_control.turn_leds_off()

                time.sleep(0.2)

                rvr.led_control.set_led_color(
                    led=RvrLedGroups.headlight_left, color=Colors.green
                )

                time.sleep(0.2)

                rvr.led_control.turn_leds_off()

                time.sleep(0.2)

                rvr.led_control.set_led_color(
                    led=RvrLedGroups.headlight_right, color=Colors.yellow
                )

            time.sleep(2)

            rvr.led_control.turn_leds_off()

            time.sleep(1)

            rvr.led_control.set_all_leds_rgb(red=255, green=0, blue=0)

            time.sleep(2)

            rvr.led_control.turn_leds_off()

            time.sleep(1)

    except KeyboardInterrupt:
        print("\nProgram terminated with keyboard interrupt.")

    finally:
        rvr.close()


if __name__ == "__main__":
    main()
