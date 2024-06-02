from flask import Flask, render_template, request
from playfair_cipher import encrypt_playfair, decrypt_playfair
from vigenere_cipher  import vigenere_cipher,vigenere_decipher
from rail_fence_cipher import rail_fence_encrypt,rail_fence_decrypt
app = Flask(__name__)


@app.route('/platfair', methods=['GET', 'POST'])
def platfair():
    ciphertext = ''
    decrypted_text = ''
    
    if request.method == 'POST':
        plaintext = request.form['plaintext']
        key = request.form['key']
        option = request.form['option']

        
        if option=='encrypt':
            ciphertext = encrypt_playfair(plaintext, key)
            return render_template('platfair.html', ciphertext=ciphertext,plaintext=plaintext,key=key, option=option)

        elif option=='decrypt':
            decrypted_text = decrypt_playfair(plaintext, key)
            return render_template('platfair.html', ciphertext=plaintext,decrypted_text=decrypted_text,key=key, option=option)
    
    return render_template('platfair.html')


@app.route('/vigenere', methods=['GET', 'POST'])
def vigenere():
    ciphertext = ''
    decrypted_text = ''
    
    if request.method == 'POST':
        plaintext = request.form['plaintext']
        key = request.form['key']
        option = request.form['option']

        
        if option=='encrypt':
            ciphertext = vigenere_cipher(plaintext, key)
            return render_template('vigenere.html', ciphertext=ciphertext,plaintext=plaintext,key=key, option=option)

        elif option=='decrypt':
            decrypted_text = vigenere_decipher(plaintext, key)
            return render_template('vigenere.html', ciphertext=plaintext,decrypted_text=decrypted_text,key=key, option=option)
    
    return render_template('vigenere.html')



@app.route('/')
def home():
    return render_template('home.html') 

@app.route('/rail_fence', methods=['GET', 'POST'])
def rail_fence():
    ciphertext = ''
    decrypted_text = ''
    
    if request.method == 'POST':
        plaintext = request.form['plaintext']
        key =int( request.form['key'])
        option = request.form['option']

        
        if option=='encrypt':
            ciphertext = rail_fence_encrypt(plaintext, key)
            return render_template('rail_fence.html', ciphertext=ciphertext,plaintext=plaintext,key=key, option=option)

        elif option=='decrypt':
            decrypted_text = rail_fence_decrypt(plaintext, key)
            return render_template('rail_fence.html', ciphertext=plaintext,decrypted_text=decrypted_text,key=key, option=option)
    
    return render_template('rail_fence.html')
if __name__ == '__main__':
    app.run(debug=True)
