import re


text = "Hello! I am learning Natural Language Processing with Python."


print("Original text:")
print(text)


text = text.lower()

print("\nLowercase:")
print(text)


text = re.sub(r"[^a-zA-Z0-9\s]", "", text)

print("\nAfter removing special characters:")
print(text)


words = text.split()

print("\nWords:")
print(words)


print("\nNumber of words:", len(words))