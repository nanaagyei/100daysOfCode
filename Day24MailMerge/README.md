# Personalized Letter Generator

## Overview
This Personalized Letter Generator is a Python script that automates the creation of customized letters. It reads a list of names from a file and uses a template letter, inserting each name into the letter to generate personalized versions. The script is ideal for mass mailing scenarios where personalization is required.

## Files in the Project
- `main.py`: The primary script that handles reading names, generating personalized letters, and saving them as separate files.

## How to Set Up
1. Ensure Python is installed on your system.
2. Create two directories: `Input` and `Output`.
3. Inside the `Input` directory, create two subdirectories: `Names` and `Letters`.
4. Place a file with names (`invited_names.txt`) in the `Names` directory.
5. Place your letter template (`starting_letter.txt`) in the `Letters` directory, with a placeholder for the name.
6. Run `main.py`.

## Using the Script
- The script replaces the placeholder in the letter template with each name from the names file.
- Personalized letters are saved in the `Output/ReadyToSend` directory, named as `letter_for_[name].txt`.

## Dependencies
- Python 3.x

## Credits
Developed by Prince. This script is designed to streamline the process of creating personalized letters for events, marketing campaigns, or personal use.
