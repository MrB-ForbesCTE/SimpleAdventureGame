
class Creature():
    def __init__(self, 
                 STR = 10, 
                 DEX = 10, 
                 CON = 10, 
                 WIS = 10, 
                 INT = 10, 
                 CHA = 10, 
                 HD = 0,
                 ):
        
        self.STR = STR
        self.DEX = DEX
        self.CON = CON
        self.WIS = WIS
        self.INT = INT
        self.CHA = CHA
        self.HD = HD
        self.AC = 10+self.get_mod(DEX)
        
        
    def get_mod(self,stat):
        return round((stat-10)/2)
        