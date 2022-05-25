# get sentence from user  and get lower case
sentence = input().lower()
# sentence in list
list_sentence  = list(sentence)
sentence_clear = []
# remove "," from sentence
for a in list_sentence:
    if a == ',':
        pass
    else:
        sentence_clear.append(a)

# get list to line
sentence_line = ''.join(sentence_clear)
# separate sentence
sentence_split = sentence_line.split()
# replacement word
for i in sentence_split:
    if i == "черт":
        sentence_split[sentence_split.index("черт")]="####"
sentence_ready =" ".join(sentence_split)


print(sentence_ready)


