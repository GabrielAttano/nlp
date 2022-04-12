import pickle
import os

def classified_sentence_dict(sentence, classification, words, news_type, file_name):
    classified_sentence = {}
    classified_sentence["sentence"] = sentence
    classified_sentence["classification"] = classification
    classified_sentence["words"] = words
    classified_sentence["news_type"] = news_type
    classified_sentence["file_name"] = file_name

    return classified_sentence

def classify_sentence(sentence, news_type, file_name):
    print(sentence)
    print("[0] - Negative\n[1] - Positive\n[2] - Neutral")
    classification = 3
    while classification != 0 and classification != 1 and classification != 2: 
        classification = int(input())
        if classification != 0 and classification != 1 and classification != 2:
            print("invalid input")

    if classification == 2:
        return None

    print("Type in the words that make this sentence", end = " ")
    if classification == 1:
        print("positive: ")
    if classification == 0:
        print("negative: ")
    words = input().split()
    return classified_sentence_dict(sentence, classification, words, news_type, file_name)

def load_sentences(path, newsType: bool):
    os.chdir(path)

    if newsType == True:
        try:
            file = open("true_news_sentences.pkl", "rb")            
        except:
            print("Couldn't load true news sentences")
            return None
        else:
            return pickle.load(file)
    if newsType == False:
        try:
            file = open("fake_news_sentences.pkl", "rb")
        except:
            print("Couldn't load the progress of true news sentences")
            return None
        else:
            return pickle.load(file)

    return None

def load_classified_sentences(path, newsType: bool):
    os.chdir(path)

    if newsType == True:
        try:
            file = open("true_news_classified_sentences.pkl", "rb")            
        except:
            print("Couldn't load the progress of classified true_news")
            return None
        else:
            return pickle.load(file)

    if newsType == False:
        try:
            file = open("fake_news_classified_sentences.pkl", "rb")
        except:
            print("Couldn't load the progress of classified fake_news")
            return None
        else:
            return pickle.load(file)

    return None

def was_sentence_classified(classified_sentence_list, file_name_to_compare):
    for sentences in classified_sentence_list:
        if sentences["file_name"] == file_name_to_compare:
            return True
    return False

# Mudar os paths antes de executar o programa, não esquecer de colocar duas \\ para não dar problema ao ler o path
sentences_path = "C:\\Users\\t6w31\\nlp\\pickles\\sentences"
classified_sentences_path = "C:\\Users\\t6w31\\nlp\\pickles\\classified_sentences"
current_path = os.getcwd()

keep_loop = True
true_news_sentences = load_sentences(sentences_path, True)
if true_news_sentences == None:
    keep_loop = False
    print("critical error")

fake_news_sentences = load_sentences(sentences_path, False)
if fake_news_sentences == None:
    keep_loop = False
    print("critical error")

true_news_classified_sentences = load_classified_sentences(classified_sentences_path, True)
if true_news_classified_sentences == None:
    true_news_classified_sentences = []

fake_news_classified_sentences = load_classified_sentences(classified_sentences_path, False)
if fake_news_classified_sentences == None:
    fake_news_classified_sentences = []

print("Classify [1] - Fake news or [2] - True News?")
news_type = int(input())
if news_type != 1 and news_type != 2:
    print("Input not recognized")
    keep_alive = False

while keep_loop:
    if news_type == 1:
        for sentences in fake_news_sentences:
            if was_sentence_classified(fake_news_classified_sentences, sentences["file_name"]):
                print("skipping file named " + sentences["file_name"] + " for it was already classified")
                continue
            print("Classifying " + sentences["file_name"])
            for sentence in sentences["sentences"]:
                classified_sentence = classify_sentence(sentence, "fake_news", sentences["file_name"])
                if classified_sentence != None:
                    print("-------------------------------------------")
                    print(classified_sentence)
                    print("-------------------------------------------")
                    fake_news_classified_sentences.append(classified_sentence)
                    break

            print("succesfully classified a sentence. Type <s> to stop.")
            if input() == "s":
                keep_loop = False
                break

    if news_type == 2:
        for sentences in true_news_sentences:
            if was_sentence_classified(true_news_classified_sentences, sentences["file_name"]):
                print("skipping file named " + sentences["file_name"] + " for it was already classified")
                continue
            print("Classifying " + sentences["file_name"])
            for sentence in sentences["sentences"]:
                classified_sentence = classify_sentence(sentence, "true_news", sentences["file_name"])
                if classified_sentence != None:
                    print("-------------------------------------------")
                    print(classified_sentence)
                    print("-------------------------------------------")
                    true_news_classified_sentences.append(classified_sentence)
                    break

            print("succesfully classified a sentence. Type <s> to stop.")
            if input() == "s":
                keep_loop = False
                break

    break
    
os.chdir(classified_sentences_path)
with open('true_news_classified_sentences.pkl', 'wb') as file:
    pickle.dump(true_news_classified_sentences, file)
with open('fake_news_classified_sentences.pkl', 'wb') as file:
    pickle.dump(fake_news_classified_sentences, file)

