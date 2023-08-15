
import requests
import lxml
from bs4 import BeautifulSoup
import pandas as pd


faculty_list = {
    "Jonathan Goodall": "https://scholar.google.com/citations?user=M9aKXDwAAAAJ&hl=en&oi=ao"
    }


source = requests.get(faculty_list['Jonathan Goodall'])
soup = BeautifulSoup(source.text, 'lxml')


