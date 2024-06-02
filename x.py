def decrypt_row_transposition(cipher_text, key):
    key_indexes = [int(i) for i in key]
    num_cols = len(cipher_text) // len(key)
    num_rows = len(key)
    decrypted_text = ''

    for col in range(num_cols):
        for row in key_indexes:
            index = key_indexes.index(row) * num_cols + col
            decrypted_text += cipher_text[index]

    return decrypted_text

cipher_text = "TTNA APTM TSUO AODW COIx KNLy PETz"
key = "4312567"

plain_text = decrypt_row_transposition(cipher_text.replace(" ", ""), key)
print("Decrypted Text:", plain_text)
