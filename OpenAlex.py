

# UVA institutional ID:  I51556381
    
#info about institution
#https://api.openalex.org/institutions?filter=display_name.search:University%20of%20Virginia

#works by institution
#https://api.openalex.org/works?filter=institutions.id:I51556381


import requests
import json




"""
Section 1: Data for UVA as an institution
"""
#####INSTITUTIONAL IDs FOR UVA AND AFFILIATED INSTITUTIONS
# uva_id_URL ='https://openalex.org/I51556381'
# uva_health_id_URL = 'https://openalex.org/I2799765794'
# uva_urology_id_URL = 'https://openalex.org/I21113243'


# request = requests.get(f'https://api.openalex.org/institutions?filter=display_name.search:University%20of%20Virginia')

# json_data = json.loads(request.text)
# #print(json_data)
    
# results = json_data['results']
# print('')
# for result in results:
#     print(result['display_name'])
# print('')


# # there are a bunch of results for institutions with a name similar to "university of virginia". Filtering out just the right ones
# uva_data = results[0]
# uva_health_data = results[1] 
# uva_dept_of_urology = results[2]   # why is the separate?  I don't know why
# uva_medical_center = results[9]
# uva_childrens_hospital = results[10]
# uva_hospital = results[11]

# # potentially intersting UVA data?
# print(f"Total number of UVA publications: {uva_data['works_count']}")
# print(f"Total number of UVA Health publications: {uva_health_data['works_count']}")
# print(f"Total number of Department of Urology publications: {uva_dept_of_urology['works_count']}")
# print(f"Total number of UVA Medical Center publications: {uva_medical_center['works_count']}")
# print(f"Total number of UVA children's hospital': {uva_childrens_hospital['works_count']}")
# print(f"Total number of UVA hospital publications: {uva_hospital['works_count']}")


# print('')

# print(f"Total number of citations: UVA publications: {uva_data['cited_by_count']}")
# print(f"Total number of citations: UVA Health publications: {uva_health_data['cited_by_count']}")
# print(f"Total number of citations: UVA deptartment of Urology: {uva_dept_of_urology['cited_by_count']}")
# print(f"Total number of citations: UVA medical center: {uva_medical_center['cited_by_count']}")
# print(f"Total number of citations: UVA children's hospital': {uva_childrens_hospital['cited_by_count']}")
# print(f"Total number of citations: UVA hospital': {uva_hospital['cited_by_count']}")



# print('')

# print("Publication counts and citations per year (just University of Virginia)")

# counts_by_year = uva_data['counts_by_year']
# for year in counts_by_year:
#     print(f"Year: {year['year']}, Publications: {year['works_count']}, Citations: {year['cited_by_count']}")
    
    
"""
Section 1b - Answer question: List of most highly cited UVA publications in last 15 years
"""

# request = requests.get(f'https://api.openalex.org/institutions/I51556381')
# query works by institutional id for UVA
# request = requests.get('https://api.openalex.org/works?filter=institution.id:I51556381&page=50&per-page=200')
# json_data = json.loads(request.text)

#in 'results' key, results are ordered chronologically in descending order. This means, most recently published articles shown first. 
#Because I can only get 10,000 results at the moment, I cannot get results for all 128k published articles 
#results will show the most cited articles only for the most recent 10k publications

##CAVEAT: as of now, the 10,000th article dates back only to 2020. So I can get this figure but only dating back to 2020 which is kind of useless or am I wrong?


    

    
"""
Section 2: Works

There are 39790 affiliated authors at UVA in the dataset. I can only include 10,000 in the results.
The ability to include all is not currently available in the API (but is in the works)

"""
# request = requests.get('https://api.openalex.org/authors?filter=last_known_institution.id:I51556381,cited_by_count:>0&page=1&per-page=200')
# json_data = json.loads(request.text)
# # does this seem like too many?
# print(f"# authors with last known affiliation of UVA: {json_data['meta']['count']}")

# print("")
# print("")
# print(f"Printing Authors 1 - 200 (by production)")
# print("")

# authors = json_data['results']
# print(f"Authors on current page:")
# for author in authors:
#     print(author['display_name'])





"""
Section 3: Author
"""
# author ID of Brad Cox = A3037630497
# request = requests.get(f'https://api.openalex.org/authors/A3037630497')
# request = requests.get(f'https://api.openalex.org/authors/random')

# json_data = json.loads(request.text)
# print('author name: ', json_data['display_name'])

# # print(f"Numbers for {json_data['display_name']}: ")
# print(f"Publications: {json_data['works_count']}")
# # print(f"Citations: {json_data['cited_by_count']}")

"""
Section 3a - Answer question: what is most recent inactive year for author?
"""
# counts_by_year = json_data['counts_by_year']
# inactive_years = []

# for year in counts_by_year:
#     if year['works_count'] == 0:
#         inactive_years.append(int(year['year']))

# if len(inactive_years) == 0:
#     inactive_years.append('Currently active')
        
# print(f"Most recent inactive year for json_data['display_name']: {inactive_years[0]}")


"""
Section 3b - Answer question: What discipline does the author work in?
"""
# author ID of Brad Cox = A3037630497
# request = requests.get(f'https://api.openalex.org/authors/A3037630497')   # for specific author
# # request = requests.get(f'https://api.openalex.org/authors/random')      # for random author

# json_data = json.loads(request.text)

# ##### As of now, there is no given 'department' per say. The closest thing we can get is the 'x_concepts' field (subject to removal)
# ##### x_concepts is most frequently applied to works created by this author
# ##### ex: Brad Cox - 'particle physics', 'quantum mechanics', 'nuclear physics'
# concepts = []

