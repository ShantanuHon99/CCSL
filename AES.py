
from Crypto.Cipher import AES

key = b'C&F)H@McQf9TjWnZr'[:16]  
cipher = AES.new(key, AES.MODE_EAX)

data = "Hello There".encode()
nonce = cipher.nonce
ciphertext = cipher.encrypt(data)
print("Cipher text:", ciphertext.hex())
cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
plaintext = cipher.decrypt(ciphertext)
print("Plain text:", plaintext)