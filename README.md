# Numerology

A command-line Python program that takes a full name and a birthday and works out a set of numerology numbers from them.

## What it does

- Validates the name (letters and spaces, at least one vowel) and the birthday (`mm-dd-yyyy` or `mm/dd/yyyy`, a real date).
- Calculates the life path, birth day, attitude, soul, personality and power name numbers.
- `NumerologyLifePathDetails` extends the `Numerology` class with a life path description, to practise inheritance.

## Run it

Needs Python 3.10 or newer, with no other packages.

```
python UseNumerologyInherit.py
```

## Files

- `Numerology.py`: the `Numerology` class and the `NumerologyLifePathDetails` subclass
- `UseNumerologyInherit.py`: the program that asks for input and prints the results
- `constants.py`: the letter-to-number map and the vowels

## Notes

This was a coursework project (object-oriented programming and inheritance).
