import os
import string
import random

#file paths
fpathDeg1 = "C:\Program Files (x86)\\TextFortress\\ENCRYPT\\Deg1.py"
fpathDeg2 = "C:\Program Files (x86)\\TextFortress\\ENCRYPT\\Deg2.py"
fpathDeg3 = "C:\Program Files (x86)\\TextFortress\\ENCRYPT\\Deg3.py"
fpathKey = "C:\Program Files (x86)\\TextFortress\\common\\Decrypt_keys.txt"

#------------------------------------------#
fpath = [fpathDeg1, fpathDeg2, fpathDeg3]

for path in fpath:
    with open(path) as file:
        code = file.read()
        exec(code)

#temporary file cleanups
os.remove("C:\\Program Files (x86)\\TextFortress\\ENCRYPT\\Deg1Encryption.txt")
os.remove("C:\\Program Files (x86)\\TextFortress\\ENCRYPT\\Deg2BinRepresentation.txt")
#------------------------------------------#

#generate keys
with open(fpathKey, "w") as file:
    for _ in range(8):
        sequence = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
        file.write(sequence + "\n")

print("Keys have been generated and saved to" + fpathKey)