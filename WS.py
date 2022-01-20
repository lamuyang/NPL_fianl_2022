import function.get_data_mongo
import function.pkl_input
import logging
stopword = function.pkl_input.open_pkl("StopWords.pkl")
stopword = list(stopword)
stopword.append("⋯")

from ckiptagger import data_utils, construct_dictionary, WS

FORMAT = '%(asctime)s %(levelname)s: %(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMAT)

all = function.get_data_mongo.get_mongodb_row("data")
def de_stopword(old_list):
    new_list = []
    for i in old_list:
        temp = []
        for j in i:
            if j not in stopword:
                temp.append(j)
        new_list.append(temp)
    return new_list
ws = WS("./data")
ws_data = []
for i in all:
    ws_data.append(list(i)[0].replace("\u3000",""))
word_sentence_list = ws(
    ws_data,
    segment_delimiter_set = {",", "。", ":", "?", "!", ";","／",":","："},
)
# for i in word_sentence_list:
#     print(i)
new_data = de_stopword(word_sentence_list)
# for i in new_data:
#     print(i)
import pickle
with open("new.pkl","wb") as fileobj:
    pickle.dump(new_data, fileobj)