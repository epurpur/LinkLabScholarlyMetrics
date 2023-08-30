"""
Web of science starter api docs: https://api.clarivate.com/swagger-ui/?url=https://developer.clarivate.com/apis/wos-starter/swagger
Web of Science starter github docs: https://github.com/clarivate?q=wosstarter&type=&language=&sort=
"""


import requests
import json
import math
import pandas as pd

# request = requests.get(f'https://api.openalex.org/authors/https://orcid.org/{orcid}')
# json_data = json.loads(request.text)

api_key = "clarivate:6bb4e980-42bb-11ee-b598-f13658fb0f73"