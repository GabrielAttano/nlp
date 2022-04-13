import pandas as pd
import pickle
import os
from math import sqrt
from math import exp
from math import pi

def load_dataset(path, news_type: bool):
    os.chdir(path)

    if news_type == False:
        try:
            file = open("fake_news.pkl", "rb")            
        except:
            print("Couldn't load fake_news.pkl dataframe")
            return None
        else:
            df = pickle.load(file)
            file.close()
            return df

    if news_type == True:
        try:
            file = open("true_news.pkl", "rb")
        except:
            print("Couldn't load true_news.pkl dataframe")
            return None
        else:
            df = pickle.load(file)
            file.close()
            return df

def dataset_union(fake_news_dataset, true_news_dataset):

    # Creating a new column to add the news type into it
    index = fake_news_dataset.index
    fake_news_number_of_rows = len(index)

    index = true_news_dataset.index
    true_news_number_of_rows = len(index)

    fake_news_list = []
    for i in range(fake_news_number_of_rows):
        fake_news_list.append(0)

    true_news_list = []
    for i in range(true_news_number_of_rows):
        true_news_list.append(1)

    fake_news_dataset["news_type"] = fake_news_list
    true_news_dataset["news_type"] = true_news_list

    union_dataset = pd.concat([fake_news_dataset, true_news_dataset], ignore_index=True)

    return union_dataset

def mean(numbers):
    # mean (Or average score)
    return sum(numbers)/float(len(numbers))

def standard_deviation(numbers):
    avg = mean(numbers)
    variance = sum([(x-avg)**2 for x in numbers]) / float(len(numbers)-1)
    return sqrt(variance)

def summarize_dataset(dataset):
    summaries = []
    summaries_dictionary = {}

    for column in dataset:
        # summaries_dictionary[column + "_mean_value"] = mean(dataset[column].tolist())
        # summaries_dictionary[column + "_stdev"] = standard_deviation(dataset[column].tolist())
        summaries.append(get_dict(mean(dataset[column].tolist()), standard_deviation(dataset[column].tolist()), column))
    summaries.append({'amount_analyzed':len(dataset.index)})
    return summaries

# Calculate the Gaussian probability distribution function for x
def calculate_probability(x, mean, stdev):
    exponent = exp(-((x-mean)**2 / (2 * stdev**2 )))
    return (1 / (sqrt(2 * pi) * stdev)) * exponent

# Calculate the probabilities of predicting each class for a given row
def calculate_class_probabilities(summary, row):
    probabilities = {}
    total_rows = summary[-2]
    total_rows = total_rows['amount_analyzed']
    news_type = summary[-1]
    news_type = news_type['news_type']
    for summary_split in summary:
        for key in summary_split.keys():
            #probabilities[news_type] = sum
    pass



def get_dict(mean_value, stdev_value, column_name):
    dictionary_values = {}
    dictionary_values[column_name + "_mean_value"] = mean_value
    dictionary_values[column_name + "_stdev"] = stdev_value
    return dictionary_values

path = "C:\\Users\\t6w31\\nlp\\pickles\\dataframes"
fake_news_dataset = load_dataset(path, False)
true_news_dataset = load_dataset(path, True)

dataset = dataset_union(fake_news_dataset, true_news_dataset)

fake_news_dataset = fake_news_dataset.drop('file_name', axis=1)
fake_news_dataset = fake_news_dataset.drop('news_type', axis=1)
true_news_dataset = true_news_dataset.drop('file_name', axis = 1)
true_news_dataset = true_news_dataset.drop('news_type', axis = 1)
fake_news_summary = summarize_dataset(fake_news_dataset)
fake_news_summary.append({'news_type': 0})
true_news_summary = summarize_dataset(true_news_dataset)
true_news_summary.append({'news_type': 1})
print("True news summary:")
print(true_news_summary)
print("Fake news summary:")
print(fake_news_summary)
calculate_class_probabilities(true_news_summary, 5)