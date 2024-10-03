import sys

braille_alphabet = {
    'a': 'O.....',
    'b': 'O.O...',
    'c': 'OO....',
    'd': 'OO.O..',
    'e': 'O..O..',
    'f': 'OOO...',
    'g': 'OOOO..',
    'h': 'O.OO..',
    'i': '.OO...',
    'j': '.OOO..',
    'k': 'O...O.',
    'l': 'O.O.O.',
    'm': 'OO..O.',
    'n': 'OO.OO.',
    'o': 'O..OO.',
    'p': 'OOO.O.',
    'q': 'OOOOO.',
    'r': 'O.OOO.',
    's': '.OO.O.',
    't': '.OOOO.',
    'u': 'O...OO',
    'v': 'O.O.OO',
    'w': '.OOO.O',
    'x': 'OO..OO',
    'y': 'OO.OOO',
    'z': 'O..OOO',
    ' ': '......',
    ',': '.O....',
    '.': '.O.O..',
    '?': '.O..O.',
    '!': '.O.OO.',
    ':': '.OO...',
    ';': '.O.O..',
    '-': '..OO..',
    '/': '.O..O.',
    '>': 'O..O.O',
    '<': '.O.O.O',
    '(': '.OOOO.',
    ')': '.OOOO.'
}

braille_numbers = {
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..'
}

capital_symbol = '.....O'
number_symbol = '.O.OOO'
decimal_symbol = '.O.O.O'

def english_to_braille(text):
    result = []
    is_number = False
    for char in text:
        if char.isalpha():
            if char.isupper():
                result.append(capital_symbol)
                char = char.lower()
            if is_number:
                result.append('......')
                is_number = False
            result.append(braille_alphabet[char])
        elif char.isdigit():
            if not is_number:
                result.append(number_symbol)
                is_number = True
            result.append(braille_numbers[char])
        elif char == '.':
            if is_number:
                result.append(decimal_symbol)
            else:
                result.append(braille_alphabet[char])
        else:
            result.append(braille_alphabet.get(char, ''))
            is_number = False
    return ''.join(result)

def braille_to_english(braille):
    result = []
    symbols = [braille[i:i+6] for i in range(0, len(braille), 6)]
    capitalize_next = False
    is_number = False
    
    inv_alphabet = {v: k for k, v in braille_alphabet.items()}
    inv_numbers = {v: k for k, v in braille_numbers.items()}
    
    for symbol in symbols:
        if symbol == capital_symbol:
            capitalize_next = True
        elif symbol == number_symbol:
            is_number = True
        elif symbol == decimal_symbol:
            result.append('.')
        elif symbol == '......':
            result.append(' ')
            is_number = False
        else:
            if is_number:
                char = inv_numbers.get(symbol, inv_alphabet.get(symbol, ''))
            else:
                char = inv_alphabet.get(symbol, '')
                if capitalize_next:
                    char = char.upper()
                    capitalize_next = False
            result.append(char)
    return ''.join(result)

def is_braille(text):
    return all(c in 'O.' for c in text) and len(text) % 6 == 0

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a string to translate.")
        sys.exit(1)

    input_text = ' '.join(sys.argv[1:])
    
    if is_braille(input_text):
        print(braille_to_english(input_text))
    else:
        print(english_to_braille(input_text))

