import os

folder_name = "Multiplication_Tables"

if not os.path.exists(folder_name):
    os.mkdir(folder_name)

for i in range(2, 21):
    filename = os.path.join(folder_name, f"table_{i}.txt")
    with open(filename, "w") as f:
        f.write(f"Multiplication Table of {i}\n")
        f.write("=" * 25 + "\n")
        for j in range(1, 11):
            f.write(f"{i} x {j} = {i * j}\n")
