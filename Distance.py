# Filename: Distance.py
# Author: Gracy Changirala
# Email address: GChangirala_GPS@nec.edu
# Description: Program that prompts the user for a distance in meters and then displays that distance converted to miles, feet and inches*.
# Last changed: 19-02-2024


# Program that prompts the user for a distance in meters and then displays that distance converted to miles, feet and inches*.

def meters_to_miles_feet_inches(distance_in_meters):
    """
    Convert distance in meters to miles, feet, and inches.

    Args:
    distance_in_meters (float): Distance in meters to be converted.

    Returns:
    tuple: A tuple containing the converted distance in miles, feet, and inches.
    """
    # Conversion factors
    meter_to_mile = 0.000621371
    mile_to_feet = 5280
    feet_to_inches = 12

    # Convert meters to miles
    miles = distance_in_meters * meter_to_mile
    # Extract the integer part of miles
    miles_integer = int(miles)
    # Extract the decimal part of miles and convert to feet
    feet_decimal = (miles - miles_integer) * mile_to_feet
    # Extract the integer part of feet
    feet_integer = int(feet_decimal)
    # Extract the decimal part of feet and convert to inches
    inches_decimal = (feet_decimal - feet_integer) * feet_to_inches
    # Extract the integer part of inches
    inches_integer = int(inches_decimal)

    return miles_integer, feet_integer, inches_integer

def main():
    """
    Main function to execute the program.
    """
    # Prompt the user to input distance in meters
    distance_in_meters = float(input("Enter a distance in meters: "))
    # Convert meters to miles, feet, and inches
    miles, feet, inches = meters_to_miles_feet_inches(distance_in_meters)
    # Display the converted distance
    print(f"{distance_in_meters} meters = {miles} miles, {feet} feet, {inches} inches")

if __name__ == "__main__":
    main()
