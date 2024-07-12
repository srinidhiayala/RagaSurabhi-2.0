from bs4 import BeautifulSoup
import requests
from ragam import Ragam
from ragam import Parent
from ragam import Child



def isParent(soup):
    
    p_tag = soup.find("p", class_="body_assetpage_ragaalias")
    
    if p_tag:
    # Extract the text content from the <p> tag
        full_text = p_tag.get_text(separator=' ', strip=True)
        pretty = ' '.join(full_text.split())
        
        # ragam is parent
        if len(pretty.split())==1:
            return -1 
       
        if pretty[0].isdigit():
            melaNumber = pretty.split()[0]
            return [True, melaNumber]
        
        #ragam is child
        else: 
            prettySplit = pretty.split()
            melaNumber = prettySplit[2]
            
            parent = prettySplit[4:]
            
            # data clean to find parent raegam
            for i in range (len(parent)):
                if parent[i] == ".":
                    parentName = parent[:i]
                    break
                elif parent[i] == "Alias:":
                    parentName = parent[:i]
                    break
                
            return [False," ".join(parentName), melaNumber]


url = "https://www.ragasurabhi.com/carnatic-music/ragas.html"
response = requests.get(url)

if response.status_code == 200:
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    
    
    ragas = soup.find_all('p', class_= "body_indexpage_para")
    for raga in ragas:
        # Finds the name of each ragam
        name = raga.find("a", class_="body_indexpage_assetlinktext").text
        # Find the link into each raga webpage
        suffix_link = raga.find("a").attrs["href"]
        
        new_link = "https://www.ragasurabhi.com" + suffix_link
        new_response = requests.get(new_link)
        
        if new_response.status_code == 200:
            html_content2 = new_response.text
            soup2 = BeautifulSoup(html_content2, 'html.parser')
            # determines if ragam is parent or not
            typeOfRagam=isParent(soup2) 
            print(typeOfRagam)
            # handle if -1 CASE!!!!
        
else:
    print(f"Failed to retrieve the page: {response.status_code}")
    


