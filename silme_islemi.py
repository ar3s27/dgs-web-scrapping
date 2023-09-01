import pandas as pd

# Excel dosyasını okuma
excel_file_path = 'universities.xlsx'
df = pd.read_excel(excel_file_path)

# "Bölüm Adı" sütununda "Burslu" geçen satırları filtreleme ve silme
df = df[~df['Bölüm Adı'].str.contains('Burslu')]

# "Bölüm Adı" sütununda "İndirimli" geçen satırları filtreleme ve silme
df = df[~df['Bölüm Adı'].str.contains('İndirimli')]

# "Bölüm Adı" sütununda "Burslu" geçen satırları filtreleme ve silme
df = df[~df['Bölüm Adı'].str.contains('Ücretli')]

# Filtrelenmiş DataFrame'i Excel dosyasına yazma
new_excel_file_path = 'devlet_üniversiteleri.xlsx'
df.to_excel(new_excel_file_path, index=False)

print(f"Veriler '{new_excel_file_path}' dosyasına başarıyla kaydedildi.")
