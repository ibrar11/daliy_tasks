dic = {
    "Aam": "Mango",
    "Saeb": "Apple",
    "Kela": "Banana",
    "Tarbuj": "Watermelon"
}

key = input("Enter the fruit name in Urder: ")
print("The fruit in English is:", dic.get(key, "Not found in dictionary"))