# for discipline in json_data['x_concepts']:
#     concepts.append(discipline['display_name'])



"""
Section 4: Works
"""
#Section 4a  ##SPECIFIC ARTICLE
# request = requests.get(f'https://api.openalex.org/works/W2741809807')
# json_data = json.loads(request.text)

# print(f"Information about article... ")
# print(f"Title: {json_data['title']}") 
# print(f"Authors: ")
# print('')

# for author in json_data['authorships']:
#     print(author['author']['display_name'])
    
# print('')
# print(f"Publisher: {json_data['host_venue']['display_name']}")
    
# print('')
# print(f"OA status of this article: {json_data['open_access']['oa_status']}")


"""
Section 4b   ##RANDOM ARTICLE
"""
# request = requests.get(f'https://api.openalex.org/works/random')
# json_data = json.loads(request.text)

# print(f"Information about article... ")
# print('')
# print(f"Title: {json_data['title']}") 
# print('')
# print(f"Authors: ")

# for author in json_data['authorships']:
#     print(author['author']['display_name'])
    
# print('')
# print(f"Publisher: {json_data['host_venue']['display_name']}")
    
# print('')
# print(f"Open Access? : {json_data['open_access']['is_oa']}")
# print(f"OA status of this article: {json_data['open_access']['oa_status']}")


"""
Section 4c: Answer question: can we see yaer cited for citations by each publication?
""" 
# request = requests.get(f'https://api.openalex.org/works/random')
# json_data = json.loads(request.text)

# print(f"Original Article publication date: {json_data['publication_date']}")
# print(f"Number of citations: {json_data['cited_by_count']}")

# pages = 1

# # citation_request = requests.get(json_data['cited_by_api_url']+ '&page={pages}' + '&per-page=200')
# citation_request = requests.get(f"{json_data['cited_by_api_url']}&page={pages}&per-page=200")

# citation_json = json.loads(citation_request.text)

# year_of_citations = []

# # for result in citation_json['results']:
# #     year_of_citations.append(result['publication_year'])
# #     #######START HERE

# #the loop can execute a maximum of 50 times
# #this is because 10,000 results (current max) / 200 results per page = 50
# for i in range(50):
#     try:
#         citation_request = requests.get(f"{json_data['cited_by_api_url']}&page={pages}&per-page=200")
        
#         citation_json = json.loads(citation_request.text)
        
#         for result in citation_json['results']:
#             year_of_citations.append(result['publication_year'])
            
#         pages += 1
#     except Exception:
#         pass

# #print years of citations and number of citations per year
# print('Citation years and number of citations by year')
# print([[x,year_of_citations.count(x)] for x in set(year_of_citations)])



"""
Section 4d: Can we find items by DOI?  Specifically items from Libra by their DOI?
"""
# #DOI is available:
# request = requests.get(f'https://api.openalex.org/works/random')
# json_data = json.loads(request.text)
# print(f"DOI for this article: {json_data['doi']}")

# #Specific search for item by DOI (need to use doi.id)
# request = requests.get('https://api.openalex.org/works/doi:https://doi.org/10.1007/s11948-009-9148-z')
# json_data = json.loads(request.text)


## Is Libra info in there? (I'll try searching by display_name)
## There are SOME results from stuff in Libra Open. For example the following...

# request = requests.get('https://api.openalex.org/works?filter=display_name.search:Test of Ethical Sensitivity in Science and Engineering (TESSE)')
# json_data = json.loads(request.text)
# # DOI: https://doi.org/10.18260/1-2--3253
# # links to ASEE

# request = requests.get('https://api.openalex.org/works?filter=display_name.search:A Qualitative Examination of Content-Based Image Retrieval Behavior Using Systematically Modified Test Images')
# json_data = json.loads(request.text)
# # DOI: https://doi.org/10.1109/mwscas.2002.1187306
# # Links to IEEE

# request = requests.get('https://api.openalex.org/works?filter=display_name.search:The Engineering and Science Issues Test (ESIT): A Discipline-Specific Approach to Assessing Moral Judgment')
# json_data = json.loads(request.text)
# # DOI: https://doi.org/10.1007/s11948-009-9148-z
# # Links to Springer



"""
Testing
"""
# ORCID for Jonathan Goodall = 0000-0002-1112-4522
request = requests.get(f'https://api.openalex.org/authors/https://orcid.org/0000-0002-1112-4522')
# request = requests.get(f'https://api.openalex.org/authors/random')

json_data = json.loads(request.text)
print('author name: ', json_data['display_name'])

print(f"Numbers for {json_data['display_name']}: ")
print(f"Publications: {json_data['works_count']}")
print(f"Citations: {json_data['cited_by_count']}")
print(f"Works URL for author: {json_data['works_api_url']}")
works_url_for_author = json_data['works_api_url']

works_url_for_author = json_data['works_api_url']
works_url_for_author = works_url_for_author.split("=")


request2 = requests.get(f'https://api.openalex.org/works?filter={works_url_for_author[1]}')
json_data2 = json.loads(request2.text)

papers = json_data2['results']

for paper in papers:
    print(paper['display_name'])
    print("\t Authors...")
    for author in paper['authorships']:
        print(f" \t {author['author']['display_name']}")
    print()

##### IT LOOKS LIKE CO-AUTHOR INFORMATION IS AVAILABLE
##### SOME QUESTIONS ABOUT AUTHOR AMBIGUITY?  ESPECIALLY IF THERE ARE PEOPLE WITH COMMON NAMES
##### ALSO ONLY GETTING FIRST 25 PUBLICATIONS, CAN PROBABLY FIX THIS








