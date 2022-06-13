import os, pickle
from data_treatment import data_cleaner
from enum import Enum, auto

class Directories(Enum):
    FULL_TEXT_FAKE_NEWS = "C:\\Users\\t6w31\\Desktop\\nlp\\Fake.br-Corpus\\full_texts\\fake"
    FULL_TEXT_TRUE_NEWS = "C:\\Users\\t6w31\\Desktop\\nlp\\Fake.br-Corpus\\full_texts\\true"
    NORMALIZED_FAKE_NEWS = "C:\\Users\\t6w31\\Desktop\\nlp\\Fake.br-Corpus\\size_normalized_texts\\fake"
    NORMALIZED_TRUE_NEWS = "C:\\Users\\t6w31\\Desktop\\nlp\\Fake.br-Corpus\\size_normalized_texts\\true"
    PICKLES_BAG_OF_WORDS = "C:\\Users\\t6w31\\Desktop\\nlp\\pickles\\bag_of_words"
    PICKLES_DATAFRAMES = "C:\\Users\\t6w31\\Desktop\\nlp\\pickles\\dataframes"
    PICKLES_SENTENCES = "C:\\Users\\t6w31\\Desktop\\nlp\\pickles\\sentences"
class FileReader:

    def go_to_directory(self, directory: Directories):
        if directory == Directories.FULL_TEXT_FAKE_NEWS:
            return self.__change_directory(Directories.FULL_TEXT_FAKE_NEWS)

        if directory == Directories.FULL_TEXT_TRUE_NEWS:
            return self.__change_directory(Directories.FULL_TEXT_TRUE_NEWS)

        if directory == Directories.NORMALIZED_FAKE_NEWS:
            return self.__change_directory(Directories.NORMALIZED_FAKE_NEWS)

        if directory == Directories.NORMALIZED_TRUE_NEWS:
            return self.__change_directory(Directories.NORMALIZED_TRUE_NEWS)

        if directory == Directories.PICKLES_BAG_OF_WORDS:
            return self.__change_directory(Directories.PICKLES_BAG_OF_WORDS)

        if directory == Directories.PICKLES_DATAFRAMES:
            return self.__change_directory(Directories.PICKLES_DATAFRAMES)

        if directory == Directories.PICKLES_SENTENCES:
            return self.__change_directory(Directories.PICKLES_SENTENCES)

        return False

    def __change_directory(self, directory: Directories):
        try:
            os.chdir(directory.value)
        except:
            print("Couldn't change the directory to " + directory.name)
            return False
        else:
            return True

    def read_file(self, file_name):
        '''Returns a string with the content of the file specified'''
        try:
            file = open(file_name, encoding="utf-8")
        except:
            print("no files were found with the name " + file_name)
            return None
        else:
            text = file.read()
            file.close()
            return text

    def get_clean_text_from_file(self, file_name):
        '''Returns a string with the content of the file specified already cleaned'''
        try:
            file = open(file_name, encoding="utf-8")
        except:
            print("no files were found with the name " + file_name)
            return None
        else:
            text = file.read()
            file.close()
            clean_text = data_cleaner.DataCleaner.process_text(text)
            return clean_text

class PickleReader:
    pass
