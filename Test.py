import os 

td1 = "S:\\sBackupTarget\\Test_Target"
entries = os.listdir(td1)

# List to hold directory names
directories = [entry for entry in entries if os.path.isdir(os.path.join(td1, entry))]

# Print the number of directories
print(len(directories))

# Print the list of directories
print(directories)