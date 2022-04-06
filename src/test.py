import file_reader
import data_cleaner
import data_analysis

text = file_reader.FileReader.read_file("1.txt")
clean_text = data_cleaner.DataCleaner.text_normalization(text)
clean_text = data_cleaner.DataCleaner.remove_stopwords(clean_text)
clean_text = data_cleaner.DataCleaner.lemmatization(clean_text)
print("raw text:")
print(data_analysis.DataAnalysis.character_counter(text))
print("clean text:")
print(data_analysis.DataAnalysis.character_counter(clean_text))
