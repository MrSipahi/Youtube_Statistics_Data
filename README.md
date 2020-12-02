# What is it ?

  
This code adds the current statistics data of the videos to the 'data' table in the database.

![enter image description here](https://raw.githubusercontent.com/MrSipahi/Youtube_Statistics_Data/main/photo/data.PNG)

# How does it work

  
To use the Youtube Data API service, you need to get an API_Key. You can get it from the address below.

 - [Console Cloud Google](https://console.cloud.google.com/)


For this code to work, there must be a table named 'videolist' in the database. Retrieves the 'video_ID' data from this table. 

![enter image description here](https://github.com/MrSipahi/Youtube_Statistics_Data/blob/main/photo/video_list.PNG?raw=true)


The url we use to access statistical data:
 
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
 

