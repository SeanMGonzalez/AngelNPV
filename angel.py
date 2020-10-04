
import yaml, os
from creative import *
from types import SimpleNamespace


def ParametricAngel(cfg="config.yml"):

    if os.path.isfile(cfg):
        with open(cfg, 'r') as fp:
            ycfg = SimpleNamespace(**yaml.load(fp, Loader=yaml.FullLoader))
    else:
        raise ImportError("Yaml file does not exist.")

    equityNPVstay, equityNPVplay = calcEquityNPV( SimpleNamespace(**ycfg.equity))
    cashNPVstay, cashNPVplay = calcCashNPV( SimpleNamespace(**ycfg.cash))
    ipNPVstay, ipNPVplay = calcIPNPV( SimpleNamespace(**ycfg.ip))

    creativeEVstay, creativeEVplay = calcCreativeEV( SimpleNamespace(**ycfg.creative),
                                                     equityNPVstay, equityNPVplay,
                                                     cashNPVstay, cashNPVplay,
                                                     ipNPVstay, ipNPVplay )

    print(creativeEVstay)
    print(creativeEVplay)

if __name__ == "__main__":
    ParametricAngel()

# @click.command()
# # Cash Variables
# @click.option('--market_salary', default= 2e5, prompt='What yearly salary could you likely earn elsewhere? {$}')
# @click.option('--venture_salary', default= 0, prompt='What yearly salary is your venture currently paying you? {$}')
# @click.option('--projected_salary', default= 3.5e5, prompt='What maximum salary will your venture eventually pay you? {$}')
# @click.option('--projected_time', default= 4, prompt='When do you believe you will receive this maximum salary? {months}')
# @click.option('--runway', default= 2, prompt='What is your Runway? How many months can you currently go without a salary? {months}')
#
# # Equity Percentages
# @click.option('--your_percentage', default= 0.05, prompt='What percent equity have you earned? {%}')
# @click.option('--pot_percentage', default= 0.2, prompt='What is your equity stake? What maximum percentage do you expect to vest? {%}')
# @click.option('--your_schedule', default= 3, prompt='How many months are left until your equity is fully vested? {months}')
# # Equity Valuations
# @click.option('--your_valuation', default= 1e8, prompt='If you stay and realize your vision, what is the potential valuation of this venture? {$}')
# @click.option('--time2your_valuation', default= 5, prompt='When is this likely? {months}')
# @click.option('--likely_market_valuation', default= 5e7, prompt='If you leave, what is the likely market valuation of this venture? {$}')
# @click.option('--time2market_valuation', default= 5, prompt='When is this likely? {months}')
#
# # IP Variables
# @click.option('--contributing_ip', default= False, prompt='Did the venture formally recognize your IP contributions when you started? {T/F}')
# @click.option('--ip_rights', default= 0.8, prompt='Do you have rights to any IP you develop with the venture? {T/F}')
# @click.option('--ip_init_cost', default= 1e6, prompt='How much would it cost you to recreate the IP capabilities from scratch? {$}')
# @click.option('--ip_market_value', default= 1e5, prompt='What valuation would you assign legal use of this IP? {$}')
# @click.option('--ip_time2market', default= 3, prompt='How long would it take you to realize this valuation? {months}')
# @click.option('--ip_hump_cost', default= 2e5, prompt='How much would it cost you to realize this valuation? {$}')
#
#
# # Creative Variables
# @click.option('--creative_freedom', default= 0.3, prompt='Do you have creative freedom at your current venture? How much? {%}')
# @click.option('--freedom_elsewhere', default= 0.5, prompt='Can you get creative freedom somewhere else? How much? {%}')