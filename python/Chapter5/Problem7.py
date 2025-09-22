s={}
names = ['John','Jane','Jack','Doe']
count = 0

while(count<4):
    print("Hello ",names[count])
    lang = input("Enter your fav language: ")
    s[names[count]] = lang
    count+=1

print(s)