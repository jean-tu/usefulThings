# import bcrypt

# passwd = b's$cret12'

# salt = bcrypt.gensalt()
# hashed = bcrypt.hashpw(passwd, salt)

# print(salt)
# print(hashed)

# hashed = bcrypt.hashpw(passwd, salt)

# print(salt)
# print(hashed)

import hashlib
import os

salt = os.urandom(32) # Remember this
password = 'password123'

key = hashlib.pbkdf2_hmac(
    'sha256', # The hash digest algorithm for HMAC
    password.encode('utf-8'), # Convert the password to bytes
    salt, # Provide the salt
    100000 # It is recommended to use at least 100,000 iterations of SHA-256 
)
print(key)