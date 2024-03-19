from hw1_digital_signature.rsa import encrypt, decrypt


def sign(message, private_key):
    message_hash = hash(message)
    signature = encrypt(message_hash, private_key)
    return signature


def verify(message, signature, public_key):
    message_hash = hash(message)
    decrypted_hash = decrypt(signature, public_key)
    return message_hash == decrypted_hash
