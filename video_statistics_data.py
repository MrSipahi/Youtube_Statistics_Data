
import urllib #importing to use its urlencode function
import urllib3 #for making http requests
import requests
import json #for decoding a JSON response
from datetime import datetime
import locale
import pymysql as MySQLdb

db = MySQLdb.connect("ip","user","password","db_names" )
cursor = db.cursor()

#
keys = ["API_KEYS"]

key_numara = 0
API_KEY = keys[key_numara] 
 
query="SELECT * FROM kanal"
cursor.execute(query)

kanallar = cursor.fetchall()

kanal_list=[]
for i in kanallar:
    kanal_list.append(i[0])


locale.setlocale(locale.LC_ALL, "") 
moment = datetime.now()
toplam=1

def veri_cek(metadata,toplam,API_KEY):
         # Here the videoID is printed
    try:
        SpecificVideoID = metadata
        SpecificVideoUrl = 'https://www.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&id='+SpecificVideoID+'&key='+API_KEY
        response = urllib.request.urlopen(SpecificVideoUrl) #makes the call to a specific YouTube
    except Exception as e:
        print(e)
        return 1

    videos = json.load(response) 

    for video in videos['items']: 
        if video['kind'] == 'youtube#video':
            try:
                ad = video["snippet"]["title"]
                ad = ad.replace("'","-")
                goruntulenme= video['statistics']['viewCount']
                begenme = video["statistics"]["likeCount"]
                begenmeme=video["statistics"]["dislikeCount"]
                yorum = video['statistics']['commentCount']
                

                a = video['snippet']['publishedAt']
                b = a.split("T")
                c = b[1].split(".")
                d = c[0].split("Z")
                yuklenme_tarihi = b[0]
                yuklenme_saati = d[0]
                tarih = moment.strftime("%Y-%m-%d")

                query = f"insert into data(videoID,kanal_ID,ad,goruntulenme,begenme,begenmeme,yorum,yuklenme_tarihi,yuklenme_saati,tarih) values ('{metadata}','{i}','{ad}',{goruntulenme},{begenme},{begenmeme},{yorum},'{yuklenme_tarihi}','{yuklenme_saati}','{tarih}')"
                cursor.execute(query)
                db.commit()
            except Exception as a:
                print(a)
                continue
                
            print(f"Toplam= {toplam}")
        toplam = toplam + 1  

for i in kanal_list:
    videoMetadata=[]
    query=f"SELECT DISTINCT videoID FROM videoliste where kanal_ID= '{i}' "
    cursor.execute(query)
    for j in cursor.fetchall():
        videoid = videoMetadata.append(j[0])
        a = veri_cek(j[0],toplam,keys[key_numara])
        if a==1:
            key_numara += 1
            if key_numara == 11:
                key_numara = 0
            API_KEY = keys[key_numara]
            veri_cek(j[0],toplam,keys[key_numara])
            
cursor.close()
db.commit()
db.close()
