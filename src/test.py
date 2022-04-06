import file_reader
import data_cleaner
import data_visualizer
import pandas as pd

df = data_visualizer.DataVisualizer.create_dataframe()

text = file_reader.FileReader.read_file("1.txt")
clean_text = data_cleaner.DataCleaner.text_normalization(text)
clean_text = data_cleaner.DataCleaner.remove_stopwords(clean_text)
clean_text = data_cleaner.DataCleaner.lemmatization(clean_text)
dictionary_data = data_visualizer.DataVisualizer.get_info(clean_text)
df = data_visualizer.DataVisualizer.df_append(dictionary_data, df)

text = file_reader.FileReader.read_file("2.txt")
clean_text = data_cleaner.DataCleaner.text_normalization(text)
clean_text = data_cleaner.DataCleaner.remove_stopwords(clean_text)
clean_text = data_cleaner.DataCleaner.lemmatization(clean_text)
dictionary_data = data_visualizer.DataVisualizer.get_info(clean_text)
df = data_visualizer.DataVisualizer.df_append(dictionary_data, df)

print(df)
