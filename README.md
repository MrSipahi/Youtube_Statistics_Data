# What is it ?

  
This program add timely statistics data for the 'data' table in the database.

![enter image description here](https://raw.githubusercontent.com/MrSipahi/Youtube_Statistics_Data/main/photo/data.PNG)

# How does it work

  
İf you use this program, you must be take Youtube Data API. Take this here; [Console Cloud Google](https://console.cloud.google.com/).



If you will use this program, there must be a table named 'videoliste' because this program must take 'video_ID' data so, you must add 'videoliste'

![enter image description here](https://github.com/MrSipahi/Youtube_Statistics_Data/blob/main/photo/video_list.PNG?raw=true)


If you want reach static data, use this link:
 
    https://www.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&id=VIDEO_ID&key=API_KEY
   
   Python code:
   

    SpecificVideoUrl =  'https://www.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&id='+SpecificVideoID+'&key='+API_KEY
    response = urllib.request.urlopen(SpecificVideoUrl)
    videos = json.load(response)

#  Technologies

 - [Mysql](https://www.mysql.com/)
 - [Python](https://www.python.org/)
 - [Youtube Data API](https://developers.google.com/youtube/v3)
 - [Requests](https://pypi.org/project/requests/)
 

