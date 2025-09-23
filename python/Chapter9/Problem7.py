# Open the log file
with open("log.txt", "r") as f:
    line_number = 1
    found = False
    
    while True:
        line = f.readline()
        if not line:
            break
        if "python" in line.lower():
            print(f"'python' found on line {line_number}: {line.strip()}")
            found = True
        line_number += 1

if not found:
    print("No occurrence of 'python' found in the file.")
