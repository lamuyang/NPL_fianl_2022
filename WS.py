import function.get_data_mongo
import function.pkl_input
import logging
stopword = function.pkl_input.open_pkl("StopWords.pkl")
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
    ws_data.append(list(i)[0])
word_sentence_list = ws(
    ws_data,
)
for i in word_sentence_list:
    print(i)

# count = 0
# for i in all:
#     temp = []
#     # print(i)
#     word_sentence_list = ws(
#         [list(i)[0]],
#     )
#     temp.extend([list(i)[1],list(i)[0],word_sentence_list])
#     ws_data.append(temp)
#     if count % 1000 == 0:
#         logging.info(f"{count}")
#     count += 1
# del ws
# for i in ws_data:
#     print(i)