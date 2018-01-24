"""
Juan Ramirez
CPE 321
Lab 1 - Task 1
"""

import binascii

# A function that XOR's two arbitrary-length bit strings together.
def xor_strings(s, t):
   """
   xor two strings together by first getting their ascii code values
   and then xor'ing them
   """

   # ord returns an integer of the ascii code of a given one char string
   # chr returns a one char string from a given ascii code value
   # hexlify turns the given string into a hex string

   return binascii.hexlify(''.join(chr(ord(a)^ord(b)) for a, b in zip(s, t)))


print("Hex value is: " + xor_strings("Darlin dont you go", "and cut your hair!"))
