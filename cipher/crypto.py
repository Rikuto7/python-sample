# pip install pycryptodome
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


key = get_random_bytes(16)
iv = get_random_bytes(16)
text = 'cnoanciabdeaiydiucanciarnva'

cipher = AES.new(key, AES.MODE_CBC, iv)
padding_length = AES.block_size - (len(text) % AES.block_size)
text += chr(padding_length) * padding_length

cipher_text = cipher.encrypt(text)

decrypted_text = cipher.decrypt(cipher_text)
text = decrypted_text[:-decrypted_text[-1]]
