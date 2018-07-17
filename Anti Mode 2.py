import time

start_time = time.clock()  # Time function


def main():
    frequencies = [[]]  # Create a 2d list to store all of the numbers
    text_file = input("What is the name of the text file that you want to open? ")
    File_object = open(text_file, 'r')  # Read the text file
    lines = (File_object).readlines()  # Organize the text file into a list
    File_object.close()

    for i in range(0, len(lines)):  # Adds the numbers from the text file into the 2d list
        condition = False
        for j in range(0, len(frequencies)):
            if i == 0:  # You need to append the first value no matter what
                frequencies[0] = [int(lines[0]), 1]
                condition = False
                break  # Breaks the loop because it's pointless to check afterwards
            elif int(lines[i]) == frequencies[j][0]:
                frequencies[j][1] += 1
                condition = False
                break
            elif int(lines[i]) != frequencies[j][0]:
                condition = True

        if condition is True:  # If the number from the text file is not in frequencies
            frequencies.append([int(lines[i]), 1])

    def minimums(list):  # Finds the most frequent number
        min_value = float("inf")  # first lowest number must be the greatest possible entity to compare to
        for i in range(0, len(list)):
            if list[i][1] < min_value:  # If smallest value is less than the previous
                min_value = list[i][1]  # Then replace the minimum value
        nums = ""

        for z in range(0, len(list)):  # Check every item in the 2d list and check if it matches the minimum value
            if list[z][1] == min_value:
                nums += str(list[z][0]) + ', '  # Add the number to the string if it's a minimum value
        print("The number(s) that appeared the least amount of times is/are: " + nums.rstrip(
            ', ') + " with a frequency of: " + str(min_value))  # Final print line

    minimums(frequencies)


main()
print("the code runs for: " + str((time.clock() - start_time) * 1000) + " milliseconds")

# Advantages:
# On average, this program figured out the antimode in file3 faster than the other program
# Lists don't use hashing, and also take up less memory

# Disadvantages:
# Was slower compared to the other program for finding the antimode in files 1 and 2
# More logic involved due to more comparisons between data
# Unecessary used of indexes, there isn't a use for them in this case


