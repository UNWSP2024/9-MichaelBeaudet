# Author: Michael Beaudet
# Title: Program 1 Week 9
# Date: 3/28/25

def count_file_lines():
# Open the file
    with open('names.txt', 'r') as file:
# Read the lines
        lines = file.readlines()
# Display the number of names
        print(f'The number of names in the file is: {len(lines)}')

if __name__ == '__main__':
    count_file_lines()