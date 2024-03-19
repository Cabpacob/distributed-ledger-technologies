from hw1_digital_signature.utils import generate_prime_number, generate_coprime_number, extended_gcd


class PublicKey:
    def __init__(self, public_key, modulo):
        self.key = public_key
        self.mod = modulo


class PrivateKey:
    def __init__(self, private_key, modulo):
        self.key = private_key
        self.mod = modulo


def generate_key_pair():
    p = generate_prime_number()
    q = generate_prime_number()

    while p == q:
        p = generate_prime_number()

    n = p * q
    phi = (p - 1) * (q - 1)
    private_key = generate_coprime_number(phi)
    _, x, _ = extended_gcd(private_key, phi)
    public_key = ((x % phi) + phi) % phi
    return PublicKey(public_key, n), PrivateKey(private_key, n)


def encrypt(message, public_key):
    return pow(message, public_key.key, public_key.mod)


def decrypt(ciphertext, private_key):
    return pow(ciphertext, private_key.key, private_key.mod)
