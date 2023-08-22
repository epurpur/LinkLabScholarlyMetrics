

import pandas as pd

# Sample DataFrame
data = {
    'author': ['John Smith', 'Jane Doe'],
    'title': ['Introduction to LaTeX', 'Data Analysis Techniques'],
    'year': [2000, 2015]
}

df = pd.DataFrame(data)

# Function to format a DataFrame row as a BibTeX entry
def format_bibtex_entry(row):
    return f"@book{{{row['author'].replace(' ', '_')}_{row.name}, author = '{row['author']}', title = '{row['title']}', year = {row['year']}, myField1 = 'This is a test'}}"


# Apply the function to each row and create a new column with BibTeX entries
df['bibtex'] = df.apply(format_bibtex_entry, axis=1)

# replace single quotes with double quotes
df['bibtex'] = df['bibtex'].str.replace("'", '"')

# Write the BibTeX entries to a .bib file
with open('Publications 2001.bib', 'w') as bibfile:
    bibfile.write('\n'.join(df['bibtex']))

print("BibTeX entries written to 'references.bib'")