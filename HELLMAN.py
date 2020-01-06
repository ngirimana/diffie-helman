from random import *   # importing random from library

# This   funnction to find   g  power x and then modulus  p


def generator(g, x, p):
    return pow(g, x) % p    # returning  answer

# Function  to encrypt message


def encrypt(plaintext, key):
    cypher = []  # array to  hold  encrypted  message
    for char in plaintext:  # loop  to traverse array
        # changing  every character  to corresponding number and  multiply with key and add  to array
        cypher.append(ord(char) * key)
    return cypher  # return encrypted text


# Function  to decrypt message

def decrypt(cypher, key):
    plain = []  # array to  hold  decrypted  message
    for value in cypher:  # loop  to traverse array
        # changing  every character  to corresponding number and  multiply with key and add  to array
        plain.append(chr(int(value / key)))
    return ''.join(plain)  # return decrypted text

# Function  to decrypt message


def is_prime(p):
    v = 0  # initialise v to  zero
    for i in range(2, p + 1):  # loop to  count divisor
        if p % i == 0:  # check  if  p is   divisable  by   i
            v = v + 1  # increament v  by one
    if v > 1:
        return False  # return  false   if  number is  not  prime   number
    else:
        return True  # return  false   if  number is  not  prime   number

# main function


def start():
    p = int(input("enter the value of p: "))  # get  p from  keyboard
    while not is_prime(p):  # check  if p  is prime
        # print  message
        print("P is should be a prime number!!!!!!")
        p = int(input("Enter the value of p: "))  # get  p from  keyboard
    g = int(input("Enter the value of g: "))  # get  g from  keyboard
    a = randint(0, p)  # get random  number  a  less   than  p
    b = randint(0, p)  # get random  number  b  less   than  p
    u = generator(g, a, p)  # compute  alice's  public key
    v = generator(g, b, p)  # compute  bobb's  public key
    print(f"Alice publishes U = {u}")  # print
    print(f"Bob publishes V = {v}")  # print  v
    # input  message  to  be encrypted
    plain_text = input("Enter the message :")
    key = generator(v, a, p)  # alice's shared secret key
    b_key = generator(u, b, p)  # bob's shared secret key
    print(f"Alice's shared secret key {key}")  # print  alice's shared key
    print(f"Bob's shared secret key {b_key}")  # print  bob's shared key

    cypher = encrypt(plain_text, key)  # call encrypt function
    # desplay encrypted  message
    print(f'Encrypted message is: {"".join(map(chr, cypher))}')
    recovered_plain_text = decrypt(cypher, key)  # call decrypt function
    # desplay decrypted  message
    print(f"Recovered message  is: {recovered_plain_text}")


if __name__ == "__main__":
    start()  # call start as main  funnction
