from pprint import pprint
import random


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
    """ Creates a number of events.

    :param num_events:
    :param width: width where events randomly allocated
    :param height: height where events randomly allocated
    :return: a list of events.

    """
    events = []
    for j in range(num_events):
        x = random.randint(0, width)
        y = random.randint(0, height)
        events.append([x, y])

    return events


def move_events(events, width, height):
    """ Move events randomly in four directions.

    :param events: 
    :param width: width where events randomly walk.
    :param height: height where events randomly walk.
    :return:

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


if __name__ == "__main__":

    num_individuals = 5  # number of individuals
    width = 10
    height = 10
    start_capital = 10
    num_lucky_events = 5
    num_unlucky_events = 7
    simulation_steps = 80

    # Create a list of individuals
    individuals = create_individuals(num_individuals, start_capital, width, height)

    # Create a lucky_events and unlucky_events
    lucky_events = create_events(num_lucky_events, width, height)
    unlucky_events = create_events(num_unlucky_events, width, height)

    pprint(individuals)

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

