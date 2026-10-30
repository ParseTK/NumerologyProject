"""
Name: Tyler Kirchner
Assignment: Numerology inheritance
Reflection: I love OOP!
            Decorators make it easy to extend method behavior, it helps coders write better code
            by utilizing the ability to add functionality in a reuseable way.
            1. I learned more about inheritance and creating efficient code.
            2. Learned more about caching, eager loading and lazy loading.
"""
from Numerology import NumerologyLifePathDetails
from constants import VOWELS


def validate_name(name: str) -> bool:
    """
    Validates the name.
    Checks for empty input.
    Checks for no special characters or digits.
    Checks for vowels in name.
    :param name:
    :return: boolean
    """
    valid_name: bool = False
    if len(name.strip()) == 0:
        return False

    for char in name:
        if not (char.isalpha() or char.isspace()):
            return False
        if char.lower() in VOWELS:
            valid_name = True

    if not valid_name:
        return False

    return valid_name


def get_user_input() -> tuple[str, str]:
    """
    Gets user's name and Birthdate as strings and returns them as a tuple.
    :return: tuple[str, str]
    """
    while True:
        name: str = input("Enter full name: ").strip()
        if validate_name(name):
            break
        print("Name must contain only letters and spaces.")

    while True:
        birthday: str = input("Format: mm-dd-yyyy or mm/dd/yyyy. Enter birthday: ")
        print()
        if NumerologyLifePathDetails.is_valid_date(birthday):
            break
        print("Invalid date... Format: mm-dd-yyyy or mm/dd/yyyy")
    return name, birthday


def main() -> None:
    """
    Main entry point of the program.
    :return: None
    """
    name, birthday = get_user_input()
    numerology: NumerologyLifePathDetails = NumerologyLifePathDetails(name, birthday)
    print(numerology)
    print(f"LIFE PATH DESCRIPTION\n {numerology.get_life_path_description}")


if __name__ == "__main__":
    main()