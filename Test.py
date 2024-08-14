import os 

def count_folders(path):
    entries = os.listdir(path)
    folder_count = sum(os.path.isdir(os.path.join(path, entry)) for entry in entries)
    return folder_count

# Example usage
y = f"e:\sBackupTarget\Test_Target"

print("Number of folders:", count_folders(y))
sasas