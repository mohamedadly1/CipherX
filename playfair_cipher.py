def create_playfair_table(key):
    key = "".join(dict.fromkeys(key))
    key = key.replace(" ", "")
    table = ""
    for char in key:
        if char not in table:
            table += char
    for char in range(ord('A'), ord('Z')+1):
        if chr(char) != 'J' and chr(char) not in table:
            table += chr(char)
    table = [table[i:i+5] for i in range(0, 25, 5)]
    return table

def find_char_position(table, char):
    for i, row in enumerate(table):
        for j, value in enumerate(row):
            if value == char:
                return i, j
    return -1, -1

def encrypt_playfair(plaintext, key):
    table = create_playfair_table(key.upper())
    plaintext = plaintext.replace(" ", "").upper()
    plaintext_pairs = []
    i = 0
    while i < len(plaintext):
        if i == len(plaintext) - 1:
            plaintext_pairs.append(plaintext[i] + 'X')
            i += 1
        elif plaintext[i] == plaintext[i+1]:
            plaintext_pairs.append(plaintext[i] + 'X')
            i += 1
        else:
            plaintext_pairs.append(plaintext[i] + plaintext[i+1])
            i += 2
    ciphertext = ""
    for pair in plaintext_pairs:
        char1, char2 = pair[0], pair[1]
        row1, col1 = find_char_position(table, char1)
        row2, col2 = find_char_position(table, char2)
        if row1 == row2:
            ciphertext += table[row1][(col1 + 1) % 5] + table[row2][(col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += table[(row1 + 1) % 5][col1] + table[(row2 + 1) % 5][col2]
        else:
            ciphertext += table[row1][col2] + table[row2][col1]
    return ciphertext
def decrypt_playfair(ciphertext, key):
    table = create_playfair_table(key.upper())
    ciphertext = ciphertext.replace(" ", "").upper()
    decrypted_text = ""
    i = 0
    while i < len(ciphertext):
        char1, char2 = ciphertext[i], ciphertext[i+1]
        row1, col1 = find_char_position(table, char1)
        row2, col2 = find_char_position(table, char2)
        if row1 == row2:
            decrypted_text += table[row1][(col1 - 1) % 5] + table[row2][(col2 - 1) % 5]
        elif col1 == col2:
            decrypted_text += table[(row1 - 1) % 5][col1] + table[(row2 - 1) % 5][col2]
        else:
            decrypted_text += table[row1][col2] + table[row2][col1]
        i += 2
    # Handle the case where 'X' is between two identical letters
    decrypted_text = decrypted_text.replace('XZ', '')
    decrypted_text = decrypted_text.replace('ZX', '')
    return decrypted_text

# print(decrypt_playfair("PIRUSPZTSMCZ",'python'))



