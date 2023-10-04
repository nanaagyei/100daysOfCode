# Morse Code Converter

This Python script contains a function `text_to_morse(text)` that converts a given text into Morse code.

## Function Details

### text_to_morse(text)

This function takes a string `text` as an input and returns the Morse code equivalent of the text.

#### Parameters:

- `text` (str): The text to be converted to Morse code.

#### Returns:

- `morse_text` (str): The Morse code equivalent of the input text.

#### Code Explanation:

The function first defines a dictionary `morse_code` where each key-value pair represents a character and its corresponding Morse code.

Then, it initializes an empty string `morse_text`.

Next, it iterates over each character in the input text (converted to uppercase). For each character, it appends the corresponding Morse code (obtained from the `morse_code` dictionary) to `morse_text`. If a character does not exist in the dictionary, it appends an empty string.

Finally, it returns `morse_text` after removing leading and trailing spaces.
