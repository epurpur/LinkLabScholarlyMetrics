
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

faculty_list = ['Negin Alemazkoor', 
                'Homa Alemzadeh', 
                'Larry Band', 
                'Laura Barnes', 
                'Madhur Behl', 
                'Nicola Bezzo', 
                'Matthew Bolton',
                'Steven M. Bowers', 
                'Maite Brandt-Pearce', 
                'Benton Calhoun', 
                'Brad Campbell', 
                # 'Cindy Chang', Does Qing Chang work?? two authors found
                'Qing Chang'
                'Donna T. Chen',
                'Haibo Dong', 
                'Afsaneh Doryab', 
                'Lu Feng', 
                'Tomonari Furukawa', 
                'Gregory Gerling', 
                'Jonathan L. Goodall', 
                'Devin Harris', 
                'Seongkook Heo', 
                'Arsalan Heydarian', 
                'Tariq Iqbal', 
                'Barry Johnson', 
                # YL Kuo?
                'Yen-Ling Kuo',    #find author id
                'Venkataraman Lakshmi', 
                'James H. Lambert', 
                'Zongli Lin', 
                'Felix Xiaozhu Lin', 
                'Eric Loth', 
                'Osman E. Ozbulut',
                'B. Brian Park', 
                'Daniel Quinn', 
                'Sara Riggs', 
                'Haiying Shen', 
                'Cong Shen', 
                'Brian L. Smith', 
                'Stan R. Mircea',
                'John Stankovic', 
                'Yixin Sun', 
                'Sarah Sun', 
                'Yuan Tian', #no author found
                'Shangtong Zhang']

search_query = scholarly.search_author('Shangtong Zhang, Virginia')

author = scholarly.fill(next(search_query))

# get author's google scholar id
author_id = author['scholar_id']

# publications are in a list. Get last publication in list (most recent publication?)
publications = author['publications']
# print name of all publications
for pub in publications:
    print(pub['bib']['title'])
    print()


# for i in faculty_list:
#     search_query = scholarly.search_author(f"{i}, Virginia")
    
#     # scholarly returns a generator object
#     author = scholarly.fill(next(search_query))
    
    
    
    