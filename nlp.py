import streamlit as st
import pandas as pd
#open text file :
text_file = open("Text.txt")
#read the data :
text = text_file.read()
#type_text = type(text)
#st.write(type_text)
st.write(len(text))
st.write(text)

import nltk
nltk.download('punkt')
from nltk import sent_tokenize
from nltk import word_tokenize

#Tokenize the text by sentences :
sentences = sent_tokenize(text)
#how many sentences are there ? :
st.write(len(sentences))
#print sentences :
st.write(sentences)

#Tokenize the text with words :
words = word_tokenize(text)

#How many words are there ? :
st.write(len(words))

#print words :

st.write(words)


from nltk.probability import FreqDist

#find the frequency :
fdist = FreqDist(words)

#print 10 most common words :
st.write(fdist.most_common(10))

#Plot the graph for fdist :
import matplotlib.pyplot as plt

st.line_chart(fdist.most_common(10))

#Empty list to store words:
words_no_punc = []

#removing punctuation marks:
for w in words:
    if w.isalpha():
        words_no_punc.append(w.lower())

#print the words without punctution marks :
st.write(words_no_punc)
st.write("\n")

#lenght
st.write(len(words_no_punc))

#frequency distribution :
fdist = FreqDist(words_no_punc)

st.write(fdist.most_common(10))

#plot the most common words :
st.line_chart(fdist.most_common(10))

from nltk.corpus import stopwords

#list of stopwords :
nltk.download('stopwords')
stopwords = stopwords.words('english')
st.write(stopwords)

# Empty list to store clean words:
clean_words = []

for w in words_no_punc:
    if w not in stopwords:
        clean_words.append(w)
        
st.write(clean_words)
st.write("\n")
st.write(len(clean_words))

#frequency distribution :
fdist = FreqDist(clean_words)

st.write(fdist.most_common(10))

#plot the most common words :
st.line_chart(fdist.most_common(10))
            
            #Library to from wordcloud :
from wordcloud import WordCloud
            
            #library to plot the wordcloud :
import matplotlib.pyplot as plt
            
wordcloud = WordCloud(width=800, height=800, background_color="white").generate(text)
st.image(wordcloud.to_image(), caption="Word Cloud")
