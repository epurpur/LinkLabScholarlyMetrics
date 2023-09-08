

import requests
import json
import math
import pandas as pd
import random
import re


link_lab_orcids = {
        'Eric Loth': '0000-0003-4113-733X'
    }


"""Step 1: Make API requests for data about each faculty member and their publications"""

# this holds each publication for all link lab faculty
all_publications_data = []

titles = []
authors = []    
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
                # take publications info and store in lists
                
                #first check if title contains chinese characters
                chinese_pattern = re.compile(r'[\u4e00-\u9fff]+')  # Pattern to match Chinese characters
                
                if isinstance(pub['title'], str):
                    
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
                
    except Exception:
        pass
    
    
def identify_strings_with_html_tags(string_list):
    # Regular expression pattern to check for HTML tags
    pattern = r'<[^>]+>'
    
    # Initialize an empty list to store strings with HTML tags
    strings_with_html_tags = []
    
    for text in string_list:
        if re.search(pattern, text):
            strings_with_html_tags.append(text)
    
    return strings_with_html_tags
    
htmls = identify_strings_with_html_tags(authors)
print(htmls)

# clean erroneous HTML tags from the titles, authors, journal titles
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
authors = remove_html_tags_from_list(authors)
# journals = remove_html_tags_from_list(journals)

htmls = identify_strings_with_html_tags(authors)
print(htmls)
    
# create dataframe to hold all publications data
df = pd.DataFrame()
# put lists above into columns
df['Title'] = titles
df['Author'] = authors
df['Date'] = dates
df['Journal'] = journals





# """Step 2: Create BibTeX file from pandas dataframe """


# # Convert DataFrame to BibTeX format
# bibtex_data = ""
# for index, row in df.iterrows():
#     entry = f"@article{{{index},\n"
    
#     # Join authors using 'and' separator
#     authors = ' and '.join(row['Author'])
#     entry += f"  author = {{{authors}}},\n"
    
#     entry += f"  title = {{{row['Title']}}},\n"
#     entry += f"  year = {{{row['Date']}}},\n"
#     entry += f"  journal = {{{row['Journal']}}},\n"
#     entry = entry.rstrip(',\n')  # Remove trailing comma and newline
#     entry += "\n}\n\n"
#     bibtex_data += entry







def identify_strings_with_html_tags(string_list):
    # Regular expression pattern to check for HTML tags
    pattern = r'<[^>]+>'
    
    # Initialize an empty list to store strings with HTML tags
    strings_with_html_tags = []
    
    for text in string_list:
        if re.search(pattern, text):
            strings_with_html_tags.append(text)
    
    return strings_with_html_tags



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

# Example usage:
string_list = [
    'This is a plain text string.',
    '<p>This is an HTML string.</p>',
    'Another plain text string.',
    '<div>Yet another HTML string.</div>'
]

cleaned_strings = remove_html_tags_from_list(string_list)





