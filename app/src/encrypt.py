from passlib.hash import bcrypt

def encrypt_password(password_plain):
    password_hash = bcrypt.hash(password_plain)
    return password_hash

def verify_password(password_hash):
    verified = bcrypt.verify(password_hash)
    return verified
