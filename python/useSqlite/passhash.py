import hashlib

dk = hashlib.pbkdf2_hmac('sha256', b'r0u7!nG', b'salt', 100000)
print(dk)
print(dk.hex())
