# Morse Code

Morse code is a method used in telecommunication to encode text characters as standardized sequences of two different signal durations, called dots and dashes.

## Basic use
To get started import Morse from Crypto.py
> from Crypto import Morse

Morse can be used either statically, or as an instance. To statically encode Morse code, use Morse.morse_encode

> result = Morse.morse_encode(plaintext)


> result = Morse.morse_decode(ciphertext)


The other way to encode morse code is with an instance. This allows you to edit the dictionary used when encoding
Create an Morse object with the your plain or ciphertext.

> m = Morse(plain="", cipher="")

Neither of these arguments are required.
+ plain: The plaintext to be encoded. Leave blank if you are decoding a message
+ cipher: The ciphertext to be decoded. Leave blank if you are encoding a message


Once you have set all the variables, call the encode or decode method to see the result
> result = m.encode()

or

> result = m.decode()

If you are using a custom Morse code system, you can change the dictionary used to encode/decode.

> m.dict["A"] = "."

___

Note: encode() also stores the enciphered text in the class's cipher variable. It can be retrieved later with

> foo = m.cipher

decode() stores the decoded text in the plain variable. It can be retrieved with
> foo = m.plain

This means it is possible to call encode and decode successively, even if cipher or plain were not set originally.
> result = m.encode() <br>
> original = m.decode()

___
