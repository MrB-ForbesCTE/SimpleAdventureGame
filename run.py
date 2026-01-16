# In this file we will have our code to run the Simple Adventure Game

import random
import mechanics.dice as dice

def main():
    hp = 20
    healthbar = "|"
    print(f"Let's get a random number: {dice.d20.roll()}")
    for i in range(20):
        if i < hp:
            healthbar += "*"
        else:
            healthbar += "-"
        if i == 19:
            healthbar +="|"
    print(healthbar)
        
    
if __name__ == "__main__":
    main()