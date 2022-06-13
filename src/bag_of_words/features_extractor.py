import os, pickle
from data_treatment import file_reader

class FeaturesExtractor():
    features = list()
    reader = file_reader.FileReader()

    def __init__(self, load_from_memory = False, file = "features_list.pkl", total = 1):
        if load_from_memory:
            self.load_features(file_name = file, total_files = total)


    def extract_all_features(self, news_type: bool, words_set: set, start_file = 1, end_file = 3602):
        if news_type == True:
            self.reader.go_to_directory(file_reader.Directories.NORMALIZED_TRUE_NEWS)
        else:
            self.reader.go_to_directory(file_reader.Directories.NORMALIZED_FAKE_NEWS)
        
        for i in range(start_file, end_file):
            text = self.reader.get_clean_text_from_file(str(i) + ".txt")
            if text == None:
                print("no file named" + str(i) + ".txt")
                continue
            print("getting features from " + str(i) + ".txt")
            self.features.append(self.extract_features(
                word_set = words_set,
                split_text = text.split(),
                new_type = news_type
            ))
            

    def extract_features(self, word_set: set, split_text: list, new_type: bool = None):
        word_dict = dict()

        for word in word_set:
            # if word in split_text:
            #     word_dict[word] = True
            # else:
            word_dict[word] = False
        
        for word in split_text:
            word_dict[word] = True
        
        if new_type == True:
            return (word_dict, 'True')
        if new_type == False:
            return (word_dict, 'False')
        if new_type == None:
            return word_dict

    def load_features(self, file_name: str, directory = file_reader.Directories.PICKLES_BAG_OF_WORDS, total_files = 1, start_file = 1):
        
        self.reader.go_to_directory(directory)
        if total_files > 1:
            end_file = total_files + start_file
            if file_name.endswith(".pkl"):
                print("The file_name shouldn't end with .pkl when loading from more than one file")
                return False
            for i in range(start_file, end_file):
                file = file_name + str(i) + ".pkl"
                try:
                    file_to_read = open(file, "rb")
                except:
                    print("No pickles were found with the name " + file + ". Finishing early.")
                    return True
                else:
                    print("started loading features [" + file + "]...")
                    self.features.extend(pickle.load(file_to_read))
                    file_to_read.close()
                    print("... Finished")
            return True

        try:
            file_to_read = open(file_name, "rb")
        except:
            print("No pickles were found when creating FeaturesExtractor object")
        else:
            print("started loading features [" + file_name + "]...")
            loaded_features = pickle.load(file_to_read)
            self.features = loaded_features
            file_to_read.close()
            print("... Finished loading features")

    def save_features(self, number_of_files = 1, file_name = "features_list.pkl"):
        
        
        if number_of_files < 1:
            print("Invalid number of files")
            return False
        if not self.reader.go_to_directory(file_reader.Directories.PICKLES_BAG_OF_WORDS):
            print("cound find dir to save features in")
            return False
        if len(self.features) < 1:
            print("No features to be saved")
            return False
        
        if number_of_files == 1:
            file_to_store = open(file_name, "wb")
            pickle.dump(self.features, file_to_store)
            file_to_store.close()
            print("Saved features in 1 file")
            return True

        if file_name.endswith(".pkl"):
            print("The file_name shouldn't end with .pkl when saving in more than one file")
            return False
        
        start_index = 0
        end_index = 499
        for i in range (1, number_of_files):
            file = file_name + str(i) + ".pkl"
            file_to_store = open(file, "wb")
            pickle.dump(self.features[start_index:end_index], file_to_store)
            file_to_store.close()

            start_index = end_index + 1
            if start_index > len(self.features) - 1:
                print("Finished before expected [number of files too high]")
                break

            end_index += 500
            if end_index > len(self.features) - 1:
                end_index = len(self.features) - 1

            print("Saved feature in " + file + ".pkl")
        
        print("finished saving")
        return True
            

