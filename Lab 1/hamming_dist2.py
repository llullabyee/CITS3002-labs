### Hamming Dist

def hamming_distance(codeword1, codeword2):
    hamming_dist = 0
    for i in range(len(codeword1)):
        if codeword1[i] != codeword2[i]:
            hamming_dist += 1
        else:
            continue
    return hamming_dist

def checking_codewords(codewords,received_data):
    for i in range(codewords):
        hamming_distance(codewords[i], received_data)
        if hamming_dist > 0:



cw1 = "10011101"
cw2 = "10111110"

print(hamming_distance(cw1, cw2))