from flask import Flask, request, jsonify
from cipher.caesar.caesar_cipher import CaesarCipher

app = Flask(__name__)  

caesar_cipher = CaesarCipher()

@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    data = request.json
    plain_text = data.get('plain_text', '')  
    key = int(data.get('key', 0)) 
    encrypt_text = caesar_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_message': encrypt_text})

@app.route("/api/caesar/decrypt", methods=["POST"])  
def caesar_decrypt():
    data = request.json
    cipher_text = data.get('cipher_text', '')  
    key = int(data.get('key', 0))
    decrypt_text = caesar_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_message': decrypt_text})

if __name__ == "__main__": 
    app.run(host="0.0.0.0", port=5000, debug=True)  
