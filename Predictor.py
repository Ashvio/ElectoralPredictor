from States import state_chance_hillary_pi, state_electors, states_hash, sc_obama_nate
from random import random, randrange, normalvariate
import matplotlib.pyplot as plt
import numpy as np
import os
import sys

plt.rcdefaults()

def calc_average_electoral_vote():
    hillary_counter = 0
    for state in state_electors.keys():
        hillary_counter += (state_chance_hillary_pi[state] / 100) * state_electors[state]

    print(hillary_counter)


def convert(outcomes):
    new_array = [0] * 538
    for i in range(538):
        new_array[i] = outcomes.count(i)

    return new_array





def graph_outcomes(demo_outcomes, trump_outcomes, demo, repub):
    demo_outcomes = convert(demo_outcomes)
    # trump_outcomes = convert(trump_outcomes)
    n_groups = 2
    index = np.arange(538)
    bar_width = .25
    opacity = .8
    fig, ax = plt.subplots()

    rects1 = plt.bar(index, demo_outcomes, bar_width,
                     alpha=opacity,
                     color='blue',
                     label=demo)

    # rects2 = plt.bar(index, trump_outcomes, bar_width,
    #                  alpha=opacity,
    #                  color='r',
    #                  label=repub)

    plt.xlabel("Electoral Votes")
    plt.ylabel("Simulations")
    plt.title("Election outcome chart")
    plt.legend()
    plt.tight_layout()
    plt.show()


def run_simulations(count, state_chance_demo, how="random_distribution", demo="Hillary", repub="Trump" ):

    state_map = dict.fromkeys(state_electors.keys())
    demo_outcomes = []
    trump_outcomes = []
    demo_wins = 0
    demo_stomps = 0
    trump_stomps = 0
    for i in range(count):
        demo_count = 0
        trump_count = 0
        dependent_factor = normalvariate(0, .08)
        # print(dependent_factor)
        # dependent_factor = randrange(9, 16)/12
        for state in state_electors.keys():
            rand = random()
            demo_chance = (state_chance_demo[state] / 100)
            solidity = np.math.ceil(abs(abs(.5 - demo_chance) * 2 - 1) + .1)
            demo_chance = demo_chance + (dependent_factor*solidity)

            if demo_chance < 0:
                demo_chance = 0
            electors = state_electors[state]
            if rand < demo_chance:
                demo_count += electors
            else:
                trump_count += electors
        demo_outcomes.append(demo_count)
        trump_outcomes.append(trump_count)
        if demo_count > trump_count:
            demo_wins += 1
        if demo_count >= 370:
            demo_stomps += 1
        if trump_count >= 370:
            trump_stomps += 1

    graph_outcomes(demo_outcomes, trump_outcomes, demo, repub)
    print("{demo} wins {demo_wins} out of {count} simulations. ({percent}%)".format(demo=demo, demo_wins=demo_wins,
                                                                                    count=count, percent=demo_wins*100/count))
    print("{demo} landslides {demo_stomps} out of {count} simulations ({percent}%)".format(demo=demo, demo_stomps=demo_stomps,
                                                                                           count=count, percent=demo_stomps*100/count))
    print("{repub} landslides {trump_stomps} out of {count} simulations ({percent}%)".format(repub=repub, trump_stomps=trump_stomps,
                                                                                           count=count,
                                                                                           percent=trump_stomps *100/ count))
    #print(outcomes)


if sys.version_info[0] == 2:
    virtualprefix = sys.prefix
    sys.prefix = sys.real_prefix
    import FixTk

    if "TCL_LIBRARY" not in os.environ:
        # reload module, so that sys.real_prefix be used
        reload(FixTk)
    sys.prefix = virtualprefix
else:  # Python 3
    virtualprefix = sys.base_prefix
    sys.base_prefix = sys.real_prefix
    from tkinter import _fix

    if "TCL_LIBRARY" not in os.environ:
        # reload module, so that sys.real_prefix be used
        from imp import reload

        reload(_fix)
    sys.base_prefix = virtualprefix

calc_average_electoral_vote()
run_simulations(100000, sc_obama_nate, demo="Obama", repub="Romney")
run_simulations(100000, state_chance_hillary_pi)