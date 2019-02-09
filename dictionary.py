def print_dict():
    dictionary = {}

    with open('wordfile.txt','r') as f:
        for line in f:
            tup = line.split(' ')
            word = tup[0]
            occ = tup[1]
            dictionary[word] = occ
    return dictionary




