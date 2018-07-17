import time

start_time = time.clock()  # The clock function


def main():
    frequencies = {}
    text_file = input("What is the name of the text file you want to read? ")
    File_object = open(text_file, 'r')  # You can put in the name of the file here
    lines = (File_object).readlines()  # Read the file and sort it into a list
    File_object.close()

    for i in lines:  # Adds the numbers from the text file to the dictionary
        if float(i) in frequencies:
            frequencies[int(i)] += 1
        else:
            frequencies[int(i)] = 1

    def minimums(dictionary):
        min_value = float("inf")  # first lowest number must be the greatest possible entity to compare to
        for k, v in dictionary.items():
            if v < min_value:  # If smallest value is less than the previous
                min_value = v  # Now you replace the smallest value

        nums = ''  # Create this string in order to store the smallest value(s)

        for k, v in dictionary.items():  # Adds the smallest number(s) to a string
            if v == min_value:
                nums += str(k) + ', '
        print("The number(s) that appeared the least amount of times is/are: " + nums.rstrip(
            ', ') + " with a frequency of: " + str(min_value))  # The final print statement

    minimums(frequencies)


main()  # Call the main function
print("the code runs for: " + str((time.clock() - start_time) * 1000) + " milliseconds")  # Final statement printed out

# Advantages:
# On average, ran file1 and file2 faster compared to the other program
# Dictionaries are literally the ideal data structure in this case because you only need to deal with keys and values
# They don't require indexes unlike the other program
# This is why the program runs faster when dealing with larger text files

# Disadvatages:
# Requires more memory due to hashing process compared to the other program
# Essentially, all of the numbers in the text file are the "keys" and the amounts of time they appear are the hashes
# The hash function attributes all of the keys to their appropriate value
# When dealing with smaller text files, the hashing processes will cause this program to run slower

