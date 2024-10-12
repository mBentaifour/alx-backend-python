#!/usr/bin/env python3

'''task 8 module
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:

    '''creates a multiplier function
    '''
    return lambda x: x * multiplier
