#convert each character to its binary equivalent

filereadpath = "C:\\Program Files (x86)\\TextFortress\\ENCRYPT\\Deg1Encryption.txt"
with open(filereadpath, 'r') as fread:
    encrypted_word = fread.read()

def char_to_binary(char):
    binary_repr = bin(ord(char))[2:].zfill(8)  
    # Convert to binary and ensure it's 8 bits
    return binary_repr

# Convert each character to binary and store the result
binary_word = ''.join(char_to_binary(char) for char in encrypted_word)

fpath = "C:\\Program Files (x86)\\TextFortress\\ENCRYPT\\Deg2BinRepresentation.txt"
with open(fpath, 'w') as fwrite:
    fwrite.write(binary_word)
