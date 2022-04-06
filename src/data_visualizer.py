import pandas as pd
import wordcloud
import data_analysis
from wordcloud import WordCloud
import matplotlib.pyplot as plt
class DataVisualizer:

    index_counter = 0

    @classmethod
    def create_dataframe(cls):
        df = pd.DataFrame(columns =['nouns', 'verbs', 'adjectives', 'avg_word_length', 'char_quantity', 'unique_words'])
        return df

    @classmethod
    def get_info(cls, text):
        dictionary_data = {}
        dictionary_data["nouns"] = data_analysis.DataAnalysis.noun_counter(text)
        dictionary_data["verbs"] = data_analysis.DataAnalysis.verb_counter(text)
        dictionary_data["adjectives"] = data_analysis.DataAnalysis.adjective_counter(text)
        dictionary_data["avg_word_length"] = data_analysis.DataAnalysis.average_word_length(text)
        dictionary_data["char_quantity"] = data_analysis.DataAnalysis.character_counter(text)
        dictionary_data["unique_words"] = data_analysis.DataAnalysis.unique_words_counter(text)
        return dictionary_data
        
    @classmethod
    def df_append(cls, dictionary_data, df):
        '''Append a dictionary type to a dataframe [THE DICTIONARY *MUST* FOLLOW THE get_info STYLE
        USED INSIDE THIS CLASS]'''
        # append is giving a warning, but i cant fix it now 
        df = df.append(dictionary_data, ignore_index=True)
        return df

    @classmethod
    def frequency_word_cloud(cls, text):
        '''Generates a wordcloud with the text used'''
        wordcloud = WordCloud(background_color='white').generate(text)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()