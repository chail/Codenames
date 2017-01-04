from gensim.models import Word2Vec
import sys

def get_similarity(word, word_list, model):
    similarity = {}
    for w in word_list:
        s = model.similarity(word, w)
        similarity[w] = s
    return similarity

def most_similar(similarity):
    sorted_words = sorted(similarity, key=similarity.get, reverse=True)
    for s in sorted_words:
        print(s + ": " + str(similarity[s]))

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Input words to compare similarity")
        quit()

    word_list = sys.argv[1:]
    # make sure en.model is in current directory
    model = Word2Vec.load("en.model")

    while (True):
        print("-------------------------------------")
        word = raw_input('Enter a word or q to quit: ')
        if (word == 'q'):
            break
        print("Most Similar Words:")
        similar_words = get_similarity(word, word_list, model)
        most_similar(similar_words)





