# Hill Cipher

The Hill cipher is a polygraphic substitution cipher based on linear algebra

## Basic use
To get started import Hill from Crypto.py
> from Crypto import Hill

Create an Hill object with the your plain or ciphertext.

> h = Hill(plain="", cipher="", alpha="ABCDEFGHIKLMNOPQRSTUVWXYZ")

None of these arguments are required.
+ plain: The plaintext to be encoded. Leave blank if you are decoding a message
+ cipher: The ciphertext to be decoded. Leave blank if you are encoding a message
+ key: The string to be turned into the inverse matrix. For a 2x2 matrix [[A, B] [C, D]], pass in "A B C D".
+ keyMatrix: The matrix used to encode the cipher text
+ invMatrix: The matrix used to decode. If this is left blank the inverse matrix will be automatically calculated from keyMatrix
+ alpha: The alphabet to use when encoding. Leave blank for 26 character English alphabet


Once you have set all the variables, call the encode or decode method to see the result
> result = h.encode()

or

> result = h.decode()

___

Note: encode() also stores the enciphered text in the class's cipher variable. It can be retrieved later with

> foo = h.cipher

decode() stores the decoded text in the plain variable. It can be retrieved with
> foo = h.plain

This means it is possible to call encode and decode successively, even if cipher or plain were not set originally.
> result = h.encode() <br>
> original = h.decode()

___
