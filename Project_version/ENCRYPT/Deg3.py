# Invert bin and shift function
import sys

def invert_and_shift(binary_str, leftshift_amount):
    # Invert the binary string
    inverted_str = ''.join(['1' if bit == '0' else '0' for bit in binary_str])

    # Left Circular shift the inverted string by leftshift_amount
    shifted_str = inverted_str[leftshift_amount:] + inverted_str[:leftshift_amount]

    return shifted_str

# Input File path
file_path = "C:\\Users\\HOME\\Documents\\GitHub\\cody-lab\\encryption\\ProjectX\\ENCRYPT\\Deg2BinRepresentation.txt"

# Read the binary number from the file
with open(file_path, 'r') as file:
    binary_number = file.read().strip()

leftshift_amount = 2

result = invert_and_shift(binary_number, leftshift_amount)

# Prompt the user for the desired file name and location
save_file_path=sys.argv[2]
print("Save file path = " + save_file_path)

# Output file path
# output_fpath = "C:\\Users\\HOME\\Documents\\GitHub\\cody-lab\\encryption\\ProjectX\\ENCRYPT\\Encrypted.txt"
with open(save_file_path, 'w') as output_file:
    output_file.write(result)
