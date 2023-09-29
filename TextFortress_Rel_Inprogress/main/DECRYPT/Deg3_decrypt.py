#Decrypt Deg3 encryption
import os
import sys

def shift_and_invert(binary_str, rightshift_amount):
    # Right Circular shift the binary string by rightshift_amount
    n = len(binary_str)
    shifted_str = binary_str[-rightshift_amount:] + binary_str[:-rightshift_amount]

    # Invert the shifted binary string
    inverted_str = ''.join(['1' if bit == '0' else '0' for bit in shifted_str])
    return inverted_str


# Right circular shift amount (should match the left shift amount used during encryption)
rightshift_amount = 2

# Input file path for the encrypted data
input_fpath = sys.argv[1]
print("The input fpath is : "+input_fpath)
if not os.path.exists(input_fpath):
    print("Error: The specified file does not exist.")
    exit()

# Read the encrypted data from the input file
with open(input_fpath, 'r') as encrypted_file:
    encrypted_data = encrypted_file.read()

decrypted_result = shift_and_invert(encrypted_data, rightshift_amount)

decrypted_output_fpath = "C:\\Program Files (x86)\\TextFortress\\DECRYPT\\Deg2BinRep.txt"
with open(decrypted_output_fpath, 'w') as decrypted_output_file:
    decrypted_output_file.write(decrypted_result)
