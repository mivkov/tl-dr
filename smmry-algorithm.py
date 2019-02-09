import re
import requests
from dictionary import print_dict

# assuming I have a dictionary of words and their absolute frequencies
frequencies = print_dict()
maxFrequency = max(frequencies.values())

# pretty arbitrary
cat0 = 0.01*maxFrequency
cat1 = 0.001*maxFrequency
cat2 = 0.00001*maxFrequency
cat3 = 0.000005*maxFrequency
cat4 = 0.000003*maxFrequency
cat5 = 0.000001*maxFrequency
cat6 = 0.0000005*maxFrequency
cat7 = 0.0000002*maxFrequency
cat8 = 0.0000001*maxFrequency
cat9 = 0
categories = {cat0: 0, cat1: 1, cat2: 2, cat3: 3, cat4: 4, cat5: 5, 
    cat6: 6, cat7: 7, cat8: 8, cat9: 9}

pointValues = dict()
for key in frequencies:
    pointValues[key] = categories[max(k for k in categories.keys() if frequencies[key] >= k)]


# haven't ignored forms of address as detailed; shouldn't be a problem in 
# EULAs but should figure out
# currently requires minimum sentence length 3 non-punctuation chars; likely 
# sufficient for EULA; elsewhere will remove abbreviated English honorifics
regexp = re.compile(r'[A-Za-z,;\-\'"\s\d]{3,}[.?!]', re.MULTILINE | re.DOTALL)

"""Given an input text, returns the 
"""
def summarize(input_text):
    text = input_text
    sentences = re.findall(regexp, text)

    # need to maintain the chronological order here
    # kinda ok to be a little inefficient?? Using py anyway
    sentenceValues = []
    for s in sentences:
        words = re.findall(r'[A-Za-z\']+', s)
        sValue = 0
        for w in words:
            # determine single word's point value
            if w in pointValues:
                sValue = sValue + pointValues[w]
        sentenceValues.append(sValue)
    maxIndices = sorted(range(len(sentenceValues)), key=lambda i: sentenceValues[i])[-min(int(len(sentences)/20 + 1), 5):]

    smmry = []
    for i in range(len(maxIndices)):
        smmry.append(sentences[maxIndices[i]])

    return smmry

# random text test data; sentences are inordinately long
# linkf = "https://www.cs.cmu.edu/~spok/grimmtmp/001.txt"
# f = requests.get(linkf)
# linkh = "https://www.cs.cmu.edu/~spok/grimmtmp/002.txt"
# h = requests.get(linkh)
# linkh = "https://www.cs.cmu.edu/~spok/grimmtmp/003.txt"
# k = requests.get(linkk)

linkg = "https://www.google.com/chrome/privacy/eula_text.html"
g = requests.get(linkg)

print(summarize(g.text))