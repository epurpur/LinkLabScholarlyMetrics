import pandas as pd


missing_faculty = ['Maite Brandt-Pearce', 'Seokhyun Chung', 'Yen-Ling Kuo', 'Zhen Liu (Leo)', 'Yuan Tian', 'Amanda Watson']

faculty_names = ['ALEMAZKOOR, NEGIN', 'ALEMZADEH, HOMA', 'BAND, LAWRENCE EPHRAM', 'BARNES, LAURA',
                 'BEHL, MADHUR', 'BEZZO, NICOLA', 'BOLTON, MATTHEW LEE', 'BOWERS, STEVEN MICHAEL',
                 'CALHOUN, BENTON H', 'CAMPBELL, BRADFORD J', 'CHANG, QING', 'CHEN, TONG DONNA',
                 'DONG, HAIBO', 'DORYAB, AFSANEH', 'FENG, LU', 'FURUKAWA, TOMONARI', 'GERLING, GREGORY J',
                 'GOODALL, JONATHAN LEE', 'HARRIS, DEVIN K', 'HEO, SEONGKOOK', 'HEYDARIAN, ARSALAN',
                 'IQBAL, TARIQ', 'JOHNSON, BARRY W', 'LAKSHMI, VENKATARAMAN', 'LAMBERT, JAMES H',
                 'LIN, ZONGLI', 'LIN, XIAOZHU', 'LOTH, ERIC', 'OZBULUT, OSMAN E', 'PARK, B BRIAN',
                 'QUINN, DANIEL BENJAMIN', 'RIGGS, SARA LU', 'SHEN, HAIYING', 'SHEN, CONG', 'SMITH, BRIAN L',
                 'STAN, MIRCEA R', 'STANKOVIC, JOHN A', 'SUN, YIXIN', 'SUN, YE', 'ZHANG, SHANGTONG']

academic_analytics_df = pd.read_csv("/Users/ep9k/Desktop/LinkLab/academic_analytics.csv")



#filter personname column
filtered_df = academic_analytics_df[academic_analytics_df['personname'].isin(faculty_names)]