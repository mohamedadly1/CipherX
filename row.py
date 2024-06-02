def encrypt_row_transposition(plain_text, key):
    plain_text = plain_text.replace(" ", "").upper()
    
    key = [int(num) for num in key]
    
    num_columns = len(key)

    num_rows = -(-len(plain_text) // num_columns)  
    
    columns = [''] * num_columns
    

    for i, char in enumerate(plain_text):
        columns[key[i % num_columns] - 1] += char  
    
    cipher_text = ''.join(columns)
    
    return cipher_text

def decrypt_row_transposition(cipher_text, key):
    key_indexes = sorted([index for index in range(len(key)) if key[index] != 0], reverse=True)
    
    rows = list(''.join(['.'*len(cipher_text)]*len(key)))
    
    for col_index, row_char in zip(key_indexes, cipher_text):
        for row_index in key_indexes:
            rows[row_index] = rows[row_index].replace(col_index, row_char, 1)
            
    plain_text = ''.join(rows).replace('.', '')
        
    return plain_text
c='TTNAAPTMTSUOAODWCOIKNLPET'
k='4312567'
x=decrypt_row_transposition(c, k)
print(x)