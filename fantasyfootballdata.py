import requests  
r = requests.get('https://www.fantasypros.com/nfl/projections/rb.php?week=draft')

from bs4 import BeautifulSoup  
soup = BeautifulSoup(r.text, 'html.parser')  
results = soup.find_all('td', attrs={'class':'player-label'})

records = []  
for result in results:  
    player = result.find('a').text
    team = result.find('a').text[0:-1] + ', " "'
    records.append((player, team))

import pandas as pd  
df = pd.DataFrame(records, columns=['player', 'team'])  
df['player'] = pd.to_playername(df['player'])  
df.to_csv('2019fantasyrankings.csv', index=False, encoding='utf-8') 