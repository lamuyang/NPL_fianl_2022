from pymongo import MongoClient

def get_mongodb_row(collection_name):
    client = MongoClient('localhost', 27017)
    db = client["NLP"]
    collection = db[collection_name]

    cursor = collection.find({}, {"title":1,"cate":1,"_id":1})
    
    title = []
    cate = []
    allfields_list = [] #全部


    for row in cursor:
        title.append(row['title'])
        cate.append(row['cate'])
        allfields_list.append((row['title'],row['cate']))
  
    return allfields_list
    
# def pre_data(collection_name,name,keyword,abstract,content,reference,allfields_list):
#     allfields_list= get_mongodb_row(collection_name)

#     name = []
#     keyword = []
#     abstract = []
#     content = []
#     reference = []
#     for i in range(0,len(allfields_list)):
#         name.append(allfields_list[i][0])
#         keyword.append(allfields_list[i][1])
#         abstract.append(allfields_list[i][2])
#         content.append(allfields_list[i][3])
#         reference.append(allfields_list[i][4])
#     return name,keyword,abstract,content,reference













