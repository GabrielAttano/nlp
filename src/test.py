# import data_treatment.file_reader as file_reader
# import data_treatment.data_cleaner as data_cleaner
# import data_treatment.data_visualizer as data_visualizer
# import pandas as pd
# import data_treatment.data_analysis as data_analysis
# import os
import pickle

# df = data_visualizer.DataVisualizer.create_dataframe()
# fake_news_path = 'C:\\Users\\t6w31\\nlp\\Fake.br-Corpus\\full_texts\\fake'
# pickle_path = 'C:\\Users\\t6w31\\nlp\\pickles'
# os.chdir(fake_news_path)
# for i in range(1, 3602):
#     print("processing text " + str(i) + ".txt")
#     file_name = str(i) + ".txt"
#     text = file_reader.FileReader.read_file(file_name)
#     if text == None:
#         continue
#     text = data_cleaner.DataCleaner.text_normalization(text)
#     text = data_cleaner.DataCleaner.remove_stopwords(text)
#     text = data_cleaner.DataCleaner.lemmatization(text)
#     dictionary_data = data_visualizer.DataVisualizer.get_info(text)
#     dictionary_data["file_name"] = file_name
#     df = data_visualizer.DataVisualizer.df_append(dictionary_data, df)

# print(df)
# os.chdir(pickle_path)
# df.to_pickle('true_news.pkl')

with open("fake_news_sentences.pkl", "rb") as file:
    list = pickle.load(file)

for sentences in list:
    for sentence in sentences["sentences"]:
        if sentence == "vai te catar senadora!":
            print("achou!")


# df = pd.read_pickle('fake_news.pkl')
# print(df)