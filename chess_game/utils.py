import numpy as np
import string


def string2int_coordinates(str_coords):
    letter = string.ascii_lowercase.index(str_coords[0])
    number = int(str_coords[1])-1
    return (letter, number)
