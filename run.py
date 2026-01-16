# In this file we will have our code to run the Simple Adventure Game

import random
import mechanics.dice as dice

def main():
    print(f"Let's get a random number: {dice.d20.roll()}")
    
if __name__ == "__main__":
    main()