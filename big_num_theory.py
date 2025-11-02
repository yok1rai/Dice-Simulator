"""
Big Number Theory - Dice Probability Simulator 🎲

This program simulates dice rolls in very large quantities to observe
how random distributions behave as the sample size grows.

Features:
- Simulates from small to huge sample sizes (up to 10^8 safely)
- Measures execution time for each simulation
- Displays probability distribution for each dice face
- Includes small time delays for visual clarity and pacing

Author : Yok1rai
Date   : 12.10.2025
Note   : Designed for experimentation, not for production optimization :)
"""

from time import sleep as sl
from datetime import datetime as dt
import sys
import random
import os
import platform


def clear():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def main():
    dices = {i:0 for i in range(1,7)}
    chunk_size = 100000

    while True:
        ver = sys.version_info
        if ver < (3, 10):
            print("Invalid Python version. Please update to 3.10.0 or higher (3.11.0 recommended)")
            return

        print("Welcome to big numbers testing for math!")
        try:
            scope = int(input("What's the scope: "))


            if scope == 0:
                print("Goodbye..")
                sl(1)
                break

            elif scope > 10 ** 8:
                print("Stop there! It's too big to process! ")
                while True:
                    confirm = input("Do you want to continue (y/n): ").lower().strip()

                    match confirm:
                        case "y" | "yes":
                            print("Understood")
                            break

                        case "n" | "no":
                            print("Leaving..")
                            return

                        case _:
                            print("Unknown command")

            clear()

            startP = dt.now()

            for chunk_start in range(0, scope, chunk_size):
                chunk_end = min(scope, chunk_start + chunk_size)

                for i in range(chunk_start, chunk_end):
                    rng = random.randint(1, 6)
                    dices[rng] += 1

                    percent = min(int(((i + 1) / scope) * 100 + 0.000001), 100)

                    if i + 1 == scope or percent != int(((i - 1) / scope) * 100):
                        sys.stdout.write(f"\rProgress: {percent:3d} % ")
                        sys.stdout.flush()


            print("\n")

            endP = dt.now()
            diff = endP - startP
            totalsec = diff.total_seconds()
            mins = int(totalsec // 60)
            secs = totalsec % 60
            f_line = f"{mins:02d}:{secs:06.4f}"

            for key, value in dices.items():
                print(f"{key}: {value / scope}")
                sl(0.1)
            print(f"Estimated time: {f_line}")



        except ValueError:
            print("Please enter a number")

        except Exception as e:
            print(f"Unknown error: {e}")



if __name__ == "__main__":
    main()
