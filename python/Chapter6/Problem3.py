text = input("Enter text: ").lower()

if (text.find(("make a lot of money").lower()) != -1 or
    text.find(("buy now").lower()) != -1 or
    text.find(("click this".lower())) != -1 or
    text.find(("subscribe this".lower())) != -1):
    print("This text is spam")
else:
    print("This text is not spam")