"""
Is the venture giving you creative freedom, agency? From None to Total (0-1), how much agency are they giving you?
Could you get the same freedom elsewhere? How confident are you?
How long before you could be in a similar position again?
How much venture cash, equity, IP, would you be willing to bet on that success?
How much lift

Sports Expected Value
(Amount won per bet * probability of winning) – (Amount lost per bet * probability of losing)

I'm treating this primarily as a cost, but that is all negative thinking.
I want to capture the value of creativity on the current project.
Issue is, this creates permutations?...
"""

from equity import *
from cash import *
from IP import *


def calcCreativeEV( ccfg,
                    equityNPVstay, equityNPVplay,
                    cashNPVstay, cashNPVplay,
                    ipNPVstay, ipNPVplay ):

    NPVstay = equityNPVstay + cashNPVstay + ipNPVstay
    NPVplay = equityNPVplay + cashNPVplay + ipNPVplay

    creativeNPVstay = NPVstay * ccfg.creative_freedom
    creativeNPVplay = NPVplay * ccfg.freedom_elsewhere

    creativeEVstay = creativeNPVstay - creativeNPVplay

    creativeEVplay = creativeNPVplay - creativeNPVstay

    return creativeEVstay, creativeEVplay


    # # You have some good options
    # if creative_freedom and freedom_elsewhere:
    #     opportunity_time = 0.5
    #
    # # You have a good thing where you are, hard to find something better
    # elif creative_freedom and not freedom_elsewhere:
    #     opportunity_time = 0.5
    #
    # # Staying is an investment
    # elif not creative_freedom and freedom_elsewhere:
    #     creativeNPV = ((current_value) / ((1 + inflation) ** opportunity_time)) - opportunity_bet
    #
    # # Why bother?! All about the money!
    # elif not creative_freedom and not freedom_elsewhere:
    #     return 0
    #
    # creativeNPV = ((current_value) / ((1 + inflation) ** (opportunity_time/freedom_elsewhere)) ) - opportunity_bet

    # return creativeNPV