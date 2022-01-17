import requests
from bs4 import BeautifulSoup
import pandas as pd
import random

from requests.api import get
def get_data(year,month,day):
    url = f"https://www.ettoday.net/news/news-list-{year}-{month}-{day}-0.htm"

    user_agents = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
        ]

    headers = {
        "user-agent":random.choice(user_agents)
    }

    resp = requests.get(url, headers = headers)

    soup = BeautifulSoup(resp.text,"lxml")

    elem = soup.select(".part_list_2")

    title_list = []
    date_list = []
    cate_list = []

    for e in elem:
        title_list = [title.text for title in e.select("a")]
        date_list = [date.text for date in e.select(".date")]
        cate_list = [cate.text for cate in e.select("em")]

    return title_list,date_list,cate_list


df = pd.DataFrame()
year = 2014
month = 1
day = 1
all_title_list = []
all_date_list = []
all_cate_list = []

all_df = pd.DataFrame()

while year < 2022:
    if day <= 30:
        title_list,date_list,cate_list = get_data(year,month,day)
        if len(title_list) != 0:
            all_title_list.extend(title_list)
            all_date_list.extend(date_list)
            all_cate_list.extend(cate_list)
            # break
        if len(title_list) != 100:
            print(f"{year}-{month}-{day}")
        day += 1
    elif day > 30 and month < 12:
        title_list,date_list,cate_list = get_data(year,month,day)
        if len(title_list) != 0:
            all_title_list.extend(title_list)
            all_date_list.extend(date_list)
            all_cate_list.extend(cate_list)
        if len(title_list) != 100:
            print(f"{year}-{month}-{day}")
        day = 1
        month +=1
    elif day > 30 and month == 12:
        title_list,date_list,cate_list = get_data(year,month,day)
        if len(title_list) != 0:
            all_title_list.extend(title_list)
            all_date_list.extend(date_list)
            all_cate_list.extend(cate_list)
        if len(title_list) != 100:
            print(f"{year}-{month}-{day}")
        day = 1
        month = 1
        year +=1
        
all_df["title"] = all_title_list
all_df["data"] = all_date_list
all_df["cate"] = all_cate_list
print(all_df.info())
all_df.to_csv("all_data.csv")