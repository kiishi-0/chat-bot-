import nltk
from nltk.stem.porter import PorterStemmer
# nltk.download('punkt')
stemmer = PorterStemmer()


def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
    return stemmer.stem(word.lower())

def  bag_of_words(tokenized_sentence):
    pass

a = "Do you take credit cards?"

# print(a)

# a = tokenize(a)

# print(a)


words = ["Organizer", "organizes", "organizing"]
stemmed_words = [stem(w) for w in words]
print(stemmed_words)
