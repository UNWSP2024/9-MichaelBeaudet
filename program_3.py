# Author: Michael Beaudet
# Title: Program 3 Week 9
# Date: 3/28/25

def sum_numbers_from_file():
# Initialize the total
    total = 0
    try: 
# Open the file
        with open('numbers.txt', 'r') as file:
            for line in file:
                try:
# Try to add the line to the total after converting it to an integer
                    total += int(line.strip())
# Display an error if it could not convert it to an integer
                except ValueError:
                    print(f"Error, unable to convert '{line.strip()}' to an integer")
# Display the total sum of the numbers in the file
        print(f"The total sum of the numbers is: {total}")
# Display an error if there is an IOError exception
    except IOError:
        print("Error, could not read the file")


if __name__ == '__main__':
    sum_numbers_from_file()