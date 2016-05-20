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
    hill_stomps = 0
    trump_stomps = 0
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
        if hillary_count > 370:
            hill_stomps += 1
        if trump_count > 370:
            trump_stomps += 1
    # print(outcomes)
    print("Hillary wins {hill_wins} out of {count} simulations. ({percent}%)".format(hill_wins=hill_wins,
                                                                                    count=count, percent=hill_wins*100/count))
    print("Hillary landslides {hill_stomps} out of {count} simulations ({percent}%)".format(hill_stomps=hill_stomps,
                                                                                           count=count, percent=hill_stomps*100/count))
    print("Trump landslides {trump_stomps} out of {count} simulations ({percent}%)".format(trump_stomps=trump_stomps,
                                                                                           count=count,
                                                                                           percent=trump_stomps *100/ count))
calc_average_electoral_vote()
run_simulations(100000)
