import pandas as pd
import requests as re
from bs4 import BeautifulSoup as bs

uniler = {}

url = "https://tabanpuanlari.net/dgs/bolum/bilgisayar-muhendisligi"
response = re.get(url)
soup = bs(response.content, "html.parser")

table = soup.find("table")
rows = table.find_all("tr")

atla = 10
for i, row in enumerate(rows[:253]):
    cells = row.find_all("td")

    if i == atla:
        atla += 11
        continue
    else:
        if cells:
            id = cells[0].text.strip()
            universty = cells[1].text.strip()
            quota = cells[2].text.strip()
            point = cells[5].text.strip()
            arrangement_1 = cells[8].text.strip()
            arrangement_2 = cells[9].text.strip()
            section_name = cells[12].text.strip()
            
            print("id: " + id)
            print("Üniversite: " + universty)
            print("Kontenjan: " + quota)
            print("Puan: " + point)
            print("Sıralama 2023: " + arrangement_1)
            print("Sıralama 2022: " + arrangement_2)
            print("Bölüm Adı: " + section_name)
            print("\n")

            uniler[id] = {
                "Üniversite":universty,
                "Kontenjan":quota,
                "Puan":point,
                "Sıralama 2023":arrangement_1,
                "Sıralama 2022":arrangement_2,
                "Bölüm Adı":section_name
            }

df = pd.DataFrame.from_dict(uniler, orient='index')

excel_file_path = 'Üniversiteler_bilgisayar_2023.xlsx'
df.to_excel(excel_file_path, index=False)

print(f"Veriler '{excel_file_path}' dosyasına başarıyla kaydedildi.")
