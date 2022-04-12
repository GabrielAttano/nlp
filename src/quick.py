import data_treatment.file_reader as file_reader
import sentiment_analysis.sentence_gatherer as sentence_gatherer
import os
import pickle
import string

def create_dict(file_name, text):
    sentences = {}
    sentences["file_name"] = file_name
    sentences["sentences"] = sentence_gatherer.SentenceGet.get_sentences(text)
    return sentences

fake_news_path = 'C:\\Users\\t6w31\\nlp\\Fake.br-Corpus\\full_texts\\fake'
pickle_path = 'C:\\Users\\t6w31\\nlp\\pickles\\sentences'

sentences = {}
sentences_list = []
os.chdir(fake_news_path)
for i in range (1, 3602):

    print("getting sentences from " + str(i) + ".txt")
    file_name = str(i) + ".txt"
    text = file_reader.FileReader.read_file(file_name)
    if text == None:
        continue
    text = text.lower()
    sentences_list.append(create_dict(file_name, text))

os.chdir(pickle_path)
with open('fake_news_sentences.pkl', 'wb') as file:
    pickle.dump(sentences_list, file)
