# Filename: Vowels.py
# Author: Kiran Kandimalla
# Email address: KKandimalla_GPS@NEC.edu
# Description: Program that prompts the user for a string and then displays a count of each of the vowels (a, e, i, o, u) and the total number of vowels contained in that string.
# Last changed: 19-02-2024


# Program that prompts the user for a string and then displays a count of each of the vowels (a, e, i, o, u) and the total number of vowels contained in that string.
def count_vowels(string):
    # Define a set of vowels
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    # Initialize counts
    vowel_counts = {vowel: 0 for vowel in vowels}
    total_vowels = 0

    # Iterate through each character in the string
    for char in string:
        # Check if the character is a vowel
        if char in vowels:
            # Increment the count for that vowel
            vowel_counts[char] += 1
            # Increment the total count of vowels
            total_vowels += 1

    return vowel_counts, total_vowels


def main():
    # Prompt the user for input
    user_input = input("Enter a string: ")
    # Call the count_vowels function
    vowel_counts, total_vowels = count_vowels(user_input)

    # Display the counts
    print("\nCount of each vowel:")
    for vowel, count in vowel_counts.items():
        print(f"{vowel}: {count}")

    # Display the total number of vowels found in the string
    print("\nTotal number of vowels:", total_vowels)


if __name__ == "__main__":
    main()
