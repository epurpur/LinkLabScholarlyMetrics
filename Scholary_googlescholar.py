
from scholarly import scholarly


# EXAMPLE 1

# search for faculty member, get their publications
# search_query = scholarly.search_author('Alemazkoor, Virginia')
# author = scholarly.fill(next(search_query))

# # get author's google scholar id
# author_id = author['scholar_id']

# # publications are in a list. Get last publication in list (most recent publication?)
# publications = author['publications'][-1]
# # print name of all publications
# # for pub in publications:
# #     print(pub['bib']['title'])
    

    
    

# EXAMPLE 2

# take one of faculty member's publications, get info about that publication including co-authors
# search_by_pub_title = scholarly.search_single_pub(publications['bib']['title'])
# all_authors = search_by_pub_title['author_id']

# for author in all_authors:
#     current_author = scholarly.search_author_id(author)
#     print(current_author['name'], current_author['affiliation'])





# EXAMPLE 3

# go from article title to scholarly profile for faculty member
# new_query = scholarly.search_single_pub("Efficient Stochastic Analysis of Power Distribution Systems Using Polynomial Models")
# authors = new_query['author_id']

# get_author_name = scholarly.search_author_id(authors[0])
# get_author_info = scholarly.search_author(get_author_name['name'])






# TEST ON OTHER LINK LAB FACULTY

faculty = ['Madhur Behl', 'Nicola Bezzo', 'Matthew Bolton', 'Maite Brandt-Pearce', 'Benton H. Calhoun']

search_query = scholarly.search_author('Benton Calhoun, Virginia')

author = scholarly.fill(next(search_query))

# get author's google scholar id
author_id = author['scholar_id']

# publications are in a list. Get last publication in list (most recent publication?)
publications = author['publications']
# print name of all publications
for pub in publications:
    print(pub['bib']['title'])
    print()