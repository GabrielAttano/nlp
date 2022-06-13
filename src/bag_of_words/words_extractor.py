import os, pickle
from data_treatment import data_cleaner, file_reader

class WordsExtractor():
    words = set()
    reader = file_reader.FileReader()
    
    def __init__(self, load_from_memory = False, file_name = "words_set.pkl"):
        if load_from_memory:
            self.load_words(file_name)

    def extract_all_words(self, news_type: bool, start_file = 1, end_file = 3602):
        if news_type == True:
            self.reader.go_to_directory(file_reader.Directories.NORMALIZED_TRUE_NEWS)
        else:
            self.reader.go_to_directory(file_reader.Directories.NORMALIZED_FAKE_NEWS)

        for i in range(start_file, end_file):
            text = self.reader.get_clean_text_from_file(str(i) + ".txt")
            if text == None:
                print("no file named" + str(i) + ".txt")
                continue
            print("getting words from " + str(i) + ".txt")
            for word in text.split():
                if word not in self.words:
                    self.words.add(word)

    def load_words(self, file_name = "words_set.pkl"):
        if not self.reader.go_to_directory(file_reader.Directories.PICKLES_BAG_OF_WORDS):
            print("couldn't find the directory to load words")
            return False

        if not file_name.endswith(".pkl"):
            print("The file_name should end with .pkl")
            return False

        try:
            file_to_read = open(file_name, "rb")
        except:
            print("No pickles were found when creating WordsExtractor object")
            return False
        else:
            loaded_words = pickle.load(file_to_read)
            self.words = loaded_words
            file_to_read.close()
            return True

    def save_words(self, file_name = "words_set.pkl"):
        if not self.reader.go_to_directory(file_reader.Directories.PICKLES_BAG_OF_WORDS):
            print("Couldn't find the directory to save words")
            return False
        if not file_name.endswith(".pkl"):
            print("The file_name should end with .pkl")
            return False
        
        file_to_store = open(file_name, "wb")
        pickle.dump(self.words, file_to_store)
        file_to_store.close()
        return True
            