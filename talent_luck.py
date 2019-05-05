from pprint import pprint
import random


def create_individuals(num, start_capital, width, height):
    individuals = []
    for n in range(num):
        # randomly put individuals on the grid
        x = random.randint(0, width)
        y = random.randint(0, height)

        individual = {"position": [x, y], "capital": start_capital, "talent": random.random()}
        individuals.append(individual)
    return individuals


def create_events(num_lucky_events, num_unlucky_events, width, height):
    lucky_events = []
    for j in range(num_lucky_events):
        x = random.randint(0, width)
        y = random.randint(0, height)
        lucky_events.append([x, y])

    unlucky_events = []
    for n in range(num_unlucky_events):
        x = random.randint(0, width)
        y = random.randint(0, height)
        unlucky_events.append([x, y])

    return lucky_events, unlucky_events


def move_events(events):
    for event in events:
        # 4 - up, 5 - down, 6 - left, 7 - right
        direction = random.choice([4, 5, 6, 7])
        if direction == 4:
            event[1] += 1

        elif direction == 5:
            event[1] -= 1

        elif direction == 6:
            event[0] -= 1

        elif direction == 7:
            event[0] += 1

    return events


num_individuals = 5  # number of individuals
width = 10
height = 10
start_capital = 10


# create list of individuals
individuals = create_individuals(num_individuals, start_capital, width, height)
lucky_events, unlucky_events = create_events(5, 5, width, height)

pprint(individuals)
simulation_steps = 80

# expected value
# how to calculate
for t in range(simulation_steps):
    # print(f"Step: {step}")
    lucky_events = move_events(lucky_events)
    unlucky_events = move_events(unlucky_events)

    for individual in individuals:
        if individual["position"] in lucky_events:
            individual["capital"] = individual["capital"] * 2

        if individual["position"] in unlucky_events:
            individual["capital"] = individual["capital"] / 2


pprint(individuals)



# create table of the events
# define what is it lucky and unlucky event
# uniform distribution