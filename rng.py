"""The microservice will recieve user selected parameters (list of ranges) and data from a
tabletop rpg random encounter generator application. From the parameters
the microservice will generate a series of random numbers that will be used to
pull corresponding data and return this data to the primary application"""

import random

def main():
    while True:
        with open("rng-input.txt", "r", encoding = "utf-8") as in_file:
             file_data = in_file.read()
        
        ranges = parse(file_data)

        if not ranges:
            continue
        
        random_numbers = rng(ranges)

        with open("prng-service.txt", "w", encoding = "utf-8") as out_file:
            for num in random_numbers:
                out_file.write(num)


def parse(input_data: str) -> list[tuple[int, int]]:
    """
    Recieves input data in the form of a string and returns a list
    of ranges
    """
    ranges = []

    for line in input_data.split("\n"):
        str_nums = line.split(" ")
        try:
            range = int(str_nums[0]), int(str_nums[1])
        except TypeError:
            print("Input data is not numeric")
        
        ranges.append(range)
    
    return ranges


def rng(ranges: list[tuple[int, int]]) -> list[int]:
    """Returns a list of random numbers from the given list of inclusive ranges"""
    random_numbers = []

    for start, end in ranges:
        random_number = random.randint(start, end)
        random_numbers.append(random_number)

    return random_numbers

if __name__ == "__main__":
    main()