def caesar(text: str, shift: int, encrypt: bool = True) -> str:
    """Performs Caesar cipher encryption or decryption."""
    if not isinstance(shift, int):
        raise TypeError('Shift must be an integer value.')
        
    if shift < 1 or shift > 25:
        raise ValueError('Shift must be an integer between 1 and 25.')
        
    if not encrypt:
        shift = -shift
        
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # Using modulo 26 ensures the shift wraps correctly regardless of direction
    shifted_alphabet = alphabet[shift % 26:] + alphabet[:shift % 26]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    return text.translate(translation_table)

def encrypt(text, shift):
    return caesar(text, shift)

def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)

encrypted_text = 'Pbhentr vf sbhaq va hayvxryl cynprf.'
decrypted_text = decrypt(encrypted_text, 13)
print(decrypted_text)
