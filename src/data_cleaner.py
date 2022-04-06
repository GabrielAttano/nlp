import re
import string
import unidecode
import spacy

class DataCleaner:
    '''Class used for treating a string before using it'''

    # Stopwords were taken from NLTK
    stopwords = ['de', 'a', 'o', 'que', 'e', 'do', 'da', 'em', 'um', 'para', 'e', 
    'com', 'nao', 'uma', 'os', 'no', 'se', 'na', 'por', 'mais', 'as', 'dos', 
    'como', 'mas', 'foi', 'ao', 'ele', 'das', 'tem', 'seu', 'sua', 'ou', 
    'ser', 'quando', 'muito', 'ha', 'nos', 'ja', 'esta', 'eu', 'tambem', 'so', 
    'pelo', 'pela', 'ate', 'isso', 'ela', 'entre', 'era', 'depois', 'sem', 'mesmo', 
    'aos', 'ter', 'seus', 'quem', 'nas', 'me', 'esse', 'eles', 'estao', 'voce', 
    'tinha', 'foram', 'essa', 'num', 'nem', 'suas', 'meu', 'as', 'minha', 'tem', 
    'numa', 'pelos', 'elas', 'havia', 'seja', 'qual', 'sera', 'nos', 'tenho', 'lhe', 
    'deles', 'essas', 'esses', 'pelas', 'este', 'fosse', 'dele', 'tu', 'te', 'voces', 
    'vos', 'lhes', 'meus', 'minhas', 'teu', 'tua', 'teus', 'tuas', 'nosso', 'nossa', 
    'nossos', 'nossas', 'dela', 'delas', 'esta', 'estes', 'estas', 'aquele', 'aquela', 
    'aqueles', 'aquelas', 'isto', 'aquilo', 'estou', 'esta', 'estamos', 'estao', 
    'estive', 'esteve', 'estivemos', 'estiveram', 'estava', 'estavamos', 'estavam', 
    'estivera', 'estiveramos', 'esteja', 'estejamos', 'estejam', 'estivesse', 
    'estivessemos', 'estivessem', 'estiver', 'estivermos', 'estiverem', 'hei', 'ha', 
    'havemos', 'hao', 'houve', 'houvemos', 'houveram', 'houvera', 'houveramos', 'haja', 
    'hajamos', 'hajam', 'houvesse', 'houvessemos', 'houvessem', 'houver', 'houvermos', 
    'houverem', 'houverei', 'houvera', 'houveremos', 'houverao', 'houveria', 'houveriamos', 
    'houveriam', 'sou', 'somos', 'sao', 'era', 'eramos', 'eram', 'fui', 'foi', 'fomos', 
    'foram', 'fora', 'fôramos', 'seja', 'sejamos', 'sejam', 'fosse', 'fôssemos', 'fossem', 
    'for', 'formos', 'forem', 'serei', 'sera', 'seremos', 'serao', 'seria', 'seriamos', 
    'seriam', 'tenho', 'tem', 'temos', 'tem', 'tinha', 'tinhamos', 'tinham', 'tive', 'teve', 
    'tivemos', 'tiveram', 'tivera', 'tiveramos', 'tenha', 'tenhamos', 'tenham', 'tivesse', 
    'tivessemos', 'tivessem', 'tiver', 'tivermos', 'tiverem', 'terei', 'tera', 'teremos', 
    'terao', 'teria', 'teriamos', 'teriam']

    @classmethod
    def text_normalization(cls, text):
        '''Makes the text lowercase, removes punctuation, text inside square brackets, digits, 
        newlines and diacritics'''
        text = text.lower()
        text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
        text = re.sub('\[.*?\]', '', text)
        text = re.sub('\w*\d\w*', '', text)
        text = re.sub('\n', ' ', text)
        text = unidecode.unidecode(text)
        return text

    @classmethod
    def remove_stopwords(cls, text):
        '''Removes all the stopwords in the text. Stopwords are defined inside the class'''
        for stopword in cls.stopwords:
            if stopword in text:
                text = re.sub('\s+%s\s+' % stopword, ' ', text)
        return text


    @classmethod
    def lemmatization(cls, text):
        nlp = spacy.load('pt_core_news_sm')
        doc = nlp(text)
        lemma_text = ''
        for token in doc:
            lemma_text += token.lemma_
            lemma_text += ' '
            
        return lemma_text
