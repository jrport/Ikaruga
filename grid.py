import random
import numpy

SHIP_WIDTH: int = 48

UPPER_BOUND = 50
LEFT_BOUND = 45
RIGHT_BOUND = 630
BOTTOM_BOUND = 540
HORIZONTAL_RANGE: int = LEFT_BOUND - RIGHT_BOUND 

PLACEMENT_MATRIX: list[list[int]] = numpy.zeros((3,12), dtype=int)
POSITION_MATRIX: list[list[int]] = numpy.zeros((3,12,2), dtype=int)

X_COORD: int = LEFT_BOUND
Y_COORD: int = UPPER_BOUND
for t in range(3):
    X_COORD = UPPER_BOUND
    for i in range(12):
        POSITION_MATRIX[t, i, 0] = X_COORD
        X_COORD += 48

for t in range(3):
    for i in range(12):
        POSITION_MATRIX[t, i, 1] = Y_COORD
    Y_COORD += 50

def generate_placement(Matrix: list[list[list[int]]], enemy_count) -> list[list[list[int]]]:
    for enemy in range(enemy_count):
        Matrix[random.randint(0,2), random.randint(0,11)] = 1

