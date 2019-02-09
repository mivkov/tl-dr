import nltk, string
import numpy as np
import re, os
from sklearn.feature_extraction.text import TfidfVectorizer

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

def find_uncanny(text1, text2):
    for k in text1:
        if len(k) < 5:
            text1.remove(k)
    for k in text2:
        if len(k) < 5:
            text2.remove(k)
    res = cosine_sim(text1, text2)
    dc = {}
    for (r1, r2) in res:
        dc[r1] = r2
    return dc

def parse(f1):
    f1 = re.sub(r"http\S+", "", f1)
    f1 = re.sub(r"HTTP\S+", "", f1)
    f1 = re.sub(r"[0-9]+", "", f1)
    text1 = list(map(lambda s: s.replace("\n",""), nltk.sent_tokenize(f1)))

    maxima = {t:0.0 for t in text1}
    path = os.getcwd()
    for root, _, files in os.walk(path + '/licenses'):
        for file in files:
            if file.endswith(".txt") and file != 'apple_fixed.txt':
                with open(os.path.join(root,file), 'r') as f:
                    text2 = list(map(lambda s: s.replace("\n",""), nltk.sent_tokenize(f.read())))
                    uncanny = find_uncanny(text1, text2)
                    for key in uncanny:
                        maxima[key] = max(uncanny[key],maxima[key])

    fin = []
    for key in maxima:
        if abs(maxima[key]-1) > 10.0**(-6):
            fin.append((key, maxima[key]))
    fin.sort(key = sort_pattern)
    if len(fin) == 0:
        return "Nothing out of the normal here!"
    else:
        return '\n'.join([f[0] for f in fin][:min(5, len(fin))])

    
