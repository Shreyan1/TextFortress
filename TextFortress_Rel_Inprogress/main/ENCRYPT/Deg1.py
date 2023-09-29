#Mapping and replacement with cryptographically secure random number generator
import secrets
import os
import sys

def CSRNGpadding1():
    # Generate a random byte string with 64 bits of entropy (8 bytes)
    random_bytes1 = secrets.token_bytes(8)
    return random_bytes1.hex()

#mapping
character_mapping = {}
fpath = "C:\\Program Files (x86)\\TextFortress\\common\\MapChar.txt"
with open(fpath, 'r') as file:
    for line in file:
        line = line.strip()
        if line and not line.startswith('#'):  # Ignore empty lines and comments
            parts = line.split(':')
            if len(parts) == 2:
                source_char, target_char = parts
                if source_char.strip() == '':
                    # Handle space character mapping
                    character_mapping[' '] = target_char
                else:
                    character_mapping[source_char] = target_char

#replacement
def replace_characters(input_str, mapping):
    result = ""
    for char in input_str:
        if char in mapping:
            result += mapping[char]
        else:
            # If the character is not in the mapping, then stays unchanged
            result += char
    return result

def CSRNGpadding2():
    # Generate a random byte string with 64 bits of entropy (8 bytes)
    random_bytes2 = secrets.token_bytes(8)
    return random_bytes2.hex()

# User entry - manual
#file_path = input("Enter a .txt file path: ")
#print("This is your file path: " + file_path + "\n")

# User entry - for UI
# Get the file path from the command line argument
file_path = sys.argv[1]

if not os.path.exists(file_path):
    print("Error: The specified file does not exist.")
    exit()

with open(file_path, 'r') as fread:
    word = fread.read()
transformed_word = replace_characters(word, character_mapping)
fpath1 = "C:\\Program Files (x86)\\TextFortress\\ENCRYPT\\Deg1Encryption.txt"
with open(fpath1, 'w') as fwrite:
    deg1result = fwrite.write(CSRNGpadding1() + transformed_word + CSRNGpadding2())