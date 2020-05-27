# Atbash Cipher

Atbash is a monoalphabetic substitution cipher originally used to encrypt the Hebrew alphabet.

## Basic use
To get started import Atbash from Crypto.py
> from Crypto import Atbash

Atbash can be used either statically, or as an instance. To statically encode Atbash, use Atbash.atbash_encode

> result = Atbash.atbash_encode(plaintext, alpha)

> result = Atbash.atbash_decode(ciphertext, alpha)

If you wish to use a different alphabet, pass it to the alpha argument. Leave blank for 26 character English alphabet
<br>

The other way to encode with Atbash is with an instance.
Create an Atbash object with the your plain or ciphertext.

> m = Atbash(plain="", cipher="", alpha="ABCDEFGHIKLMNOPQRSTUVWXYZ")

None of these arguments are required.
+ plain: The plaintext to be encoded. Leave blank if you are decoding a message
+ cipher: The ciphertext to be decoded. Leave blank if you are encoding a message
+ alpha: The alphabet to use when encoding. Leave blank for 26 character English alphabet


Once you have set all the variables, call the encode or decode method to see the result
> result = a.encode()

or

> result = a.decode()

___

Note: encode() also stores the enciphered text in the class's cipher variable. It can be retrieved later with

> foo = a.cipher

decode() stores the decoded text in the plain variable. It can be retrieved with
> foo = a.plain

This means it is possible to call encode and decode successively, even if cipher or plain were not set originally.
> result = a.encode() <br>
> original = a.decode()

___
