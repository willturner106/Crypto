# Crypto

This is hopefully going to become a well documented crypto library. Right now its just a bunch of python code dumped into a directory. Documentation? Whats that?

## Supported Ciphers
##### Substitution Ciphers
1. Caesar
2. Substitution
3. Vignere
4. Playfair
5. Morse Code
6. Atbash
##### Transposition Ciphers
7. Columnar Transposition
8. Rail Fence
##### Mathematical Ciphers
5. Affine (Modular Arithmetic)
6. Hill (Matrix Multiplication)
##### Combination Ciphers
7. ADFGVX (Substitution + Transposition)

## Use

*Check out the docs for comprehensive guides.*

All ciphers can be imported from Crypto.py. For example:
> from Crypto import Affine

Create an object, passing in your plaintext, ciphertext, key, alphabet, or whatever else you want.
>a = Affine(plain="ENCODETHISPLEASE", a=3, b=11)

Then call .encode() or .decode()
>result = a.encode()
