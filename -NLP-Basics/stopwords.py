import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download("punkt")
nltk.download("stopwords")


text = "Python is a popular programming language and it is easy to learn."

words = word_tokenize(text.lower())

stop_words = set(stopwords.words("english"))

filtered_words = []

for word in words:
    if word.isalpha() and word not in stop_words:
        filtered_words.append(word)


print("Original words:")
print(words)

print("\nAfter removing stopwords:")
print(filtered_words)