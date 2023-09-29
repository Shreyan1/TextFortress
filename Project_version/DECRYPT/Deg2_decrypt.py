# Define a function to convert a binary string to a character
def binary_to_char(binary_str):
    decimal_value = int(binary_str, 2)
    char = chr(decimal_value)
    return char

# Read the binary data from the file
binary_file_path = "C:\\Users\\HOME\\Documents\\GitHub\\cody-lab\\encryption\\ProjectX\\DECRYPT\\Deg2BinRep.txt"
with open(binary_file_path, 'r') as fread:
    binary_data = fread.read()

# Split the binary data into 8-bit chunks
binary_chunks = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]

# Convert each 8-bit chunk back to its decimal representation and then to characters
decrypted_text = ''.join(binary_to_char(chunk) for chunk in binary_chunks)

# Specify the path to save the decrypted text
decryption_file_path = "C:\\Users\\HOME\\Documents\\GitHub\\cody-lab\\encryption\\ProjectX\\DECRYPT\\Deg2gen_DecryptedWord.txt"

# Write the decrypted text to a file
with open(decryption_file_path, 'w') as fwrite:
    fwrite.write(decrypted_text)
