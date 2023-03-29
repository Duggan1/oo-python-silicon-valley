from .funding_round import FundingRound
from lib.startup import *


class VentureCapitalist:
    
    all = []
    tres_commas_club = []


    def __init__(self, name:str, total_worth:float):
        self.name = name 
        self.total_worth = total_worth
        VentureCapitalist.all.append(self)
        if total_worth > 1000000000:
            VentureCapitalist.tres_commas_club.append(self)


    def offer_contract(self, startup, type, investment ):
        FundingRound(startup, self, type, investment )

    @property
    def funding_rounds(self):
        return [fr for fr in FundingRound.all if fr.venture_capitalist == self]
    
    @property
    def portfolio(self):
        return [fr.startup for fr in self.funding_rounds]
    
    @property
    def biggest_investment(self):
        standard = 0
        for fr in self.funding_rounds:
            if fr.investment > standard:
                standard = fr.investment
        return standard
    
    def invested(self,domain):
        for fr in self.funding_rounds:
            if fr.startup.domain == domain:
                return fr.startup.total_funds 

# .total_funds
