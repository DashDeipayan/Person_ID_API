import requests
import csv

r=requests.get("http://localhost:3000/db").json()

c = csv.writer(open("person_table.csv","w"), lineterminator='\n')

for i in r['person']:
    c.writerow([i['ID'],i['NAME'],i['Contact_no'],i['Address']])




               
