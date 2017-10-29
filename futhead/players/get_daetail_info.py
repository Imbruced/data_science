from bs4 import BeautifulSoup
import re
import requests
import json

url = 'http://www.futhead.com/18/players/4304/robert-lewandowski/'
data = requests.get(url).content.decode('utf-8')
soup = BeautifulSoup(data, 'html.parser')

#this list stores information about basics statistics of the player
player_data = []
# this line of code scrapping basic statistics of player
dictionary = {}
# for iter in range(1,7):
#     try:
seek_element = soup.find_all('div', {'class': re.compile('playercard-attr playercard-attr\d')})
for iter in seek_element:
    basic_statistics = iter.text.strip().split(' ')
    dictionary[basic_statistics[1]] = basic_statistics[0]
    # except Exception as e:
    #     pass


#this line of code scrapping more detail;ed info

detailed_statistics = []
detailed_data_stats = soup.find_all('span', {'class': 'player-stat-title'})
detailed_data_value = soup.find_all('span', {'class': re.compile('player-stat-value chembot-value stat-color-\d pull-right')})
for value, name in zip(detailed_data_value, detailed_data_stats):
    dictionary[name.text.strip()] = value.text.strip()


player_data.append(dictionary)


json_data = json.loads(requests.get('http://www.futhead.com/prices/api/?year=18&id=176580').content.decode('utf-8'))
# print(json_data)

dictionary['ps_prize_min'] = json_data['176580']['psLowFive'][0]
dictionary['ps_prize_1'] = json_data['176580']['psLowFive'][1]
dictionary['ps_prize_2'] = json_data['176580']['psLowFive'][2]
dictionary['ps_prize_3'] = json_data['176580']['psLowFive'][3]
dictionary['ps_prize_4'] = json_data['176580']['psLowFive'][4]

# # print(data)
# print(player_data)

dane_personalne = soup.find_all('div', {'class': 'col-xs-7'})
dane_personalne_value = soup.find_all('div', {'class', 'col-xs-5 player-sidebar-value'})
for key, value in zip(dane_personalne, dane_personalne_value):
    if len(key)>0:
        dictionary[key.text.strip()] = value.text.strip()

dictionary['rating'] = soup.find('div', {'class': 'playercard-rating'}).text.strip()
dictionary['name'] = soup.find('div', {'class': 'playercard-name'}).text.strip()
dictionary['pozycja'] = soup.find('div', {'class': 'playercard-position'}).text.strip()
dictionary['skills'] = soup.find('div', {'class': 'playercard-skill-move'}).text.strip()
dictionary['weak_foot'] = soup.find('div', {'class': 'playercard-weak-foot'}).text.strip()



print(dictionary)
