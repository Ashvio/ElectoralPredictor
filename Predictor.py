from States import state_chance_hillary, state_electors, states_hash
from random import random
import matplotlib.pyplot as plt; plt.rcdefaults()

def calc_average_electoral_vote():
    hillary_counter = 0
    for state in state_electors.keys():
        hillary_counter += (state_chance_hillary[state] / 100) * state_electors[state]

    print(hillary_counter)


def run_simulations(count, how="random_distribution"):

    state_map =  dict.fromkeys(state_electors.keys())
    outcomes = []
    hill_wins = 0
    for i in range(count):
        hillary_count = 0
        trump_count = 0
        for state in state_electors.keys():
            rand = random()
            hill_chance = state_chance_hillary[state] / 100
            electors = state_electors[state]
            if rand < hill_chance:
                hillary_count += electors
            else:
                trump_count += electors
        outcomes.append((hillary_count, trump_count))
        if hillary_count > trump_count:
            hill_wins += 1
    print(outcomes)
    print(hill_wins)

calc_average_electoral_vote()
run_simulations(10000)
