from Crypto.Cipher import AES
import base64

# the block size for the cipher object, it must be 16 for 128 bit encryption to work
BLOCK_SIZE = 16

# the character used for padding--with a block cipher such as AES, the value
# you encrypt must be a multiple of BLOCK_SIZE in length.  This character is
# used to ensure that your value is always a multiple of BLOCK_SIZE
PADDING = '{'

# the lambda operator or lambda function is used for creating small, one-time and anonymous function objects in Python.
# pads the text to be encrypted
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING

# encrypt with AES, encode with base64
EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))

# creating a key by your own choice and checking to make sure it is 16 characters long
# using an infinite while loop to error check
while True: 
    secret = input("Please Enter An Encryption Key (it must be 16 characters long): ")
    countTotal= (len(secret))
    if countTotal==16:
        cipher = AES.new(secret)
        break
    else:
        print ("Please Ensure The Key You Entered Is 16 Characters In Length")

# entering the string we want to encrypt
data=input("Please Enter Text You'd Like Encrypted: \n")

# encoding and printing the string
encoded = EncodeAES(cipher, data)
print ('Encrypted string:', encoded)
