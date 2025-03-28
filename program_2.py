# Author: Michael Beaudet
# Title: Program 2 Week 9
# Date: 3/28/25

import random

def random_number_file():
# Ask user how many numbers they want generated
    count = int(input("Enter the number of random numbers (1-1000): "))
# Make sure the numbers are between 1 and 1000
    if 1 <= count <= 1000:
# If the numbers is between 1 and 1000 open the file and print the random numbers
        with open("random_numbers.txt", "w") as file:
            for _ in range(count):
                file.writelines(f"{random.randint(1, 500)}\n")
            print(f"{count} random numbers have been written to random_numbers.txt")
# Else display an error
    else:
        print("Invalid input. Please enter a numebr between 1 and 1000.")

if __name__ == "__main__":
    random_number_file()
