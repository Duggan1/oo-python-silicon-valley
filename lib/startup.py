from .funding_round import FundingRound
from .venture_capitalist import VentureCapitalist

class Startup:
   all = []

   def __init__(self, name, founder, domain):
      self.name = name 
      self._founder = founder
      self._domain = domain
      Startup.all.append(self)

   @property
   def founder(self):
      return self._founder
   
   @property
   def domain(self):
      return self._domain 
   
   @classmethod
   @property
   def domains(cls):
      return [ s._domain for s in cls.all  ]

   def pivot(self, newName, newDomain):
      self.name = newName
      self._domain = newDomain

   @classmethod
   def find_by_founder(cls, founder):

      for su in cls.all:
         if su.founder == founder:
            return su 
      print("No Startup")
      return None
   
   def sign_contract(self,venture_capitalist, type, investment ):
      FundingRound( self, venture_capitalist, type, investment)

   def num_funding_rounds(self):
      return len([r for r in FundingRound.all if r.startup == self])
   
   @property
   def total_funds(self):
      return sum([ fr.investment for fr in FundingRound.all if fr.startup == self])
   
   @property
   def investors(self):
      return list({fr.venture_capitalist.name for fr in FundingRound.all if fr.startup == self   })
       
   @property
   def big_investors(self):
      return list({fr.venture_capitalist.name for fr in FundingRound.all if fr.startup == self and  fr.venture_capitalist in VentureCapitalist.tres_commas_club })
   







    
