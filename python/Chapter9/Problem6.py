with open("log.txt", "r") as f:
    log_content = f.read().lower()

if "python" in log_content:
    print("The log file contains 'python'.")
else:
    print("The log file does not contain 'python'.")
