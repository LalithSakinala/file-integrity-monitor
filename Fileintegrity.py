import hashlib

filename = input("Enter file name to monitor: ")

with open(filename,"rb") as f:
    data = f.read()

hash1 = hashlib.sha256(data).hexdigest()

print("Original Hash:",hash1)

input("Modify file and press enter")

with open(filename,"rb") as f:
    data = f.read()

hash2 = hashlib.sha256(data).hexdigest()

print("New Hash:",hash2)

if hash1 != hash2:
    print("File was modified!")
else:
    print("No change detected")
