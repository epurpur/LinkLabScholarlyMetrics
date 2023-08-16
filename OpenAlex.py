

# UVA institutional ID:  I51556381
    
#info about institution
#https://api.openalex.org/institutions?filter=display_name.search:University%20of%20Virginia

#works by institution
#https://api.openalex.org/works?filter=institutions.id:I51556381


import requests
import json
import math
import pandas as pd


####### CHANGE THIS
output_file_location = '/Users/ep9k/Desktop/LinkLab/'


# Create pandas dataframe to hold data for each faculty member
link_lab_df = pd.DataFrame(columns=['Name', 'ORCID', 'Number of Publications', 'Publications with Co-Author', 'Average Publications per Year'])




"""
I am looking for # of publications, # of publications with co-author, # avg number publications per year
"""

# ORCID for Jonathan Goodall = 0000-0002-1112-4522
# ORCID for Larry Band = 0000-0003-0461-0503

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


for name, orcid in link_lab_orcids.items():
    
    #Step 1. Create Link Lab Faculty report as a whole
    if orcid != "?":
        try:    
            request = requests.get(f'https://api.openalex.org/authors/https://orcid.org/{orcid}')
            
            json_data = json.loads(request.text)
            faculty_name = json_data['display_name']
            number_publications = json_data['works_count']
            
            # print(f"Works URL for author: {json_data['works_api_url']}")
            works_url_for_author = json_data['works_api_url']
            
            works_url_for_author = works_url_for_author.split("=")
            
            all_publications_info = []   #holds all publications
            
            
            """ Step 1. Collect data for all link lab faculty together """
            # GETS DATA FOR PUBLICATIONS BY THE AUTHOR
            # I can get up to 200 publication results per page. I need to divide the author's total number of publications by 200 to get the # of pages
            number_of_pages = math.ceil(number_publications / 200)
            
            # iterate of number of pages needed per author
            for i in range(number_of_pages):
                request2 = requests.get(f'https://api.openalex.org/works?filter={works_url_for_author[1]}&page={i+1}&per-page=200')
                json_data2 = json.loads(request2.text)
            
                # take publications info and store in list
                for pub in json_data2['results']:
                    all_publications_info.append(pub)
            
            
            ## GET PUBLICATIONS WITH COAUTHOR AND # OF PUBLICATIONS PER YEAR
            pubs_with_coauthor = 0
            publication_years = []
            
            
            for paper in all_publications_info:
                publication_years.append(paper['publication_year'])
                if len(paper['authorships']) > 1:
                    pubs_with_coauthor += 1
                
                
            #convert publication_years to list of integers
            publication_years = list(map(int, publication_years))
            # gets average number of publications per year
            avg_pubs_per_year =  number_publications / ( max(publication_years) - min(publication_years))
            
            #put metricsin list to add to pandas dataframe
            faculty_data_final = [faculty_name, orcid, number_publications, pubs_with_coauthor, avg_pubs_per_year]
            
            # Add faculty member's data as last row of datafrmae
            link_lab_df.loc[len(link_lab_df)] = faculty_data_final
            
            
            """ Step 2. Collect publications per year data for individual faculty members"""
            # I want the number of publications per year in a dataframe
            years = []

            for pub in all_publications_info:
                years.append(pub['publication_year'])
                
            # get the unique years from the above list 'years'
            individual_years = list(set(years))


            # for each unique year in individual_years, count the occurrences of that year in the years list.
            # make result into dict ex: {'2015': 4}
            pubs_by_year = {}
            for year in individual_years:
                count = 0
                for i in years:
                    # match current item with current year. If match, increment the count. 
                    if i == year:
                        count += 1
                        
                pubs_by_year[year] = count
                
                
            # create dataframe to store final data
            final_pubs_dict = [{'Year': key, '# of Publications': value} for key, value in pubs_by_year.items()]

            final_publications_df = pd.DataFrame(final_pubs_dict)
            
            # sort in ascending order by year
            final_publications_df = final_publications_df.sort_values(by='Year')
            #export final_publications_df to csv. One for each faculty member
            final_publications_df.to_csv(output_file_location + name + '_pubs_per_year.csv', index=False)

        
        except Exception:
            """ Step 1. Collect data for all link lab faculty together """
            # create filler data for errors
            faculty_data_final = [name, 'n/a', 'n/a', 'n/a', 'n/a']
            
            # Add faculty member's data as last row of datafrmae
            link_lab_df.loc[len(link_lab_df)] = faculty_data_final
            
            """ Step 2. Collect publications per year data for individual faculty members"""
            final_publications_df = pd.DataFrame(columns=['Year', '# of Publications'])
            final_publications_df.to_csv(output_file_location + name + '_pubs_per_year.csv', index=False)

            
            
    else:
        """ Step 1. Collect data for all link lab faculty together """

        # create filler data for faculty with unknown or non-existant ORCID
        faculty_data_final = [name, 'n/a', 'n/a', 'n/a', 'n/a']
        
        # Add faculty member's data as last row of datafrmae
        link_lab_df.loc[len(link_lab_df)] = faculty_data_final

        """ Step 2. Collect publications per year data for individual faculty members"""
        final_publications_df = pd.DataFrame(columns=['Year', '# of Publications'])
        final_publications_df.to_csv(output_file_location + name + '_pubs_per_year.csv', index=False)



#export results to output file location for whole Link Lab data
link_lab_df.to_csv(output_file_location + 'link_lab_whole.csv', index=False)




