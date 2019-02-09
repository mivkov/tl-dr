import nltk, string
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

# nltk.download('punkt') # if necessary...

stemmer = nltk.stem.porter.PorterStemmer()
remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)

def stem_tokens(tokens):
    return [stemmer.stem(item) for item in tokens]

'''remove punctuation, lowercase, stem'''
def normalize(text):
    return stem_tokens(nltk.word_tokenize(text.lower().translate(remove_punctuation_map)))

vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words='english')

def cosine_sim(text1, text2):
    lent1 = len(text1) 
    text = text1 + text2
    tfidf = vectorizer.fit_transform(text)
    vec =  ((tfidf * tfidf.T).A)
    cng = np.delete(np.delete(vec, np.s_[0:lent1], axis=1), np.s_[lent1:len(text)], axis=0)
    return [(text1[i],np.amax(cng[i])) for i in range(len(cng))]

def sort_pattern(x):
    return x[1]

def find_uncanny(f1, f2):
    text1 = list(map(lambda s: s.replace("\n",""), nltk.sent_tokenize(f1)))
    text2 = list(map(lambda s: s.replace("\n",""), nltk.sent_tokenize(f2)))
    for k in text1:
        if len(k) < 5:
            text1.remove(k)
    for k in text2:
        if len(k) < 5:
            text2.remove(k)
    res = cosine_sim(text1, text2)
    rest = []
    for r in res:
        if abs(r[1]-1) > 10.0**(-6):
            rest.append(r)
    rest.sort(key = sort_pattern)
    return [r[0] for r in rest][:min(5, len(rest))]

def parse(f1, f2):
    uncanny = find_uncanny(f1, f2)
    if len(uncanny) == 0:
        return "Nothing out of the normal here!"
    else:
        return '\n'.join(uncanny)

with open('apple_fixed.txt','r') as f1:
    with open('apple.txt','r') as f2:
        print(parse(f1.read(), f2.read()))

    
