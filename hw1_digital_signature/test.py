from hw1_digital_signature import rsa, digital_signature


def test_rsa_crypt_decrypt():
    message = 2281337
    public_key, private_key = rsa.generate_key_pair()
    encrypted_message = rsa.encrypt(message, public_key)
    decrypted_message = rsa.decrypt(encrypted_message, private_key)
    assert decrypted_message == message


def test_digital_signature():
    message = 123456789

    public_key, private_key = rsa.generate_key_pair()
    signature = digital_signature.sign(message, private_key)
    assert digital_signature.verify(message, signature, public_key)
