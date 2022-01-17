# -*- coding: utf-8 -*-
import function.get_data_mongo
# from collections import defaultdict

all = function.get_data_mongo.get_mongodb_row("data")

political = []
social = []
comedy = []
life = []
international = []
real_estate = []
sports = []
finance = []
china = []
pets = []
travel = []
health = []
consumption = []
fashion = []
cars = []
cool = []
netsearch = []
military = []
local = []
online_chat = []
famous = []
three_C = []
open_box = []
game = []
online_game = []
search = []
insurance = []
ET_come = []
law = []
direct_selling = []
movies = []
sex = []
parents = []
public_welfare = []
marketing = []
luck = []
out = []

cate_dic = {
    "政治":"political",
    "社會":"social",
    "影劇":"comedy",
    "生活":"life",
    "國際":"international",
    "房產雲":"real_estate",
    "體育":"sports",
    "財經":"finance",
    "大陸":'china',
    "寵物動物":'pets',
    "旅遊":'travel',
    "健康":'health',
    "消費":'consumption',
    "時尚":'fashion',
    "ET車雲":'cars',
    "新奇":'cool',
    "網搜":'netsearch',
    "軍武":'military',
    "地方":'local',
    "論壇":'online_chat',
    "名家":'famous',
    "3C家電":'three_C',
    "開箱雲":'open_box',
    "遊戲":'game',
    "電競":'online_game',
    "探索":'search',
    "保險":'insurance',
    "ET來了":'ET_come',
    "法律":'law',
    "直銷":'direct_selling',
    "電影":'movies',
    "男女":'sex',
    "親子":'parents',
    "公益":'public_welfare',
    "行銷雲":"marketing",
    "運勢":"luck",
    "公民(勿用)":"out",
    "ETlife(勿用)":'out'
    }


def generat_cate(i):
    i = list(i)
    title = "".join(i[0].split())
    cate = i[1]
    if cate == "政治":
        political.append(title)
    elif cate == "社會" :
        social.append(title)
    elif cate == "影劇" :
        comedy.append(title)
    elif cate == "生活" :
        life.append(title)
    elif cate == "國際" :
        international.append(title)
    elif cate == "房產雲" :
        real_estate.append(title)
    elif cate == "體育" :
        sports.append(title)
    elif cate == "財經" :
        finance.append(title)
    elif cate == "大陸" :
        china.append(title)
    elif cate == "寵物動物" :
        pets.append(title)
    elif cate == "旅遊" :
        travel.append(title)
    elif cate == "健康" :
        health.append(title)
    elif cate == "消費" :
        consumption.append(title)
    elif cate == "時尚" :
        fashion.append(title)
    elif cate == "ET車雲" :
        cars.append(title)
    elif cate == "新奇" :
        cool.append(title)
    elif cate == "網搜" :
        netsearch.append(title)
    elif cate == "軍武" :
        military.append(title)
    elif cate == "地方" :
        local.append(title)
    elif cate == "論壇" :
        online_chat.append(title)
    elif cate == "名家" :
        famous.append(title)
    elif cate == "3C家電" :
        three_C.append(title)
    elif cate == "開箱雲" :
        open_box.append(title)
    elif cate == "遊戲" :
        game.append(title)
    elif cate == "電競" :
        online_game.append(title)
    elif cate == "探索" :
        search.append(title)
    elif cate == "保險" :
        insurance.append(title)
    elif cate == "ET來了" :
        ET_come.append(title)
    elif cate == "法律" :
        law.append(title)
    elif cate == "直銷" :
        direct_selling.append(title)
    elif cate == "電影" :
        movies.append(title)
    elif cate == "男女" :
        sex.append(title)
    elif cate == "親子" :
        parents.append(title)
    elif cate == "公益" :
        public_welfare.append(title)
    elif cate == "行銷雲" :
        marketing.append(title)
    elif cate == "運勢" :
        luck.append(title)
    else:
        out.append(title)

for i in all:
    generat_cate(i)


print(f"政治:{len(political)}")
print(f"社會:{len(social)}")
print(f"影劇:{len(comedy)}")
print(f"生活:{len(life)}")
print(f"國際:{len(international)}")
print(f"房產雲:{len(real_estate)}")
print(f"體育:{len(sports)}")
print(f"財經:{len(finance)}")
print(f"大陸:{len(china)}")
print(f"寵物動物:{len(pets)}")
print(f"旅遊:{len(travel)}")
print(f"健康:{len(health)}")
print(f"消費:{len(consumption)}")
print(f"時尚:{len(fashion)}")
print(f"ET車雲:{len(cars)}")
print(f"新奇:{len(cool)}")
print(f"網搜:{len(netsearch)}")
print(f"軍武:{len(military)}")
print(f"地方:{len(local)}")
print(f"論壇:{len(online_chat)}")
print(f"名家:{len(famous)}")
print(f"3C家電:{len(three_C )}")
print(f"開箱雲:{len(open_box)}")
print(f"遊戲:{len(game)}")
print(f"電競:{len(online_game)}")
print(f"探索:{len(search)}")
print(f"保險:{len(insurance)}")
print(f"ET來了:{len(ET_come)}")
print(f"法律:{len(law)}")
print(f"直銷:{len(direct_selling)}")
print(f"電影:{len(movies)}")
print(f"男女:{len(sex)}")
print(f"親子:{len(parents)}")
print(f"公益:{len(public_welfare)}")
print(f"行銷雲:{len(marketing)}")
print(f"其餘：{len(out)}")

# for i in out:
#     print(i)
"政治"
"社會"
"影劇"
"生活"
"國際"
"房產雲"
"體育"
"財經"
"大陸"
"寵物動物"
"旅遊"
"健康"
"消費"
"時尚"
"ET車雲"
"新奇"
"網搜"
"軍武"
"地方"
"論壇"
"名家"
"3C家電"
"開箱雲"
"遊戲"
"電競"
"探索"
"保險"
"ET來了"
"法律"
"直銷"
"電影"
"男女"
"親子"
"公益"
"行銷雲"