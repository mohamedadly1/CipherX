def generate_repeated_key(key, text):
      key_without_spaces = key.replace(" ", "")
      repeated_key = ''
      space_index = 0
      for char in text:
          if char != ' ':
              repeated_key += key_without_spaces[space_index % len(key_without_spaces)]
              space_index += 1
          else:
              repeated_key += ' '  
      return repeated_key
def vigenere_cipher(plain_text, key):
    plain_text = plain_text.upper()
    key = key.upper()
    cipher_text = ''
    # repeated_key = (key * (len(plain_text) // len(key))) + key[:(len(plain_text) % len(key))]
    repeated_key=generate_repeated_key(key,plain_text)

    for i in range(len(plain_text)):
        if plain_text[i] == ' ':  
            cipher_text += ' '
        else:
          
            encrypted_char = chr(((ord(plain_text[i]) - 65 + ord(repeated_key[i]) - 65) % 26) + 65)
            cipher_text += encrypted_char

    return cipher_text

def vigenere_decipher(cipher_text, key):
    cipher_text = cipher_text.upper()
    key = key.upper()
    deciphered_text = ''
    repeated_key = generate_repeated_key(key, cipher_text)

    for i in range(len(cipher_text)):
        if cipher_text[i] == ' ':
            deciphered_text += ' '
        else:
            decrypted_char = chr(((ord(cipher_text[i]) - 65 - (ord(repeated_key[i]) - 65)) % 26) + 65)
            deciphered_text += decrypted_char

    return deciphered_text




