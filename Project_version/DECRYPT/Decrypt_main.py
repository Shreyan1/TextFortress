import subprocess
import os

# Check if the specified file exists

fpathDeg1 = "C:\\Users\\HOME\\Documents\\GitHub\\cody-lab\\encryption\\ProjectX\\DECRYPT\\Deg1_decrypt.py"
fpathDeg2 = "C:\\Users\\HOME\\Documents\\GitHub\\cody-lab\\encryption\\ProjectX\\DECRYPT\\Deg2_decrypt.py"
fpathDeg3 = "C:\\Users\\HOME\\Documents\\GitHub\\cody-lab\\encryption\\ProjectX\\DECRYPT\\Deg3_decrypt.py"

fpath = [fpathDeg3, fpathDeg2, fpathDeg1]

for path in fpath:
    print("Executing - "+path)
    with open(path) as file:
        code = file.read()
        exec(code)

print("Your file is now decrypted")

#temporary file cleanups
os.remove("C:\\Users\\HOME\\Documents\\GitHub\\cody-lab\\encryption\\ProjectX\\DECRYPT\\Deg2BinRep.txt")
os.remove("C:\\Users\\HOME\\Documents\\GitHub\\cody-lab\\encryption\\ProjectX\\DECRYPT\\Deg2gen_DecryptedWord.txt")
