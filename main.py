# Will Turner 2020

#import Affine
#import Playfair
#import Hill
#import ADFGVX
#import Vignere
import Transposition
#import SubCipher
from Crypto import ADFGVX

if __name__ == "__main__":
    print(Transposition.decode("Wm Coreetr al hylrctepiyoo tb!", 5))
    print(Hill.encode("WHATS UP DUDE", "13 4 1 3"))
    print(Hill.decode("CRYFWPINZIMD", "13 4 1 3"))
