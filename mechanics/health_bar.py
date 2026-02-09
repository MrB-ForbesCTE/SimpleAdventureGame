healthbar = "|"
def health_bar(current, max):
    global healthbar
    for i in range(max):
        if i < current:
            healthbar += "*"
        else:
            healthbar += "-"
        if i == max - 1:
            healthbar +="|"
    return healthbar
    