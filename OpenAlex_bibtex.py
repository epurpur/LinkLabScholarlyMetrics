"""
Iterates over each faculty member's ORCID. 
Collects all publications from all faculty members.
Assembles them into a BibTeX file. 
"""


import requests
import json
import math
import pandas as pd
import random


#ask for user input for upper and lower year constraints
start_year = int(input("Please enter a lower year limit: "))
end_year = int(input("Please enter an ending year limit: "))



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



"""Step 1: Make API requests for data about each faculty member and their publications"""

# this holds each publication for all link lab faculty
all_publications_data = []

titles = []
authors = []    #author = "Orti, E. and Bredas, J.L. and Clarisse, C.",
dates = []
journals = []


for name, orcid in link_lab_orcids.items():
    try:
        
        request = requests.get(f'https://api.openalex.org/authors/https://orcid.org/{orcid}')
        json_data = json.loads(request.text)


        #get URL from author info to get info about publications
        works_url_for_author = json_data['works_api_url']
        works_url_for_author = works_url_for_author.split("=")

        # get number of publications which will be used to find number of pages, for future API calls
        number_publications = json_data['works_count']
        number_of_pages = math.ceil(number_publications / 200)

        for i in range(number_of_pages):
            request2 = requests.get(f'https://api.openalex.org/works?filter={works_url_for_author[1]}&page={i+1}&per-page=200')
            json_data2 = json.loads(request2.text)
    
            for pub in json_data2['results']:
                # take publications info and store in list
                all_publications_data.append(pub)
                
                titles.append(pub['title'])
                dates.append(pub['publication_year'])
                
                # get journal title. Journal title not always available. If not available, just append "unknown journal"
                try:
                    journals.append(pub['primary_location']['source']['display_name'])
                except Exception:
                    journals.append('Unknown Journal')
                
        
                # must loop through authors to get each individual author for each publication. There can be many authors
                authors_by_publication = []
        
                for author in pub['authorships']:
                    author_name = author['author']['display_name']
                    authors_by_publication.append(author_name) 
                    
                
                # add group of authors_by_publication to authors list above
                authors.append(authors_by_publication)
        
    except Exception:
        pass
    
    
    
# create dataframe to hold all publications data
df = pd.DataFrame()
# put lists above into columns
df['Title'] = titles
df['Author'] = authors
df['Date'] = dates
df['Journal'] = journals



# remove rows from dataframe that have a publication date outside the time frame previously established by the user in start_year and end_year
df = df[(df['Date'] >= start_year) & (df['Date'] <= end_year)]



"""Step 2: Create BibTeX file from pandas dataframe """


# Convert DataFrame to BibTeX format
bibtex_data = ""
for index, row in df.iterrows():
    entry = f"@article{{{index},\n"
    
    # Join authors using 'and' separator
    authors = ' and '.join(row['Author'])
    entry += f"  author = {{{authors}}},\n"
    
    entry += f"  title = {{{row['Title']}}},\n"
    entry += f"  year = {{{row['Date']}}},\n"
    entry += f"  journal = {{{row['Journal']}}},\n"
    entry = entry.rstrip(',\n')  # Remove trailing comma and newline
    entry += "\n}\n\n"
    bibtex_data += entry


# Save to a .bib file
with open('Link_Lab_Publications.bib', 'w') as bibtex_file:
    bibtex_file.write(bibtex_data)
    






    



