import pandas as pd
import data_analysis

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
        # append is giving a warning, but i cant fix it now 
        df = df.append(dictionary_data, ignore_index=True)
        cls.index_counter += 1
        print(cls.index_counter)
        return df
