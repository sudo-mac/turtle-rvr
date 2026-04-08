from myrvr import *

turtle = MyRVR()

codes = [
    InfraredCodes.one,
    InfraredCodes.two,
    InfraredCodes.three,
    InfraredCodes.four,
    InfraredCodes.five,
]


def main():
    turtle.connect()

    print(InfraredCodes)

    while True:
        if turtle.infrared_listen() != None:
            print(turtle.infrared_listen())


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram stopped by user.")
    finally:
        turtle.close()
