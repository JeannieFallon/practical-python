# bounce.py
#
# Exercise 1.5
import sys


INIT_HEIGHT = 100


def main():
    print(f"Height of first 10 bounces from drop of {INIT_HEIGHT} meters")

    height = INIT_HEIGHT
    for i in range(0, 10):
        height = round(height * .6, 4)
        print(f"{i}. {height}")

    
if __name__ == "__main__":
    main()
