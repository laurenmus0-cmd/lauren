with open("chrome.txt", "w") as x:
    x.write("Hi, this a some text")

#read
with open("chrome.txt", "r") as file:
    content=file.read()
    print(content)