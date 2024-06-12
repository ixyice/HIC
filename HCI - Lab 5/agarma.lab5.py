import os
import string
from collections import Counter
import matplotlib.pyplot as plt


# Setting your code base directory  
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
text = open (BASE_DIR + '/read.txt', encoding='utf-8').read() 
lower_case = text.lower()


#stri: Specifies the list of characters that need to be replaced.
#str2: Specifies the list of characters with which the characters need to be replaced. #str3: Specifies the list of characters that needs to be deleted.
#stri "abc"
#str2= 'gef
# Returns: Returns the translation table which specifies the conversions that can be used by

cleaned_text = lower_case.translate(str.maketrans('','',string.punctuation))

tokenized_words = cleaned_text.split() 

#print(tokenized_words)

stop_words = ["1", "ako", "akin", "aking", "kami", "atin", "atin", "aming sarili", "ikaw", "iyo", "iyo", "iyong sarili", "iyong sarili", "siya ", "siya", "kaniya", "sarili",
"siya", "kaniya", "kanya", "sarili", "ito", "nito", "sarili", "sila", "kanila", "kanila", "kanila", "kanila", "ano ", "alin", "sino", "kanino", "ito", "iyan",
"ito", "mga", "am", "ay", "ay", "noon", "nariyan", "maging", "naging", "nariyan", "mayroon", "mayroon", "nagkaroon ", "pagkakaroon", "gawin", "ginagawa", "gawin", "ginagawa", "a", "an", "ang",
"at", "ngunit", "kung", "o", "dahil", "bilang", "hanggang", "habang", "ng", "sa", "ni", "para sa", "kasama ang ", "tungkol sa", "laban", "sa pagitan", "sa", "sa pamamagitan ng", "sa panahon",
"bago", "pagkatapos", "itaas", "ibaba", "sa", "mula", "pataas", "pababa", "sa", "labas", "sa", "off", "tapos na", "sa ilalim", "muli", "patuloy", "pagkatapos", "minsan", "dito", "doon",
"kailan", "saan", "bakit", "paano", "lahat", "anuman", "pareho", "bawat isa", "kaunti", "higit pa", "karamihan", "iba pa", "ilan ", "ganyan", "hindi", "hindi", "hindi", "lamang", "pag-aari", "kapareho", "kaya", "kaysa",
"masyado", "napaka","s", "t", "maaari", "magagawa", "lang", "don", "dapat", "ngayon"]

final_words = []

for word in tokenized_words:
    if word not in stop_words:
        final_words.append(word)

#NLP Emotion Algorithm
# 1) Check it the word in the final word list is also present in emotion.text 
#       open the emotion file
#       Loop Lhrough each line and clear it
#       Extract the word and emotion using split
# 2) It word is present -> Add the emotion to emotion list
# 3) Finally count each emotion in the cmoliton list

emotion_list = []

with open(BASE_DIR + '/emotions.txt', 'r') as file:
    for line in file:
        clear_line = line.replace('\n','').replace(',','').replace("'",'').strip()
        word, emotion = clear_line.split(':')

        if word in final_words:
            emotion_list.append(emotion)

print (emotion_list)    
w = Counter (emotion_list)
print(w)

# For displaying the graph
fig, ax1 = plt.subplots()
ax1.bar(w.keys(), w.values())
fig.autofmt_xdate()

plt.savefig(BASE_DIR + '\graph.png') 
plt.show()