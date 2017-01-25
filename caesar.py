def alphabet_position(letter):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    letter = letter.lower()
    ix = 0
    while ix < len(alphabet):
        if alphabet [ix] == letter:
            return ix
        else:
            ix = ix+1

def rotate_character(char,rot):


    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for i in range(len(alphabet)):
        if char == alphabet[i]:
            return alphabet[(i+rot)%26]
        elif char == alphabet1[i]:
            return alphabet1[(i+rot)%26]
    return char


def encrypt(text,rot):

    new_text = ''
    for char in text:
        new_text = new_text + rotate_character(char,rot)

    return new_text
