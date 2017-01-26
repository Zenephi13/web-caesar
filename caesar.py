def encrypt(text, rot):
    """Encrypts passed string by rotation amount"""
    new_text = ''

    for char in text:
        if char.isalpha():
            new_text += rotate_character(char, rot)

        else:
            new_text += char

    return new_text

def alphabet_position(letter):
    """Returns an index number based on the passed 
    letter's position in the alphabet"""
    mapping = "abcdefghijklmnopqrstuvwxyz"
    ind = mapping.index(letter)
    return ind

def rotate_character(char, rot):
    """Rotates the character based upon its index in 
    the alphabet and its rotation amount"""
    mapping = "abcdefghijklmnopqrstuvwxyz"
    low_char = char.lower()
    ind = alphabet_position(low_char)
    new_ind = (ind + rot) % 26
    new_char = mapping[new_ind]

    if char.isupper():
        return new_char.upper()

    else:
        return new_char