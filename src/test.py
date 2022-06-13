from data_treatment.file_reader import FileReader
from data_treatment.file_reader import Directories
from bag_of_words.features_extractor import FeaturesExtractor
from bag_of_words.words_extractor import WordsExtractor
import os
import nltk

trainingFeatures = FeaturesExtractor(True, file="normalized_features_list", total = 5)
print("started training")
classifier = nltk.NaiveBayesClassifier.train(trainingFeatures.features)
print("finished training")

testFeatures = FeaturesExtractor(True, file="normalized_features_list10.pkl")
print(testFeatures.features[19])
result = classifier.prob_classify(testFeatures.features[19][0])
for key in result.samples():
    print(key, result.prob(key))

