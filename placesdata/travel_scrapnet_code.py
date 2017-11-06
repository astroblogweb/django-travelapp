#meghalaya:    https://www.tripadvisor.in/Attractions-g297657-Activities-Meghalaya.html
#sikkim:       https://www.tripadvisor.in/Attractions-g297673-Activities-Sikkim.html


from google import search
from bs4 import BeautifulSoup
from urllib.request import urlopen
from pandas import DataFrame
##states=['meghalaya']
##query='tripadvisor.in atrractions activities places to visit in'+states[0]
##for url_gen in search(query, tld='co.in', lang='en',num=1, stop=1,pause=1.0):
##    url=url_gen    
##print(url)



url="https://www.tripadvisor.in/Attractions-g297657-Activities-Meghalaya.html"
page=urlopen(url)

soup = BeautifulSoup(page,'html.parser')
print(len(soup))
#print(soup.prettify())
#for item in list(soup.children):
#    print(item)
#rating=listing.find(class_=re.compile("ui_bubble_rating bubble_"))
#print(soup.find_all(id="FILTERED_LIST"))

def fetch_hours_GPS(site_link):
    page=urlopen(site_link)
    soup = BeautifulSoup(page,'html.parser')
    print(len(soup))
    



    
def extract_details(listing_info):
    sites=[]
    for listing in listing_info:
        #listing=listing_info[0]
        title=listing.find("div",attrs={"class":"listing_title "})
        site_name,site_city_parent=title.text.split('\n')[1:3]
        site_city_parent=site_city_parent[1:-1]
        site_link=listing.find("a")["href"][1:]

        #[site_spend,site_gps]=fetch_hours_GPS(site_link)
        
        rs_rating=listing.find("div",attrs={"class","rs rating"})
        site_rating=int(str(rs_rating.find("span"))[-11:-9])/10.0
        site_category=listing.find("div",attrs={"class","tag_line"}).text.strip()
        site_speciality=listing.find("div",attrs={"class","popRanking wrap"}).text.strip()
        #print(site_name)
        #print(site_name,site_city_parent,site_link,site_rating,site_category,site_speciality,sep='\n')
        site=[site_name,site_city_parent,site_link,site_rating,site_category,site_speciality]
        sites.append(site)
    #print(sites[-1])
    #print(len(sites))
    return(sites)


#listing_info=soup.find_all("div",attrs={"class":"listing_info"})
listing_info=soup.find_all("div",attrs={"class":"listing_details"})
sites=extract_details(listing_info)
site_headers=["site_name","site_city_parent","site_link","site_rating","site_category","site_speciality"]
len(sites)
sites_df=DataFrame(sites)
sites_df.columns=site_headers
print(sites_df.head())
#site_link='https://www.tripadvisor.in/'+'Attraction_Review-g668046-d2441213-Reviews-Double_Decker_Living_Root_Bridge-Cherrapunjee_East_Khasi_Hills_District_Meghalaya.html'
##fetch_hours_GPS(site_link)
##page=urlopen(site_link)
##soup = BeautifulSoup(page,'html.parser')
##print(len(soup))
##site_address=s.find("div",attrs={"class","detail_section address"}).text




