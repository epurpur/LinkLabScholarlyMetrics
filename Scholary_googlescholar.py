
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


faculty_list = {'Negin Alemazkoor': "lDDZYr0AAAAJ",
                'Homa Alemzadeh': 'sXpmLxUAAAAJ',
                'Larry Band': 'hKmmMrAAAAAJ',
                'Laura Barnes' : "h-Lr0bQAAAAJ",
                'Madhur Behl': "bj_imaYAAAAJ",
                'Nicola Bezzo': "lyNOlzoAAAAJ",
                'Matthew Bolton': "6c19RG8AAAAJ",
                'Steven M. Bowers': "0h-RyocAAAAJ",
                'Maite Brandt-Pearce': "KFLFbWoAAAAJ&hl",
                'Benton Calhoun': "I7a8pr0AAAAJ&hl",
                'Brad Campbell': "MLx5TCQAAAAJ&hl", 
                'Qing Chang' : "TfPemJcAAAAJ",
                'Donna T. Chen': "l20iH34AAAAJ",
                'Haibo Dong': "SrYdog8AAAAJ",
                'Afsaneh Doryab': "O0lONMkAAAAJ",
                'Lu Feng': "HiyMQzEAAAAJ",
                'Tomonari Furukawa': "RMETVDwAAAAJ",
                'Gregory Gerling': "ibBUGLAAAAAJ&hl",
                'Jonathan L. Goodall': "M9aKXDwAAAAJ",
                'Devin Harris': "Y0e7hZsAAAAJ&hl",
                'Seongkook Heo': "7r0_F0kAAAAJ",
                'Arsalan Heydarian': "VTdMErEAAAAJ&hl",
                'Tariq Iqbal': "t_ndTI4AAAAJ&hl",
                'Barry Johnson': "vMTL9koAAAAJ&hl",
                'Yen-Ling Kuo': 'pNkyRs4AAAAJ',
                'Venkataraman Lakshmi': "vbNdSy0AAAAJ",
                'James H. Lambert': "qVfffxkAAAAJ",
                'Zongli Lin': "n4fG76YAAAAJ",
                'Felix Xiaozhu Lin': "f6FFhS8AAAAJ",
                'Eric Loth': "AqEcQtYAAAAJ",
                'Osman E. Ozbulut': "VdoAeqAAAAAJ",
                'B. Brian Park': "I23GOcEAAAAJ",
                'Daniel Quinn': "8A8eaZMAAAAJ",
                'Sara Riggs': "ALjgMAoAAAAJ",
                'Haiying Shen': "W0Cx7ZAAAAAJ",
                'Cong Shen': "70LBhKcAAAAJ",
                'Brian L. Smith': "9uFvl5wAAAAJ",
                'Stan R. Mircea': "5DLZvlMAAAAJ",
                'John Stankovic': "4VJre9IAAAAJ",
                'Yixin Sun': "ov72AA4AAAAJ",
                'Sarah Sun': "7oNkNtIAAAAJ",
                'Yuan Tian': "ja0GtqgAAAAJ",
                'Shangtong Zhang': "Pn7fj4IAAAAJ"
    }

# search_query = scholarly.search_author('Jonathan Goodall, Virginia')
search_query = scholarly.search_author_id('7oNkNtIAAAAJ')
# test = search_query['source']
# author = scholarly.fill(next(search_query))
author_name = search_query['name']

search2 = scholarly.search_author(author_name)
author_info = scholarly.fill(next(search2))

# # get author's google scholar id
# author_id = author['scholar_id']

# # publications are in a list. Get last publication in list (most recent publication?)
# publications = author['publications']
# # print name of all publications
# for pub in publications:
#     print(pub['bib']['title'])
#     print()


# for i in faculty_list:
#     search_query = scholarly.search_author(f"{i}, Virginia")
    
#     # scholarly returns a generator object
#     author = scholarly.fill(next(search_query))
    
    
    
    