"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = []
    # start coding here
    for i in items:
        frequencies.append(str(i))
    temp = frequencies
    frequencies = dict((i, temp.count(i)) for i in temp)
    print(frequencies)
    return frequencies