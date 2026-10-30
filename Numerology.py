import re
from datetime import datetime
from constants import VOWELS, LETTER_MAP, WIDTH


class Numerology:
    def __init__(self, name: str, birthdate: str) -> None:
        """
        Constructor for Numerology class
        :param name, birthdate:
        :return:
        """
        self.__name: str = name.lower()
        self.__birthdate: str = birthdate.replace("/", "-")
        month, day, year = self.__extract_date()
        date_number: int = Numerology.__get_date_number(self.birthdate)
        self.__life_path: int = Numerology.__reduce_number(date_number)
        self.__birth_day: int = Numerology.__reduce_number(day)
        self.__attitude: int = Numerology.__reduce_number(month + day)

        soul_total: int = 0
        personality_total: int = 0
        for char in self.__name:
            if char.isalpha():
                if char in VOWELS:
                    soul_total += LETTER_MAP[char]
                else:
                    personality_total += LETTER_MAP[char]
        self.__soul: int = Numerology.__reduce_number(soul_total)
        self.__personality: int = Numerology.__reduce_number(personality_total)
        self.__power_name: int = Numerology.__reduce_number(soul_total + personality_total)


    @property
    def name(self) -> str:
        """
        Returns the name of the numerology object
        :return: str
        """
        return self.__name


    @property
    def birthdate(self) -> str:
        """
        Returns the birthdate of the numerology object
        :return: str
        """
        return self.__birthdate


    @property
    def life_path(self) -> int:
        """
        Returns the life path of the numerology object.
        :return: int
        """
        return self.__life_path


    @property
    def birth_day(self) -> int:
        """
        Return the birth day of the numerology object.
        :return: int
        """
        return self.__birth_day


    @property
    def soul(self) -> int:
        """
        Returns the soul number of the numerology object
        :return: int
        """
        return self.__soul


    @property
    def attitude(self) -> int:
        """
        Returns the attitude number of the numerology object
        :return: int
        """
        return self.__attitude


    @property
    def personality(self) -> int:
        """
        Returns the personality number of the numerology object.
        :return: int
        """
        return self.__personality


    @property
    def power_name(self) -> int:
        """
        Returns the power name number of the numerology object
        :return: int
        """
        return self.__power_name


    def __str__(self) -> str:
        """
        Creates a string representation of the numerology object with formatting
        :return: str
        """
        return (
            f"Client Name: {self.name.title()}\n"
            f"Birthdate: {self.birthdate}\n\n"
            f"{'*--Numerology Report--*':^{WIDTH}}\n"
            f"Life Path:    {self.life_path:<{WIDTH}}\n"
            f"Birth Day:    {self.birth_day:<{WIDTH}}\n"
            f"Attitude:     {self.attitude:<{WIDTH}}\n"
            f"Soul:         {self.soul:<{WIDTH}}\n"
            f"Personality:  {self.personality:<{WIDTH}}\n"
            f"Power Name:   {self.power_name:<{WIDTH}}\n"
        )


    def __extract_date(self) -> tuple[int, int, int]:
        """
        Splits the birthdate of the numerology object into a tuple of strings
        returns the tuple elements as ints
        :return: tuple[int, int, int]
        """
        month, day, year = self.birthdate.split('-')
        return int(month), int(day), int(year)


    @staticmethod
    def __reduce_number(number: int) -> int:
        """
        Reduce a number to its digital root using the digital root formula (Often used in leetcode problems to solve the add digits problem.)
        Handles zero and negative numbers
        :param number:
        :return: int
        """
        n: int = int(number)
        if n <= 0:
            raise ValueError("Value must be greater than zero.")
        return 1 + (n - 1) % 9


    @staticmethod
    def __get_date_number(date_str: str) -> int:
        """
        Get the date as a raw value ex. 12-12-2012 = 12122012
        raises error if date number is not digits
        returns the raw date number as an int
        :param date_str:
        :return: int
        """
        date_number: str = date_str.replace("-", "")
        if not date_number.isdigit():
            raise ValueError("Invalid date")
        return int(date_number)


    @staticmethod
    def is_valid_date_format(date_to_test: str) -> bool:
        """
        This code checks using regex to make sure a date
        Positions STARTS 1 and 2 are numbers
        Position 3 has -
        Positions 4 and 5 are numbers
        Position 6 has -
        Positions 7,8,9,10 are numbers"""
        return bool(re.match(r'^\d{2}[-/]\d{2}[-/]\d{4}$', date_to_test))

    @staticmethod
    def is_valid_date(date_to_test: str) -> bool:
        if not Numerology.is_valid_date_format(date_to_test):
            return False
        try:
            normalized_date: str = date_to_test.replace("/","-")
            date_numbers = Numerology.__get_date_number(normalized_date)
            datetime.strptime(str(date_numbers), '%m%d%Y')
            return True
        except ValueError as e:
            print("Invalid date", e)
            return False


class NumerologyLifePathDetails(Numerology):
    def __init__(self, name: str, birthdate: str) -> None:
        """
        Constructor for NumerologyLifePathDetails class
        Calls the parent constructor
        :param name, birthdate:
        :return:
        """
        super().__init__(name, birthdate)


    @property
    def get_life_path_description(self) -> str:
        """
        Returns a description of the life path number
        :return: str
        """
        descriptions: dict = {
            1: "The Independent: Wants to work/think for themselves",
            2: "The Mediator: Avoids conflict and wants love and harmony",
            3: "The Performer: Likes music, art and to perform or get attention",
            4: "The Teacher/Truth Seeker: Is meant to be a teacher or mentor and is truthful",
            5: "The Adventurer: Likes to travel and meet others, often a extrovert",
            6: "The Inner Child: Is meant to be a parent and/or one that is young at heart",
            7: "The Naturalist: Enjoy nature and water and alternative life paths, open to spirituality",
            8: "The Executive: Gravitates to money and power",
            9: "The Humanitarian: Helps others and/or experiences pain and learns the hard way"
        }
        return descriptions[self.life_path]