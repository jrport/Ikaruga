from typing import Any
import numpy
from numpy import ndarray, zeros

# Esse código gerará algumas matrizes úteis pra criação e geração randomizada e procedural dos 
# inimigos.

# Primeiro algumas constantes,

SHIP_WIDTH: int = 48

UPPER_BOUND = 50
LEFT_BOUND = 45
RIGHT_BOUND = 630
BOTTOM_BOUND = 540
HORIZONTAL_RANGE: int = LEFT_BOUND - RIGHT_BOUND 

# Essa matriz tridimensional permitirá que discretizemos todas as 36 posições possíveis
# para as naves inimigas spawnarem e assim facilmente as indexaremos.

POSITION_MATRIX: numpy.ndarray[numpy.ndarray[Any, Any], numpy.int_] = numpy.zeros((3,12,2))

x_coord: int = LEFT_BOUND
y_coord: int = UPPER_BOUND


for t in range(3):
    x_coord = UPPER_BOUND
    for i in range(12):
        POSITION_MATRIX[t, i, 0] = x_coord
        x_coord += 48

for t in range(3):
    for i in range(12):
        POSITION_MATRIX[t, i, 1] = y_coord
    y_coord += 50
