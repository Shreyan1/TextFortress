import os
import string
import random

#file paths
fpathDeg1 = "C:\\Users\\HOME\\Documents\\GitHub\\cody-lab\\encryption\\ProjectX\\ENCRYPT\\Deg1.py"
fpathDeg2 = "C:\\Users\\HOME\\Documents\\GitHub\\cody-lab\\encryption\\ProjectX\\ENCRYPT\\Deg2.py"
fpathDeg3 = "C:\\Users\\HOME\\Documents\\GitHub\\cody-lab\\encryption\\ProjectX\\ENCRYPT\\Deg3.py"
fpathKey = "C:\\Users\\HOME\\Documents\\GitHub\\cody-lab\\encryption\\ProjectX\\common\\Decrypt_keys.txt"

#------------------------------------------#
fpath = [fpathDeg1, fpathDeg2, fpathDeg3]

for path in fpath:
    with open(path) as file:
        code = file.read()
        exec(code)

#temporary file cleanups
os.remove("C:\\Users\\HOME\\Documents\\GitHub\\cody-lab\\encryption\\ProjectX\\ENCRYPT\\Deg1Encryption.txt")
os.remove("C:\\Users\\HOME\\Documents\\GitHub\\cody-lab\\encryption\\ProjectX\\ENCRYPT\\Deg2BinRepresentation.txt")
#------------------------------------------#

#generate keys
with open(fpathKey, "w") as file:
    for _ in range(8):
        sequence = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
        file.write(sequence + "\n")

print("Keys have been generated and saved to" + fpathKey)