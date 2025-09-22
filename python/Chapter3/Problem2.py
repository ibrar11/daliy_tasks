import datetime

Name = input("Enter your name: ")
Date = datetime.date.today()
letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''
letter = letter.replace("<|Name|>", Name).replace("<|Date|>", str(Date))

print(letter)