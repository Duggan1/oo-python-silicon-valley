class FundingRound:
    all = []
    Examples = [ "Angel", "Pre-Seed", "Seed", "Series A", "Series B", "Series C"]
    
    def __init__(self,startup, venture_capitalist,type:str, investment:float):
        self._startup = startup
        self._venture_capitalist = venture_capitalist
        if investment >= 0:
            self.investment = investment
        else :
            print(f"{investment} needs to be a float and +$")
        
        type = type.title()

        if type in FundingRound.Examples:
            self.type = type 
        else :
            print(f"{type} is not Angel, Pre-Seed, Seed, Series A, Series B, Series C")
        FundingRound.all.append(self)
        


    @property
    def startup(self):
        return self._startup
    
    @property
    def venture_capitalist(self):
        return self._venture_capitalist
    

    

    

