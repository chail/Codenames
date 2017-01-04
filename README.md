# Codenames
A quick script to help with solving the codenames game.

## How it works
The goal of the codenames game is to guess some number of words that the other player is thinking of by a single-word cue. I thought that using the word2vec algorithm might be a simple approach to help solve this game. Using a word2vec model, similar words in meaning tend to be closer in n-dimensional space in their word embedding format. This script uses the word2vec algorithm to find words in meaning similar to the provided cue word.

## Installation
1. Install [gensim][gensim].
2. I used a prebuilt word2vec model on English Wikipedia. You can get a prebuilt model [here][model].

## Usage
Run the script with `python most_similar_words.py word1 word2 ...`, where the command line words are the input vocabulary.
It will loop prompting for the input cue word and print the words from the input vocabulary most similar to the cue word.

[gensim]:https://radimrehurek.com/gensim/install.html
[model]:https://github.com/idio/wiki2vec/
