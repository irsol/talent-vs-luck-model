from pprint import pprint
import random
import csv 


def create_individuals(num, start_capital, width, height):
    """ Creates a list of individuals randomly located on a grid.

    :param num: number of individuals to create
    :param start_capital: initial amount of capital for each individual
    :param width:  width of the grid where individuals will be located
    :param height: height of the grid where individuals will be located
    :return: list of individuals

    """

    individuals = []
    for n in range(num):
        # randomly put individuals on the grid
        x = random.randint(0, width)
        y = random.randint(0, height)

        individual = {"position": [x, y], "capital": start_capital, "talent": random.random()}
        individuals.append(individual)

    return individuals


def create_events(num_events, width, height):
    """ Creates a list of events

    :param num_events: the number of events to create
    :param width: width where events will be randomly located
    :param height: height where events will be randomly located
    :return: a list of events

    """
    events = []
    for j in range(num_events):
        x = random.randint(0, width)
        y = random.randint(0, height)
        events.append([x, y])

    return events


def move_events(events, width, height):
    """ Move every event from events randomly in one of four directions (up, down, left, right).
        Function changes positions of events inplace

    :param events: a list of events 
    :param width: width of the grid
    :param height: height of the grid
    :return: events

    """

    for event in events:
        x, y = event
        direction = random.choice(["up", "down", "left", "right"])
        if direction == "up":
            if y+1 < height:
                event[1] += 1

        elif direction == "down":
            if y-1 >= 0:
                event[1] -= 1

        elif direction == "left":
            if x-1 >= 0:
                event[0] -= 1

        elif direction == "right":
            if x+1 < width:
                event[0] += 1

    return events


def store_results(individuals):
    """ Store results of a simulation in csv file
    
    """
    rows = []
    
    for individual in individuals:
        row = individual["capital"], individual["talent"]
        # row = "{},{}".format(individual["capital"], individual["talent"])
        rows.append(row)

    with open('results.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(rows)


if __name__ == "__main__":

    num_individuals = 5
    width = 100
    height = 100
    start_capital = 10
    num_lucky_events = 25
    num_unlucky_events = 25
    simulation_steps = 180

    # Create a list of individuals
    individuals = create_individuals(num_individuals, start_capital, width, height)

    # Create a lucky_events and unlucky_events
    lucky_events = create_events(num_lucky_events, width, height)
    unlucky_events = create_events(num_unlucky_events, width, height)

    # pprint(individuals)

    for t in range(simulation_steps):
        # print(f"Step: {step}")
        lucky_events = move_events(lucky_events, width, height)
        unlucky_events = move_events(unlucky_events, width, height)

        for individual in individuals:
            if individual["position"] in lucky_events:
                individual["capital"] = individual["capital"] * 2

            if individual["position"] in unlucky_events:
                individual["capital"] = individual["capital"] / 2

    pprint(individuals)


    store_results(individuals)