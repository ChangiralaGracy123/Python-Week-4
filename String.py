# Filename: String.py
# Author: Gracy Changirala
# Email address: GChangirala_GPS@nec.edu
# Description: A program that asks the user to enter a string
# Last changed: 19-02-2024

# A program that asks the user to enter a string
def capitalize_vowels(string):
    # Define all vowels
    vowels = "aeiou"
    modified_string = ""  # Initialize an empty string to store the modified string
    # Iterate over each character in the input string
    for char in string:
        # If the character is a vowel, capitalize it and add to modified string
        if char in vowels:
            modified_string += char.upper()
        # If the character is not a vowel, keep it unchanged
        else:
            modified_string += char
    return modified_string  # Return the modified string


def main():
    user_string = input("Enter a string: ")  # Prompt user to input a string
    print("Length of string:", len(user_string))  # Display length of the string
    modified_string = capitalize_vowels(user_string)  # Capitalize vowels in the string
    print("Modified string with capitalized vowels:", modified_string)  # Display modified string
    words = user_string.split()  # Split the string into a list of words
    print("Number of words:", len(words))  # Display the number of words


if __name__ == "__main__":
    main()  # Call the main function to execute the program


# Description:
# This function takes a string input and returns a modified version of the string where all vowels are capitalized.
# This function is the entry point of the program. It prompts the user to enter a string, calls the capitalize_vowels function to modify the string, calculates and displays the length of the original string, displays the modified string with capitalized vowels, and finally counts and displays the number of words in the original string.
# The program ensures that it only executes when run directly as a script (not when imported as a module) by checking the __name__ variable. If it is run as the main script (__name__ == "__main__"), it calls the main function to start the execution.
