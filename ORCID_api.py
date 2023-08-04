import requests


""" Looking for number of papers per year, papers per author, collaborative papers with coauthors, etc"""


link_lab_faculty = {
    "Negin Alemazkoor": "0000-0003-0221-3985",
    "Jonathan Goodall": "0000-0002-1112-4522",
    "Lawrence Band": "0000-0003-0461-0503",
    "Mahdur Behl": "0000-0002-5921-0331",
    "Tomonari Furukawa": "0000-0003-2811-4221"
    }


# ORCID for Jonathan Goodall
orcid_only = link_lab_faculty['Jonathan Goodall']

# URL for ORCID API
ORCID_RECORD_API = "https://pub.orcid.org/v3.0/"

# query ORCID for an ORCID record
def query_orcid_for_record(orcid_id):

    # response = requests.get(url=requests.utils.requote_uri(ORCID_RECORD_API + orcid_id),
    #                       headers={'Accept': 'application/json'})
    response = requests.get(url=requests.utils.requote_uri('https://pub.orcid.org/v3.0/0000-0002-9227-8514/work/733536'), headers={'Accept': 'application/json'})
    response.raise_for_status()
    result=response.json()
    return result


orcid_record = query_orcid_for_record(orcid_only)

# gets publications by author
works = orcid_record['activities-summary']['works']['group']

publications = []
number_of_publications = 0
publication_years = []

for i in works:
    summary = i['work-summary']
    for x in summary:
        # article title
        title = x['title']['title']['value']
        publications.append(title)
        number_of_publications += 1
        
        # journal title
        try:
            journal = x['journal-title']['value']
        except Exception:
            pass
        
        #publication year
        try:
            year = x['publication-date']['year']['value']
            publication_years.append(year)
        except Exception:
            pass
        
# convert list of publication year strings to integers
publication_years = [int(item) for item in publication_years]
# get average number of publications per year
pubs_per_year = number_of_publications / (max(publication_years) - min(publication_years))
        
print(orcid_record)
        


## TODO: seems like you can get the collaborating authors through the /works url (remember to look at stackoverflow thread regarding this)
            
    


