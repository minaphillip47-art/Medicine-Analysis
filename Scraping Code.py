import requests as rq
import pandas as pd
from bs4 import BeautifulSoup as bs




#Main#
#medcines#
url='https://www.dawaagate.com/medicines'
all_medcine=[]
for page_num in range(1,1145):
    response = rq.get(url, params={'page': page_num})
    if response.status_code==200:
        print(f"Page {page_num} fetched successfully.")
    else:
        print(f"Failed to fetch page {page_num}. Status code: {response.status_code}")
        continue
    soup= bs(response.content,'html.parser')
    medcines=soup.select('article.ph-card')
    for medcine in medcines:
        name = medcine.find('h3',class_='ph-card-name').text.strip()
        name_en= medcine.find('p',class_='ph-card-en').text
        medcine_type= medcine.find('span',class_='ph-card-cat').text
        company_n= medcine.find('p',class_='ph-card-company')
        Company_name= company_n.text if company_n else None
        now_tag = medcine.find('span', class_='ph-price-now')
        price_now = now_tag.text if now_tag else None
        old_tag = medcine.find('span', class_='ph-price-old')
        price_old = old_tag.text if old_tag else None
        all_medcine.append([name, name_en, medcine_type, Company_name, price_now, price_old])
columns= ['name','name_en','medcine_type','company_name','price_now','price_old']
medcines= pd.DataFrame(all_medcine,columns = columns)
medcines.to_csv('medcines.csv', index=False, encoding='utf-8-sig')

#date#


all_dates = []
base_url = 'https://www.dawaagate.com/price-updates'

for page_num in range(1,1135):
    response = rq.get(base_url, params={'page': page_num})
    if response.status_code == 200:
        print(f"Page {page_num} fetched successfully.")
    else:
        print(f"Failed to fetch page {page_num}. Status code: {response.status_code}")
        continue

    soup = bs(response.content, 'html.parser')
    rows = soup.select('table.ph-table tbody tr')

    for row in rows:
        name_cell = row.find('td', class_='name')
        if name_cell is None:
            continue

        link_tag = name_cell.find('a')
        name = link_tag.text.strip() if link_tag else None
        link = link_tag.get('href') if link_tag else None

        cells = row.select('td[class="num"]')
        update_date = cells[-1].text.strip() if cells else None

        all_dates.append([name, link, update_date])   

df = pd.DataFrame(all_dates, columns=['name', 'link', 'update_date'])
df.to_csv('dates.csv', index=False, encoding='utf-8-sig')
