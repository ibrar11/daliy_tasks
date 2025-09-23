def are_files_identical(file1, file2):
    with open(file1, "r") as f1, open(file2, "r") as f2:
        content1 = f1.read()
        content2 = f2.read()
        return content1 == content2

file1 = "this.txt"
file2 = "copy.txt"

if are_files_identical(file1, file2):
    print("The files are identical.")
else:
    print("The files are different.")
