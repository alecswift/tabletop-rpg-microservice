"""The microservice will recieve user selected parameters (list of ranges) and data from a
tabletop rpg random encounter generator application. From the parameters
the microservice will generate a series of random numbers that will be used to
pull corresponding data and return this data to the primary application"""

import random

def main():
    while True:
        with open("rng-input.txt", "r", encoding = "utf-8") as in_file:
             file_data = in_file.read()
        
        ranges = []

        for line in file_data.split("\n"):
            str_nums = line.split(" ")
            try:
                start, end = int(str_nums[0]), int(str_nums[1])
            except:

        ranges = [(line.split(" ")) for line in file_data.split("\n")]

def rng(ranges: list[tuple[int, int]]) -> list[int]:
    """Returns a list of random numbers from the given list of inclusive ranges"""
    random_numbers = []

    for start, end in ranges:
        random_number = random.randint(start, end)
        random_numbers.append(random_number)

    return random_numbers
