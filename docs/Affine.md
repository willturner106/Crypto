# Affine Cipher

The affine cipher is a monoalphabetic substitution cipher that encrypts letters using the formula y = (ax + b) mod 26.

## Basic use
To get started import the Affine cipher from Crypto.py
> from Crypto import Affine


Create an Affine object with the your plain or ciphertext, the a and b variables, and the alphabet you want to use

> a = Affine(plain="", cipher="", a=1, b=1, alpha="ABC")

None of these arguments are required.
+ plain: The plaintext to be encoded. Leave blank if you are decoding a message
+ cipher: The ciphertext to be decoded. Leave blank if you are encoding a message
+ a: The multiplier to be used for encoding. Must be co-prime with the length of the alphabet
+ b: The number to be added when encoding.
+ alpha: The alphabet to be used. Leave blank for 26 character english alphabet.
<br>


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


## Cracking the Affine Cipher

Cracking the Affine cipher is relatively easy. The nature of modular arithmetic means that there are a very limited number of possible a and b values. For the 26 character english alphabet, there are 12 possible a values and 25 possible b values, for 300 total combinations. It is very easy for a computer to try them all.
<br><br>
To get started, import the Affine Decoder from CrackingTools.py
> from CrackingTools import AffineDecoder

The AffineDecoder class extends Affine. Create a new AffineDecoder and pass in your ciphertext.
> a = AffineDecoder(ciphertext="DECRYPTTHISPLEASE", alpha="ABC")
* ciphertext: The text you want to decode
* alpha: The alphabet to be used. Leave blank for 26 character english alphabet

Once again, the alpha argument is optional. The default is the 26 character english alphabet.


The last step is to call the spam method. Spam returns a list of possible results. It uses a primitive english language detector to determine which results are likely to be correct.

> a.spam(tolerance=4)

The tolerance argument determines how sensitive the english detector is. A lower tolerance means a longer list of possible plaintexts will be returned. The default is 3. It is recommended that you start with 3, and then gradually decrease the tolerance until the answer is found.
