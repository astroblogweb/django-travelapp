from google import search
from bs4 import BeautifulSoup
from urllib.request import urlopen
from pandas import DataFrame
import re

def choose_state(site_state,max_listing=5):
    url_final=get_state_URL(site_state,max_listing)
    site_state=url_final.split('-')[-1].split('.')[0]
    print("site_state:\t",site_state)
    page=urlopen(url_final)
    soup = BeautifulSoup(page,'html.parser')
#    print(len(soup))
    listing_info=soup.find_all("div",attrs={"class":"listing_details"})
    sites=extract_details(site_state,url_final,listing_info,max_listing)
    site_headers=["site_state","site_name","site_city_parent","site_link","site_rating","site_category","site_speciality"]
#    print("retrieved data for :",len(sites),"sites")
    sites_df=DataFrame(sites)
    sites_df.columns=site_headers
    print(sites_df.head())
    return(sites_df)





def get_state_URL(site_state,max_listing):
    ss=''.join(site_state.split()).lower()
    query='tripadvisor.in places to visit in'+'_'.join(site_state.split())
    url=[];url_final=""
    for url_gen in search(query, tld='co.in', lang='en',num=10, stop=10,pause=1.0):
        output=re.search(r'^(https://www.tripadvisor.in/).*(attractions).*(activities).*[^0-9].*(html)',url_gen,re.M|re.I)
        if output:
            url.append(url_gen)
            final=''.join([x for x in url[-1].split('-')[-1].split('.')[0].split('_')]).lower()
            if final == ss:
                url_final=url[-1]
                break 
    print("site_state:",site_state,"\t","final URL:",url_final)
    return(url_final)





    
def extract_details(site_state,url_final,listing_info,max_listing):
    sites=[]
    for index,listing in enumerate(listing_info):
        if index>max_listing:
            break
        #listing=listing_info[0]
        title=listing.find("div",attrs={"class":"listing_title "})
        site_name,site_city_parent=title.text.split('\n')[1:3]
        site_city_parent=site_city_parent[1:-1]
        site_link=listing.find("a")["href"][1:]
        site_link=url_final.split('/')[-2]+'/'+site_link
#        print(site_link)
        #[site_spend,site_gps]=fetch_hours_GPS(site_link)
        rs_rating=listing.find("div",attrs={"class","rs rating"})
        site_rating=int(str(rs_rating.find("span"))[-11:-9])/10.0
        site_category=listing.find("div",attrs={"class","tag_line"}).text.strip()
        site_speciality=listing.find("div",attrs={"class","popRanking wrap"}).text.strip()
        #print(site_name)
        #print(site_name,site_city_parent,site_link,site_rating,site_category,site_speciality,sep='\n')
        site=[site_state,site_name,site_city_parent,site_link,site_rating,site_category,site_speciality]
        sites.append(site)
    #print(sites[-1])
    #print(len(sites))
    return(sites)

#print("printing")
#states=['meghalaya']
#for state in states:
#    sites_df=choose_state(state)




