"""
Empty Compose Template to implement :D
Github: https://www.github.com/kying18
"""
# Step1 : Get words from text
# Step2 : Make graph using those words
# Step3 : Get next word for X number of words
# Step4 : Show those words to user

import os
import re
import string
import random

from GC_graph import Graph, Vertex

def get_words_from_text(text_path): # import text file, do simple word processing to make text ready for graph
    with open(text_path, 'r') as f:
        text = f.read()

        text = ' '.join(text.split()) # separate words from text, and rejoin them with only single spaces between them
        text = text.lower() # make everything lowertext
        text = text.translate(str.maketrans('','', string.punctuation)) # remove all punctuation marks

    words = text.split() # Finally, again split the above text into words
    return words

def make_graph(words):
    g = Graph()
    previous_word = None

    for word in words: # for each word
        word_vertex = g.get_vertex(word)

        if previous_word: # if there was a previous word & if edge already exists, increment weight
            previous_word.increment_edge(word_vertex)

        previous_word = word_vertex # set word to previous word and continue iterating

    g.generate_probability_mappings() # generate probability mapping before returning the Graph object
    return g

def compose(g, words, length=50):
    composition = []
    word = g.get_vertex(random.choice(words))
    for _ in range(length):
        composition.append(word.value)
        word = g.get_next_word(word)

    return composition

def main():
    words = get_words_from_text('C:/Users/LAMDA/PycharmProjects/Python_baby_steps/graph-composer-master/texts/hp_sorcerer_stone.txt') # get's text

    g = make_graph(words) # creates graph from text

    composition = compose(g, words, 100) # generates text using the graph
    print(' '.join(composition))


if __name__ == '__main__':
    main()