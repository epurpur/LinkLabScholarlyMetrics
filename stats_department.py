import requests
import json
import math
import pandas as pd
import random
import re

"""
From what I can tell, basically the way to get data out of ORCID is to make an API request to one of their endpoints
There is a python ORCID package but it was difficult to use. I have not used the ORCID R package. 
"""


orcid = "0000-0002-0271-5726" #this is for Shan Yu from dept of Statistics


# this holds each publication for all link lab faculty
all_publications_data = []

titles = []
authors = []    #author = "Orti, E. and Bredas, J.L. and Clarisse, C.",
dates = []
journals = []


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
        # take publications info and store in lists
                
        #first check if title contains chinese characters
        chinese_pattern = re.compile(r'[\u4e00-\u9fff]+')  # Pattern to match Chinese characters
                
        if isinstance(pub['title'], str):  # for some reason, some of the titles are not strings?
            if not chinese_pattern.search(pub['title']):
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


# create dataframe to hold all publications data
df = pd.DataFrame()
# put lists above into columns
df['Title'] = titles
df['Author'] = authors
df['Date'] = dates
df['Journal'] = journals


# clean erroneous HTML tags from the titles
def remove_html_tags(text):
    # Regular expression pattern to match HTML tags
    pattern = r'<[^>]+>'
    
    # Use re.sub to replace HTML tags with an empty string
    clean_text = re.sub(pattern, '', text)
    
    return clean_text

def remove_html_tags_from_list(string_list):
    # Initialize an empty list to store strings without HTML tags
    strings_without_html_tags = []
    
    for text in string_list:
        clean_text = remove_html_tags(text)
        strings_without_html_tags.append(clean_text)
    
    return strings_without_html_tags

titles = remove_html_tags_from_list(titles)
