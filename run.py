# In this file we will have our code to run the Simple Adventure Game

# Warmup 1/21/26
# What do you think this code does?

from mechanics import dice, health_bar
max_hp = 20
hp = max_hp

def main():
    hp = dice.d20.roll()
    print(f"Your starting hp is: {hp}/{max_hp}")
    health_bar.health_bar(hp, max_hp)
    print(health_bar.healthbar)


if __name__ == "__main__":
    main()