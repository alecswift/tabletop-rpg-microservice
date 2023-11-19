# Tabletop RPG Random Number Generator Microservice

## How to programatically request data

First the file rng.py must be running, so that the main loop can detect data. The main service will write the data to the rng-input.txt file. the data should be written to this text file in the format of inclusive ranges, with each range being on the new line. Each range should be two numbers with a space in between them. For example, "1 2" could be one line which represents the inclusive range of 1 to 2. The rng-input.txt file currently has data within it as an example of the correct format. As the microservice rng.py file is running it will be scanning the text file using a loop and when the data is written to the text file the microservice will read this data as a request.

## How to programatically recieve data

Once the microservice has recieved the data, microservice will perform the necessary operations on the data. Inn this case generating random numbers from the given ranges. The random numbers will be written to the rng-output.txt file, so that the main service can recieve the output from the text file. The data will be written to the file in the format of individual numbers on each new line. Finally, the microservice will erase the data from the rng-input.txt file and continue scanning until new data is requested in the rng-input.txt file.

## UML Sequence Diagram




