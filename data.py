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
        
def getRagaDetailsString(soup):
    div_tag = soup.find("div", class_="body_assetpage_details_box")
    
    if div_tag:
        full_text = div_tag.get_text(separator=' ', strip=True)
        pretty = ' '.join(full_text.split())
    
    return pretty

def getAroAva(string):
    
    if "Note" in string:
        return -1
    index = string.rfind("Arohanam")
    whole = string[:index]
    aro = whole[9:whole.find("Avarohanam")]. strip()
    ava = whole[whole.find("Avarohanam")+11:].strip()
    
    return [aro,ava]
    
def aroAvaFile(soup):
    # div_tag = soup.find("div", class_="body_assetpage_details_box")
    ul_tag = soup.find("ul", class_="playlist")
    
    if ul_tag:
        first_li = ul_tag.find('li')
        
        if "Arohanam" in first_li.get_text():
       
            aroavalink = first_li.find('a')
            if aroavalink:
                link_url = aroavalink['href']
            
        else:
            return
            
    return ("https://www.ragasurabhi.com"+link_url)
    
def signatureFile(soup):
    
    ul_tag = soup.find("ul", class_="playlist")
    
    if ul_tag:
        li_tags = ul_tag.find_all('li')
        if len(li_tags) > 1:
            second_li = li_tags[1]
            
    if second_li:    
        if "Signature" in second_li.get_text():
            a_tag = second_li.find('a')
            if a_tag:
                link_url = a_tag['href']
        else:
            return 
    
    return ("https://www.ragasurabhi.com"+link_url)
    




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
            isRagaParent = isParent(soup2)
            
            if isRagaParent != -1:
                if isRagaParent[0] == True:
                    # ragam is parent, get mela num
                    melaNumber = isRagaParent[1]
                elif isRagaParent[0] == False:
                    # ragam is not parent, get parent and mela number
                    parentName = isRagaParent[1]
                    melaNumber = isRagaParent[2]

            
            # get all details String for raga
            details = getRagaDetailsString(soup2)
            # get Aro Ava
            aroAvaDetails = getAroAva(details) 
            if aroAvaDetails != -1:
                aro, ava = aroAvaDetails[0], aroAvaDetails[1]
            
            # generates the Aro/Ava link
            aroAvaLink = aroAvaFile(soup2)
            print(aroAvaLink)
            
            # generates the signature link
            signatureLink = signatureFile(soup2)
            
            # generates carnatic song and file
            
                
            
            
            
        
else:
    print(f"Failed to retrieve the page: {response.status_code}")
    


