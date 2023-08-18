import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}


# {"A": "Alfa", "B": "Bravo"}
phonetic_alphabets = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in phonetic_alphabets.iterrows()}


def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        phonetic_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetic()
    else:
        print(phonetic_list)


generate_phonetic()

