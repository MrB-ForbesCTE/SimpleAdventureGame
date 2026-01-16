import random
class Die():
    def __init__(self,face):
        self.face = face
        
    def roll(self):
        return random.randint(1,self.face)
    
    def advantage(self):
        r1 = self.roll()
        r2 = self.roll()
        return (max(r1,r2),r1,r2)
    
    def disadvantage(self):
        r1 = self.roll()
        r2 = self.roll()
        return (min(r1,r2),r1,r2)
    
d4 = Die(4)
d6 = Die(6)
d8 = Die(8)
d10 = Die(10)
d12 = Die(12)
d20 = Die(20)
d100 = Die(100)
