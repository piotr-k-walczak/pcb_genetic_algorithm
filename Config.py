from enum import Enum


class SelectionType(Enum):
    TOURNAMENT = 0,
    ROULETTE = 1


SEED = 100
POPULATION = 500
GENERATIONS = 250
TOURNAMENT_SIZE = 40
CROSSOVER_PROBABILITY = .8
MUTATION_PROBABILITY = .1
DATA_PATH = "data/zad1.txt"
SELECTION_TYPE = SelectionType.TOURNAMENT
STOP_AFTER = 20

#scoring
LENGTH_WEIGHT = 10
SEGMENT_WEIGHT = 10
CROSSING_WEIGHT = 500
DISTANCE_OUTSIDE_WEIGHT = 50
FULL_SEGMENT_OUTSIDE_WEIGHT = 500


