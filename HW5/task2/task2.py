import pytest

"""Morse Code Translator"""

LETTER_TO_MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.',
    'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----',
    '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----',
    ', ': '--..--', '.': '.-.-.-', '?': '..--..',
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-',
    ' ': ' '
}

MORSE_TO_LETTER = {
    morse: letter
    for letter, morse in LETTER_TO_MORSE.items()
}


def decode(morse_message: str) -> str:
    """
    Декодирует строку из азбуки Морзе в английский
    """
    print(morse_message)
    decoded_letters = [
        MORSE_TO_LETTER[letter] for letter in morse_message.split()
    ]

    return ''.join(decoded_letters)


@pytest.mark.parametrize('morse_message, text_output', [
    ('... --- ...', 'SOS'),
    ('.... . .-.. .-.. --- -....- -.. .. .- -. .- -....- .... --- .-- -....- .- .-. . -....- -.-- --- ..- ..--..',
     'HELLO-DIANA-HOW-ARE-YOU?'),
    ('... .. -- .--. .-.. . -....- - . ... - -....- .-- -....- .--. -.-- - . ... - .-.-.- .--. .- .-. .- -- . - .-. '
     '.. --.. .',
     'SIMPLE-TEST-W-PYTEST.PARAMETRIZE')
])
def test_decode(morse_message: str, text_output: str):
    assert decode(morse_message) == text_output


@pytest.mark.parametrize('morse_message, error', [
    ('hello', KeyError),
    (123, AttributeError)
])
def test_exception(morse_message, error):
    with pytest.raises(error):
        decode(morse_message)


