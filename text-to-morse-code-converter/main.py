def text_to_morse(text):
    morse_code = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
        'Y': '-.--', 'Z': '--..', ' ': ' / ', '0': '-----', '1': '.----', '2': '..---', 
        '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', 
        '9': '----.'
    }
    
    morse_text = ''
    for char in text.upper():
        morse_text += morse_code.get(char, '') + ' '
    
    return morse_text.strip()


if __name__ == "__main__":
    text = input("Enter the text to convert to morse code: ")
    print(text_to_morse(text))