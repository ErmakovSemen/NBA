from bs4 import BeautifulSoup
import requests
import json
import csv
import re
import pandas as pd
from tqdm import tqdm

BIGDATA_dr = {
    "name": [],
    "pos": [],
    "height": [],
    "weight": [],
    "gp": [],
    "min": [],
    "pts": [],
    "fgm": [],
    "fga": [],
    "fg%": [],
    "3pm": [],
    "3pa": [],
    "3p%": [],
    "ftm": [],
    "fta": [],
    "ft%": [],
    "reb": [],
    "ast": [],
    "stl": [],
    "blk": [],
    "tov": [],
    "pf": [],
    "drafted": [],
    "draft_year": [],
}

BIGDATA_undr = {
    "name": [],
    "pos": [],
    "height": [],
    "weight": [],
    "gp": [],
    "min": [],
    "pts": [],
    "fgm": [],
    "fga": [],
    "fg%": [],
    "3pm": [],
    "3pa": [],
    "3p%": [],
    "ftm": [],
    "fta": [],
    "ft%": [],
    "reb": [],
    "ast": [],
    "stl": [],
    "blk": [],
    "tov": [],
    "pf": [],
    "drafted": [],
    "draft_year": [],
}



for n in tqdm(range(2000, 2022)):

    print()

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36"
    }

    a = str(n)

    url = "https://basketball.realgm.com/nba/draft/past_drafts/" + a

    html = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(html.text, "lxml")

    with open ("draft.html", "w") as file:
        file.write(html.text)

    draft_hrefs = soup.find_all("h2", text=re.compile("Selections"))

    list_players = []
    for player in draft_hrefs:
        players = player.next_element.next_element.next_element.find("tbody").find_all("tr")
        list_players.append(players)

    players_dict_drafted = {}
    for player1 in list_players:
        for player in player1:
            player_href = "https://basketball.realgm.com" + player.find("a").get("href")
            player_name = player.find("a").text

            players_dict_drafted[player_name] = player_href

    with open("players_dict_drafted.json", "w") as file:
        json.dump(players_dict_drafted, file, indent=5)

    undraft_hrefs = soup.find("h2", text=("Undrafted Players")).next_element.next_element.next_element.find("tbody").find_all("tr")

    players_dict_undrafted = {}
    for player in undraft_hrefs:
        player_href = "https://basketball.realgm.com" + player.find("a").get("href")
        player_name = player.find("a").text

        players_dict_undrafted[player_name] = player_href

    with open("players_dict_undrafted.json", "w") as file:
        json.dump(players_dict_undrafted, file, indent=5)



    i = 0

    for player_name, player_href in players_dict_drafted.items():

        html1 = requests.get(url=player_href, headers=headers)
        link = html1.text

        soup = BeautifulSoup(link, "lxml")

        try:

            table_heading = soup.find("h2", text=("NCAA Season Stats - Per Game")).next_element.next_element.find("tfoot").find(class_="career per_game").find_all("td")
            BIGDATA_dr["gp"].append(table_heading[3].text)
            BIGDATA_dr["min"].append(table_heading[5].text)
            BIGDATA_dr["pts"].append(table_heading[6].text)
            BIGDATA_dr["fgm"].append(table_heading[7].text)
            BIGDATA_dr["fga"].append(table_heading[8].text)
            BIGDATA_dr["fg%"].append(table_heading[9].text)
            BIGDATA_dr["3pm"].append(table_heading[10].text)
            BIGDATA_dr["3pa"].append(table_heading[11].text)
            BIGDATA_dr["3p%"].append(table_heading[12].text)
            BIGDATA_dr["ftm"].append(table_heading[13].text)
            BIGDATA_dr["fta"].append(table_heading[14].text)
            BIGDATA_dr["ft%"].append(table_heading[15].text)
            BIGDATA_dr["reb"].append(table_heading[18].text)
            BIGDATA_dr["ast"].append(table_heading[19].text)
            BIGDATA_dr["stl"].append(table_heading[20].text)
            BIGDATA_dr["blk"].append(table_heading[21].text)
            BIGDATA_dr["tov"].append(table_heading[22].text)
            BIGDATA_dr["pf"].append(table_heading[23].text)

            BIGDATA_dr["name"].append(player_name)
            BIGDATA_dr["pos"].append(soup.find(class_="profile-box").find(class_="feature").text)
            BIGDATA_dr["height"].append(int(soup.find(class_="profile-box").find("strong", text=("Height:")).next_element.next_element.split()[1][1:-3]))
            BIGDATA_dr["weight"].append(int(soup.find(class_="profile-box").find("strong", text=("Weight:")).next_element.next_element.split()[1][1:-3]))
            BIGDATA_dr["drafted"].append(1)
            BIGDATA_dr["draft_year"].append(n)

        except:

            continue

        i += 1

        print(i, "-й игрок загрузился", sep='')



    for player_name, player_href in players_dict_undrafted.items():

        html1 = requests.get(url=player_href, headers=headers)
        link = html1.text

        soup = BeautifulSoup(link, "lxml")

        try:

            table_heading = soup.find("h2", text=("NCAA Season Stats - Per Game")).next_element.next_element.find("tfoot").find(class_="career per_game").find_all("td")
            BIGDATA_undr["gp"].append(table_heading[3].text)
            BIGDATA_undr["min"].append(table_heading[5].text)
            BIGDATA_undr["pts"].append(table_heading[6].text)
            BIGDATA_undr["fgm"].append(table_heading[7].text)
            BIGDATA_undr["fga"].append(table_heading[8].text)
            BIGDATA_undr["fg%"].append(table_heading[9].text)
            BIGDATA_undr["3pm"].append(table_heading[10].text)
            BIGDATA_undr["3pa"].append(table_heading[11].text)
            BIGDATA_undr["3p%"].append(table_heading[12].text)
            BIGDATA_undr["ftm"].append(table_heading[13].text)
            BIGDATA_undr["fta"].append(table_heading[14].text)
            BIGDATA_undr["ft%"].append(table_heading[15].text)
            BIGDATA_undr["reb"].append(table_heading[18].text)
            BIGDATA_undr["ast"].append(table_heading[19].text)
            BIGDATA_undr["stl"].append(table_heading[20].text)
            BIGDATA_undr["blk"].append(table_heading[21].text)
            BIGDATA_undr["tov"].append(table_heading[22].text)
            BIGDATA_undr["pf"].append(table_heading[23].text)

            BIGDATA_undr["name"].append(player_name)
            BIGDATA_undr["pos"].append(soup.find(class_="profile-box").find(class_="feature").text)
            BIGDATA_undr["height"].append(int(soup.find(class_="profile-box").find("strong", text=("Height:")).next_element.next_element.split()[1][1:-3]))
            BIGDATA_undr["weight"].append(int(soup.find(class_="profile-box").find("strong", text=("Weight:")).next_element.next_element.split()[1][1:-3]))
            BIGDATA_undr["drafted"].append(-1)
            BIGDATA_undr["draft_year"].append(n)

        except:

            continue

        i += 1
        print(i, "-й игрок загрузился", sep='')

        print()


with open("BIGDATA_dr.json", "w") as file:
    json.dump(BIGDATA_dr, file, indent=5)

df = pd.DataFrame(BIGDATA_dr)

with open("BIGDATA_undr-.json", "w") as file:
    json.dump(BIGDATA_undr, file, indent=5)

df = pd.DataFrame(BIGDATA_undr)

print('Загрузка завершена.')