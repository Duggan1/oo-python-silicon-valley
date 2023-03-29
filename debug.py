from lib import *

# code here
# e.g.


s1 = Startup( 'Pied Piper', 'Richard Hendricks', 'www.pp.com' )

vc1 = VentureCapitalist( 'Peter Gregory', 10000000000 )
vc2 = VentureCapitalist( 'Peter dinosao', 1333330000008888888888888800 )
vc3 = VentureCapitalist( 'aom from canada', 166990 )

fr1 = FundingRound( s1, vc1, "Series C", 200000.99 )
fr2 = FundingRound( s1, vc2, "Pre-Seed", 133333000.00 )
fr3 = FundingRound(s1 , vc2, "Seed",133333000.99)
fr4 = FundingRound( s1, vc3, "Seed", 1330.00 )
fr5 = FundingRound(s1, vc3, "Seed", 99.00)


# vc1 = VentureCapitalist( 'Peter Gregory', 1000000000 )
# Angel, Pre-Seed, Seed, Series A, Series B, Series C







# do not remove
import ipdb; ipdb.set_trace()
