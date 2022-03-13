import hashlib
import base64
import os


password = 'password'
salt = base64.b64encode(os.urandom(32))
bytes_pass = bytes(password, 'utf-8')
hash_pass = hashlib.sha256(salt+bytes_pass).hexdigest()
for _ in range(777):
    hash_pass = hashlib.sha256(bytes(hash_pass), 'utf-8').hexdigest()

digest = hashlib.pbkdf2_hmac(
    'sha256', bytes_pass, salt, 777
)
