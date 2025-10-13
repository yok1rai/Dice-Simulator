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

import random
from datetime import datetime as dt
from time import sleep as sl

def bignum():
    while True:
        dices = {i:0 for i in range(1,7)}
        try:
            scope = int(input("What is the scope: "))
            sl(0.5)

            if scope == 0:
                print("Goodbye..")
                sl(1.5)
                break

            elif scope > 10 ** 8:
                print("Warning: Number is too big. Do you want to continue?")
                while True:
                    confirm = input("y/n ").lower().strip()

                    match confirm:
                        case "y":
                            print("Undestood")
                            sl(0.5)
                            break
                        case "n":
                            raise RuntimeError
                        case _:
                            print("Unknown command")
            
            startP = dt.now()
            for i in range(1, scope + 1):
                rng = random.randint(1,6)
                dices[rng] += 1
            
            endP = dt.now()
            diff = endP - startP
            total_sec = diff.total_seconds()
            minutes = int(total_sec // 60)
            seconds = total_sec % 60
            f_line = f"{minutes:02d}:{seconds:06.4f}"

            for num, dice in dices.items():
                print(f"{num}: {dice / scope}")
                sl(0.1)
            print(f"Estimamted time: {f_line}")
            sl(0.5)
        
        except ValueError:
            print("Please enter a valid number")
        except RuntimeError:
            print("Number is too big to process")
        except Exception as e:
            print(f"Unknown Error: {e}")


if __name__ == "__main__":
    bignum()