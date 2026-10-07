import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

nltk.download("punkt")


text = "Python is easy to learn. NLP is used to work with human language."


sentences = sent_tokenize(text)

print("Sentences:")
print(sentences)


words = word_tokenize(text)

print("\nWords:")
print(words)


print("\nNumber of sentences:", len(sentences))
print("Number of words:", len(words))