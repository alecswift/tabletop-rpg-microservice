"""The microservice will recieve user selected parameters (list of ranges) and data from a
tabletop rpg random encounter generator application. From the parameters
the microservice will generate a series of random numbers that will be used to
pull corresponding data and return this data to the primary application"""

def rng(ranges: list[tuple[int, int]]) -> list[int]:
    """"""
