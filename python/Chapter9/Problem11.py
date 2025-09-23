import os

old_name = "this.txt"
new_name = "renamed_by_python.txt"

os.rename(old_name, new_name)

print(f"File renamed from '{old_name}' to '{new_name}'")
