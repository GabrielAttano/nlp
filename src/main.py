import os, pickle
import nltk
from data_treatment import data_cleaner, file_reader
from bag_of_words import words_extractor, features_extractor

print("started loading words")
word = words_extractor.WordsExtractor(load_from_memory = True)
print("finished loading words")

print("started loading features")
features = features_extractor.FeaturesExtractor(load_from_memory= True)
print("finished loading features")

print("started saving features")
features.save_features(number_of_files = 100, file_name = "features_extractor_")
print("finished saving features")




# print("started training")
# classifier = nltk.NaiveBayesClassifier.train(features.features)
# print("finished training")

# reader = file_reader.FileReader()
# reader.go_to_directory("full_text_fake_news")
# fake_new = file_reader.FileReader.get_clean_text_from_file("1.txt")
# feature = features.extract_features(word.words, fake_new.split())
# result = classifier.prob_classify(feature)
# for key in result.samples():
#     print(key, result.prob(key))