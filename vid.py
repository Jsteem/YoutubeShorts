
from pypexels import PyPexels
import psycopg2
import time
import requests
# Establish database connection
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password=""
)

# Create cursor
cursor = conn.cursor()

QUERY="nature vertical"

api_key = 'AGKyBH4u9wYBXjBwiKg9T79T73Y63khzSjEY73kfPVajjLeat37vqdHH'
# instantiate PyPexels object
py_pexel = PyPexels(api_key=api_key)
search_videos_page = py_pexel.videos_search(query=QUERY, per_page=40)
while True:
    for video in search_videos_page.entries:
        print(video.id, video.user.get('name'), video.url, video.duration, video.width, video.height)
        data_url = 'https://www.pexels.com/video/' + str(video.id) + '/download'


        insert_query = "INSERT INTO Backgrounds (backgroundsiteid, backgroundduration, backgroundmaker, backgroundlink, backgroundquery, width, height) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        values = (int(video.id), int(video.duration), video.user.get('name'),video.url, QUERY, int(video.width), int(video.height))
        try:
            cursor.execute(insert_query, values)
 
        except Exception as e: 
            print(e)

        conn.commit()
        # r = requests.get(data_url)

        # with open('nature_vids\\' + str(video.id) + '.mp4', 'wb') as outfile:
        #      outfile.write(r.content)



    if not search_videos_page.has_next:
        break
    
    time.sleep(10)
    search_videos_page = search_videos_page.get_next_page()


# Close cursor and connection
cursor.close()
conn.close()