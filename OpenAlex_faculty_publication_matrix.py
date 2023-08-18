

import requests
import json
import math
import pandas as pd



link_lab_orcids = {
        'Negin Alemazkoor': '0000-0003-0221-3985',
        'Homa Alemzadeh': '0000-0001-5279-842X',          #?
        'Larry Band': '0000-0003-0461-0503',
        'Laura Barnes': '?',
        'Madhur Behl': '0000-0002-5921-0331',
        'Nicola Bezzo': '0000-0001-6627-5048',            #?        
        'Matthew Bolton': '?',
        'Steven Bowers': '?',
        'Maite Brandt-Pearce': '0000-0002-2566-8280',
        'Benton Calhoun': '0000-0002-3770-5050',
        'Brad Campbell': '?',
        'Qing Chang': '0000-0003-3744-1371',
        'T Donna Chen': '0000-0002-7026-3418',              #?
        'Seokhyun Chung': '?',
        'Haibo Dong': '?',
        'Afsaneh Doryab': '0000-0003-1575-385X',          #?
        'Lu Feng': '0000-0002-4651-8441',
        'Tomonari Furukawa': '0000-0003-2811-4221',
        'Gregory Gerling': '0000-0003-3137-3822',
        'Jonathan Goodall': '0000-0002-1112-4522',
        'Devin Harris': '0000-0003-0086-1073',
        'Seongkook Heo': '0000-0003-2004-4812',
        'Arsalan Heydarian': '0000-0001-5972-6947',
        'Tariq Iqbal': '0000-0003-0133-1234',
        'Barry Johnson': '0000-0001-6707-7588',
        'Yen-Ling Kuo': '0000-0002-6433-6713',               #?
        'Venkataraman Lakshmi': '0000-0001-7431-9004',
        'James Lambert': '0000-0002-0697-8339',
        'Zongli Lin': '0000-0003-1589-1443',
        'Felix Xiaozhu Lin': '?',
        'Liu Zhen': '0000-0001-8013-3804',                 #?
        'Eric Loth': '0000-0003-4113-733X',
        'Osman Ozbulut': '0000-0003-3836-3416',            #?
        'Byungkyu Brian Park': '0000-0003-4597-6368',
        'Daniel Quinn': '?',
        'Sara Riggs': '0000-0002-0112-9469',
        'Haiying Shen': '?',
        'Cong Shen': '?',
        'Brian Smith': '0000-0001-5102-6399',
        'Mircea Stan': '0000-0003-0577-9976',
        'John Stankovic': '0000-0001-7307-9395',
        'Yixin Sun': '0000-0001-6650-4373',
        'Sarah Sun': '0000-0003-1086-8017',
        'Yuan Tian': '0000-0002-6435-564X',
        'Shangtong Zhang': '0000-0003-4255-1364'
        
    }



# faculty_names = []

# for key, value in link_lab_orcids.items():
#     faculty_names.append(key)
    

# df = pd.DataFrame(columns=faculty_names)

"""
GET PUBLICATIONS BY YEAR FOR ONE FACULTY MEMBER
"""

# orcid = '0000-0003-1589-1443'

# request = requests.get(f'https://api.openalex.org/authors/https://orcid.org/{orcid}')

# json_data = json.loads(request.text)
# faculty_name = json_data['display_name']
# number_publications = json_data['works_count']
            
# # print(f"Works URL for author: {json_data['works_api_url']}")
# works_url_for_author = json_data['works_api_url']

# works_url_for_author = works_url_for_author.split("=")

# all_publications_info = []   #holds all publications



# number_of_pages = math.ceil(number_publications / 200)

# request2 = requests.get(f'https://api.openalex.org/works?filter={works_url_for_author[1]}&page={number_of_pages+1}&per-page=200')
# json_data2 = json.loads(request2.text)

# # iterate of number of pages needed per author
# for i in range(number_of_pages):
#     request2 = requests.get(f'https://api.openalex.org/works?filter={works_url_for_author[1]}&page={i+1}&per-page=200')
#     json_data2 = json.loads(request2.text)
            
#     # take publications info and store in list
#     for pub in json_data2['results']:
#         all_publications_info.append(pub)
        
        
        
# # go through all_publication_info. End result will be a dict with year, # of pubs like: {1999:1, 2000:3, 2001:4}
# pubs_by_year = {}
# for pub in all_publications_info:
#     year = pub['publication_year']
    
#     if year not in pubs_by_year:
#         pubs_by_year[year] = 1
#     else:
#         pubs_by_year[year] += 1
        
        
        
"""
GET PUBLICATIONS BY YEAR FOR MULTIPLE FACULTY MEMBERS
"""

orcids = {
        'Jonathan Goodall': '0000-0002-1112-4522',
        'Larry Band': '0000-0003-0461-0503'  ,
        'Negin Alemazkoor': '0000-0003-0221-3985'
    }

all_data = {}
all_years = []

for name, orcid in link_lab_orcids.items():
    try:
        individual_pubs = {}
        
        request = requests.get(f'https://api.openalex.org/authors/https://orcid.org/{orcid}')
        json_data = json.loads(request.text)
    
        #get URL from author info to get info about publications
        works_url_for_author = json_data['works_api_url']
        works_url_for_author = works_url_for_author.split("=")
        all_publications_info = []   #holds all publications
        
        # get number of publications which will be used to find number of pages, for future API calls
        number_publications = json_data['works_count']
        number_of_pages = math.ceil(number_publications / 200)
    
        for i in range(number_of_pages):
            request2 = requests.get(f'https://api.openalex.org/works?filter={works_url_for_author[1]}&page={i+1}&per-page=200')
            json_data2 = json.loads(request2.text)
    
            for pub in json_data2['results']:
                # take publications info and store in list
                all_publications_info.append(pub)
                
                
        # look at all_publications_info for each person
        for pub in all_publications_info:
            year = pub['publication_year']
            
            # check to see if year in all_years above
            if year not in all_years:
                all_years.append(year)
                
            if year not in individual_pubs:
                individual_pubs[year] = 1
            else:
                individual_pubs[year] += 1
    
        all_data[name] = individual_pubs
        
    except Exception:
        pass

 





# sort all_years ascending order
all_years.sort()

# now need to iterate over each faculty dictionary to populate them with all years for all faculty members. 
# if someone didn't publish in a certain year, they get a 0 for publications that year
for name, data_dict in all_data.items():
    for year in all_years:
        # if year is not a key in current dictionary, add it with a value of 0
        if year not in data_dict:
            data_dict[year] = 0
        


# create dataframe to store final data
df = pd.DataFrame(all_data)
df = df.reindex(all_years)
# add 'total' column to end of each row
df['Total'] = df.sum(axis=1)

# export final dataframe
df.to_csv('/Users/ep9k/Desktop/LinkLab/pubs_by_year_matrix.csv')
