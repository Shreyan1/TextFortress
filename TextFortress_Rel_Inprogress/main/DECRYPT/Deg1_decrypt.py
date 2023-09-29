#Decrypt Deg1 encryption
import sys

character_mapping_reverse = {}
fpath = "C:\\Program Files (x86)\\TextFortress\\common\\MapChar.txt"
with open(fpath, 'r') as file:
    lines = file.readlines()
    for line in reversed(lines):  # Reverse the lines to get the reverse mapping
        line = line.strip()
        if line and not line.startswith('#'):  # Ignore empty lines and comments
            parts = line.split(':')
            if len(parts) == 2:
                source_char, target_char = parts
                if source_char.strip() == '':
                    # Handle space character mapping
                    character_mapping_reverse[' '] = target_char
                else:
                    character_mapping_reverse[source_char] = target_char

# Reverse character replacement
def reverse_replace_characters(input_str, mapping):
    result = ""
    for char in input_str:
        reversed_mapping = {v: k for k, v in mapping.items()}  # Reverse the mapping
        if char in reversed_mapping:
            result += reversed_mapping[char]
        else:
            # If the character is not in the mapping, then stays unchanged
            result += char
    return result

# Read the encrypted data from the file
readpath = "C:\\Program Files (x86)\\TextFortress\\DECRYPT\\Deg2gen_DecryptedWord.txt"
with open(readpath, 'r') as fread:
    encrypted_data = fread.read()

# Remove the padding
start_index = 16  # Length of the CSRNG padding (8 bytes each, hex-encoded)
end_index = -16   # Negative index to remove the last 16 characters
encrypted_word = encrypted_data[start_index:end_index]

# Reverse the character replacement
decrypted_word = reverse_replace_characters(encrypted_word, character_mapping_reverse)

# Write the decrypted word to a file
writepath = sys.argv[2]
with open(writepath, 'w') as fwrite:
    fwrite.write(decrypted_word)