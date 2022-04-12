import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

class SentenceGet:

    @classmethod
    def get_sentences(cls, txt):
        # nltk.download('punkt')
        
        return sent_tokenize(txt, language='portuguese')