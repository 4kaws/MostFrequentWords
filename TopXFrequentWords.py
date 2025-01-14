#!/usr/bin/env python
# coding: utf-8

# In[163]:


'''Write a program to process words in a text file
1.Read in some data.
2.Count the frequency of each word and identify the top 10 most frequent words.
3.Plot the top words.
4.Save the results into a new file.
'''


# In[164]:


import matplotlib.pyplot as plt
import pandas as pd
f = open(r"C:\Users\andre\OneDrive\Documents\microdose_top_articles.txt", 'r', encoding='utf-8')
articles = f.read()


# In[165]:


def getWords(articles):
    """
    It takes "articles" as an argument, which must be a text file.
    
    This function will create a Dictionary out of all the words that are
    in the text file and it will count their frequency.
    
    Also this handles the case sensitivity problem by making all of the
    words in lowercase and then counting them.
    """
    D = {}
    words = articles.split()
    for word in words:
        word = word.lower()
        if word in D:
            D[word] += 1
        else:
            D[word] = 1
    return D


# In[166]:


w_count = getWords(articles)


# In[167]:


def getTopTen(w_count):
    """
    It takes "w_count" as an argument, which must be a Dictionary.
    
    This function will create a dictionary that will take the highest 10
    frequent words and display them in a descending order.
    It iterates through the "getWords()" dictionary and it checks for the maximum value by updating
    the "maxi" parameter.
    
    The return value of this function will be also a Dictionary
    that will contain the expected result.
    """
    
    topNumber = int(input("Enter a number to declare how big your top is going to be: "))
    D = {}
    for _ in range(topNumber):
        maxi = 0
        key = " "
        for x in w_count:
            if w_count[x] > maxi and x not in D:
                maxi = w_count[x]
                key = x
        D[key] = maxi
            
    return D


# In[168]:


myTop = getTopTen(w_count)
displayMytop = pd.Series(myTop)
displayMytop


# In[169]:


def charCounter():
    """
    This function will count how many words are in total in the text file.
    """
    count = 0
    prep_articles = articles.split()
    for i in prep_articles:
        if(len(i) > 0):
            count += 1
    return count


# In[170]:


charactersNumber = charCounter()
print("The number of words in the text file is:", charactersNumber)


# In[177]:


def plotTop(myTop):
    """
    This function will plot:
    - on the x axis the words
    starting from 0 with the most common word and going on in a descending way to inf.
    - on y axis the values that represent how many times a word has been
    occuring in the file.
    """
    plt.bar(range(len(myTop)), list(myTop.values()), align='center')
    plt.xticks(range(len(myTop)), list(myTop.keys()))
    plt.savefig('word_frequency_plot.png')


# In[178]:


plotTop(myTop)


# In[175]:


with open('output.txt', 'w') as file:
    file.write(f"Top most frequent words list:\n")
    file.write(str(pd.Series(myTop)) + '\n')
    file.write(f"The number of words in the text file is: {charactersNumber}\n")

