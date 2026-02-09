from dice import d20
def roll_initiative(fighter):
    return fighter.init_mod + d20.roll

def fight(combatants[]):
    initiative = {}
    for fighter in combatants:
        initiative[fighter.name] = roll_initiative(fighter)
    