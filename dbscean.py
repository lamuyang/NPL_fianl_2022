from scipy.fftpack import tilbert
import text_preprocess as tp
import pandas as pd
from sklearn.cluster import DBSCAN

def open_pkl(pkl):
    import pickle
    with open(f"{pkl}", 'rb') as fp:
        sorted = pickle.load(fp)
    fp.close()
    return sorted
stopword = open_pkl("/Users/yangsicheng/OneDrive - gapp.fju.edu.tw/輔大大三上/圖_自然語言與處理/final/NPL_fianl_2022/StopWords.pkl")
stopword = list(stopword)
stopword.extend(["使用研究","學系","探討","我國"])
# print(stopword)
raw_title = open_pkl("/Users/yangsicheng/OneDrive - gapp.fju.edu.tw/輔大大三上/圖_自然語言與處理/final/NPL_fianl_2022/new.pkl")
def orin_list(old_list):
    new_list = []
    for i in old_list:
        new_list.append("".join(i))
    return new_list
origin_title = orin_list(raw_title)
def stop(old_list):
    new_list = []
    for i in old_list:
        temp = []
        for j in i:
            if j not in stopword:
                temp.append(j)
        new_list.append(temp)
    return new_list

def list_to_space(old_list):
    new_list = []
    for i in old_list:
        new_list.append(" ".join(i))
    return new_list

title = stop(raw_title)

new_title = list_to_space(title)


# Input Data
# Q_clean_list = FAQ_df.clean_msg.tolist()
# category_list = FAQ_df.category.tolist()

# new_df = pd.DataFrame({'Q_clean': Q_clean_list, 'category': category_list})
# print(new_df)

tfidf_vectorizer, X_tfidf, tfidf_array, tfidf_T_array, terms = tp.tfidf(new_title, max_df=0.8, min_df=2)
print()

# DBSCAN
dbscan_clf = DBSCAN(eps=0.95, min_samples=5).fit(tfidf_array)
print(all(dbscan_clf.labels_ == dbscan_clf.fit_predict(tfidf_array)))
print(dbscan_clf.labels_)
print(dbscan_clf.fit_predict(tfidf_array))

# display by group
frame = pd.DataFrame(tfidf_array)
frame['Cluster'] = dbscan_clf.fit_predict(tfidf_array)
frame['title'] = title
# frame['Q_clean'] = Q_clean_list

print(frame['Cluster'].value_counts())

print("-----------------------------------------------")
print(frame.groupby('Cluster').agg({'Cluster':'count'}))

sectors = frame.groupby('Cluster')
sectors_len = len(sectors)

for ClusterN in range(-1, sectors_len -1, 1):
    print("===== Cluster {} =====".format(ClusterN))
    ClusterN_index = list(sectors.get_group(ClusterN).index)
    print(frame.loc[ClusterN_index].title)
