import spacy
import re

class DataAnalysis:

    nlp = spacy.load('pt_core_news_sm')    

    @classmethod
    def noun_counter(cls, text):
        '''returns the amount of nouns found'''
        counter = 0
        doc = cls.nlp(text)
        for token in doc:
            if token.pos_ == 'NOUN':
                counter += 1
        return counter
    
    @classmethod
    def verb_counter(cls, text):
        '''returns the amount of verbs found'''
        counter = 0
        doc = cls.nlp(text)
        for token in doc:
            if token.pos_ == 'VERB':
                counter += 1
        return counter

    @classmethod
    def adjective_counter(cls, text):
        '''returns the amount of adjectives found'''
        counter = 0
        doc = cls.nlp(text)
        for token in doc:
            if token.pos_ == 'ADJ':
                counter += 1
        return counter

    @classmethod
    def average_word_length(cls, text):
        '''returns the average word length'''
        word_list = text.split()
        total_characters = 0
        for word in word_list:
            total_characters += len(word)
        return total_characters / len(word_list)

    @classmethod
    def character_counter(cls, text):
        '''returns the amount of characters in a text (minus whitespaces)'''
        text = re.sub("\s*", '', text)
        return len(text)

    @classmethod
    def unique_words_counter(cls, text):
        '''returns the amount of unique words in a text'''
        unique_words = []
        words = text.split()
        for word in words:
            if word not in unique_words:
                unique_words.append(word)
        return len(unique_words)

    @classmethod
    def word_frequency(cls, text):
        '''returns a sorted (descending) dictionary, where the keys are the words and the values
        the frequency of such words in the text'''
        # creating a dictionary with the frequency of the words
        frequency = {}
        words = text.split()
        for word in words:
            if word in frequency.keys():
                frequency[word] += 1
            else:
                frequency[word] = 1

        sorted_values = sorted(frequency.values(), reverse=True)
        sorted_frequency = {}
        for value in sorted_values:
            for key in frequency.keys():
                if frequency[key] == value:
                    sorted_frequency[key] = frequency[key]

        return sorted_frequency