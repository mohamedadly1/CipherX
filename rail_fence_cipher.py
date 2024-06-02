def rail_fence_encrypt(plain_text, num_rails):
    # Create empty rail matrix
    rails = [[] for _ in range(num_rails)]
    plain_text=plain_text.replace(" ", "").upper()
    # Fill the rail matrix with the letters of the plain text
    rail_index = 0
    direction = 1  # Direction of movement along the rails (down or up)
    for char in plain_text:
        rails[rail_index].append(char)
        rail_index += direction
        if rail_index == num_rails:
            direction = -1  # Change direction to up
            rail_index -= 2
        elif rail_index == -1:
            direction = 1  # Change direction to down
            rail_index = 1

    # Concatenate the letters from each rail to form the ciphertext
    cipher_text = ''.join(''.join(rail) for rail in rails)
    return cipher_text

  
#meet me after  the toga party
def rail_fence_decrypt(cipher_text, key):
    num_chars = len(cipher_text)
    num_rails = key
    cycle_length = 2 * num_rails - 2
    decrypted_text = [''] * num_chars

    # Find positions of spaces in cipher text
    space_positions = [i for i, c in enumerate(cipher_text) if c == ' ']

    # Decrypt the message
    index = 0
    for rail in range(num_rails):
        step_cycle = 2 * (num_rails - rail - 1)
        step_alternate = 2 * rail
        i = rail
        while i < num_chars:
            # Check if current index is a space position
            if index in space_positions:
                index += 1
            if index < num_chars:
                decrypted_text[i] = cipher_text[index]
                index += 1

            if step_cycle != 0 and step_alternate != 0:
                if (step_cycle != cycle_length and step_alternate != cycle_length):
                    i += step_cycle
                    if i < num_chars:
                        if index in space_positions:
                            index += 1
                        if index < num_chars:
                            decrypted_text[i] = cipher_text[index]
                            index += 1
                i += step_alternate
            elif step_cycle != 0:
                i += step_cycle
            elif step_alternate != 0:
                i += step_alternate

    return ''.join(decrypted_text)














# T1=''
# T2=''
# i=0
# for  d in cipher_text:
#     if i<int(len(cipher_text)/2)+1:
#       T1+=d
#     else:
#       T2+=d
#     i+=1
# TEXT1=[]
# TEXT2=[]
# for  T in T1:
#     TEXT1.append(T)
# for  s in T2:
#     TEXT2.append(s)
# TEXT2.append('.')
# cc=''
# x=0
# while (x<12):
#     cc+=TEXT1[x]
#     cc+=TEXT2[x]
#     x+=1
    

# print(cc)
# print()
#MMTHGREEEEAT  

# plain_text = rail_fence_decrypt(cipher_text, num_rails)
# print("Deciphered Text:", plain_text)

# Example usage




