#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
This module defines get_bands and convert(), which
take colours of bands from the console and returns
the computed resistance and tolerance values.
"""
# Define global dictionaries
COLOURS = {
    'black': 0,
    'brown': 1,
    'red': 2,
    'orange': 3,
    'yellow': 4,
    'green': 5,
    'blue': 6,
    'violet': 7,
    'grey': 8,
    'white': 9,
    'gold': -1,
    'silver': -2
}

MARGIN = {
    'brown': 1,
    'red': 2,
    'orange': 3,
    'yellow': 4,
    'green': 0.5,
    'blue': 0.25,
    'violet': 0.1,
    'grey': 0.05,
    'gold': 5,
    'silver': 10,
    'blank': 20
}

def get_bands():
    """
    Get the colours of bands from console. Make sure that
    at least three are given. If there are exactly three,
    add 'blank' as the fourth.
    """
    bands = []

    while len(bands) < 3:
        print "Please give me at least three bands."
        bands = raw_input('Bands:').split(" ")

    if len(bands) == 3:
        bands.append('blank')
 
    return bands

def convert_bands(bands):
    """
    Assume that resistors have at least four bands: two
    significant figures, one multiplier, one margin. If
    five bands are specified, then there are three s.f.
    Segment bands list into figures, factor, and margin,
    then compute the resistance + tolerance.
    """
    value = 0
    figures = [COLOURS[band] for band in bands[:-2]]
    factor = bands[-2]
    margin = bands[-1]

    # multiply the significant figures here
    for fig in figures:
        value += fig
        value *= 10

    # then apply the multiplier, less one
    value *= (10 ** (COLOURS[factor]-1))

    # tolerance is computed using the second dict
    tolerance = value * 0.01 * MARGIN[margin]

    return (value, tolerance)

def main():
    """
    Filler function just to run the computation.
    """
    result = convert_bands(get_bands())
    print "{0} ± {1} Ω ".format(result[0], result[1])

if __name__ == '__main__':
    main()
