from random import *


def generate(g, x, p):
    return pow(g, x) % p


def encrypt(plaintext, key):
    cypher = []
    for char in plaintext:
        cypher.append(ord(char) * key)
    return cypher


def decrypt(cypher, key):
    plain = []
    for value in cypher:
        plain.append(chr(int(value / key)))
    return ''.join(plain)


def is_prime(p):
    v = 0
    for i in range(2, p + 1):
        if p % i == 0:
            v = v + 1
    if v > 1:
        return False
    else:
        return True


def start():
    while True:
        p = int(input("enter the value of p: "))
        if not is_prime(p):
            print("P is supposed to be a prime number!,try again")
        else:
            break
    g = int(input("enter the value of g: "))
    a = randint(0, p)
    b = randint(0, p)
    u = generate(g, a, p)
    v = generate(g, b, p)
    print(f"Alice publishes U = {u}")
    print(f"Bob publishes V = {v}")
    plain_text = input("enter the message :")
    key = generate(v, a, p)
    b_key = generate(u, b, p)
    print(f"alice's shared secret key {key}")
    print(f"Bob's shared secret key {b_key}")

    cypher = encrypt(plain_text, key)
    print(f'encrypted text is: {"".join(map(chr, cypher))}')
    recovered_plain_text = decrypt(cypher, key)
    print(f"Recovered message from sender is: {recovered_plain_text}")


if __name__ == "__main__":
    start()
