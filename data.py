from bs4 import BeautifulSoup
import requests
from ragam import Ragam
from ragam import Parent
from ragam import Child


url = "https://www.ragasurabhi.com/carnatic-music/ragas.html"
response = requests.get(url)

if response.status_code == 200:
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    
    
    ragas = soup.find_all('p', class_= "body_indexpage_para")
    for raga in ragas:
        # print(raga.find("a", class_="body_indexpage_assetlinktext").text)
        temp = raga.find("a", class_="body_indexpage_assetlinktext").text
        new_raga = Child(temp, 1, 2, 4, 98, "CHAKRAVAM")
        print(new_raga.name, new_raga.melaNumber)
        
else:
    print(f"Failed to retrieve the page: {response.status_code}")
    

