from moviepy.editor import *
import psycopg2
import requests
WIDTH = 1080
HEIGHT = 1920
fontsize = 60
w_text, h_text = 1000, 1900
w_text_heading, h_text_heading = 600, 200
offset_y = 400

def adjust_final_duration(video, final_duration):
    # Get the duration of the original video
    original_duration = video.duration

    # Calculate the factor by which the video should be slowed down
    factor = original_duration / final_duration

    # Slow down the video
    return video.fx(vfx.speedx, factor) 

def split_text(text, width):
    words = text.split()
    lines = []
    line = ""
    for word in words:
        line += word + " "
        if len(line) * fontsize > width:
            lines.append(line.strip())
            line = ""
    if line:
        lines.append(line.strip())
    return "\n".join(lines)


def assemble_video(quote_text, quote_heading):
    content = quote_text.split(";")
    fragments = len(content)
    length_short = 30 if fragments > 2 else 20 
    duration  = length_short // fragments
    start = 0
    end = duration
    text_clips = []

    video = VideoFileClip("temp_video.mp4")
    video = video.resize((WIDTH, HEIGHT))
    video = adjust_final_duration(video, length_short)

    for i in range(fragments):
        wrapped_content = split_text(content[i], w_text)
        sub_clip = video.subclip(start,min(end, length_short))

        # Create the text clip
        text_clip = TextClip(wrapped_content, 
                            size=(w_text, h_text), 
                            fontsize=fontsize, 
                            color='white',        
                            font="Source Code Pro ExtraLight",
                            ).set_duration(duration)

        text_clip = text_clip.set_pos(("center", 200)).set_duration(duration)

        start += duration                            
        end += duration

       
        title_clip = TextClip(quote_heading, 
                            size=(w_text_heading, h_text_heading), 
                            fontsize=50, 
                            color='white',
                            bg_color='black',
                            font="Source Code Pro ExtraLight",
                            ).set_duration(duration)
        title_clip = title_clip.set_pos(("center", offset_y)).set_duration(duration)


        watermark = TextClip("@WisdomOasisOfficial", 
                            size=(w_text_heading, h_text_heading), 
                            fontsize=50, 
                            color='white',
                            font="Source Code Pro ExtraLight",
                            ).set_duration(duration)
        watermark = watermark.set_pos(("center", 1600)).set_duration(duration)


        text_clips.append(CompositeVideoClip([sub_clip, text_clip, title_clip, watermark]))


    video = concatenate_videoclips(text_clips, method="compose")

    audio_clip = AudioFileClip("temp_audio.mp3")
    audio_clip = audio_clip.set_duration(length_short)

    new_audioclip = CompositeAudioClip([audio_clip])
    video.audio = new_audioclip
    return video

def load_info_from_database(cursor):

    query_sound ='''select * from music
                    where quoteid is null
                    limit 1'''
    query_background = '''select * from backgrounds
                        where quoteid is null
                        limit 1'''
    query_quote = '''select * from quotes
                    where backgroundid is null and musicclipid is null
                    limit 1'''

    try:
        cursor.execute(query_background)
        result = cursor.fetchall()[0]
        background_id = result[0]
        background_site_id = result[1]
        
        cursor.execute(query_sound)
        result = cursor.fetchall()[0]
        music_id = result[0]
        music_preview_link = result[1]

        cursor.execute(query_quote)
        result = cursor.fetchall()[0]
        quote_id = result[0]
        quote_text = result[1]
        quote_heading = result[2]

        return background_id, background_site_id, music_id, music_preview_link, quote_id, quote_text, quote_heading



    except Exception as e: 
        print(e)

def download_video(background_site_id):
    download_link = 'https://www.pexels.com/video/' + str(background_site_id) + '/download'
    response = requests.get(download_link)
    with open('temp_video.mp4', 'wb') as video_file:
        video_file.write(response.content)
    return video_file


def download_audio(music_preview_link):
    response = requests.get(music_preview_link)
    with open('temp_audio.mp3', 'wb') as audio_file:
        audio_file.write(response.content)
    return audio_file

def update_data_bank(conn, cursor, quote_id, background_id, music_id):
    cursor.execute("UPDATE Backgrounds SET quoteid = %s WHERE backgroundid = %s", (quote_id,background_id))
    cursor.execute("UPDATE Music SET quoteid = %s WHERE musicid = %s", (quote_id,music_id))
    cursor.execute("UPDATE Quotes SET backgroundid = %s, musicclipid = %s WHERE quoteid = %s", (background_id, music_id, quote_id))
    conn.commit()
    return

def post_to_youtube():
    CLIENT_SECRETS_FILE = "client_secrets.json"
    YOUTUBE_UPLOAD_SCOPE = "https://www.googleapis.com/auth/youtube.upload"
    YOUTUBE_API_SERVICE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"

    from oauth2client.client import flow_from_clientsecrets
    from oauth2client.file import Storage
    from oauth2client.tools import argparser, run_flow
    from apiclient.discovery import build
    import httplib2
    
    flow = flow_from_clientsecrets(CLIENT_SECRETS_FILE,
                                   scope=YOUTUBE_UPLOAD_SCOPE,
                                   )

    storage = Storage("%s-oauth2.json" % sys.argv[0])
    credentials = storage.get()
    if credentials is None or credentials.invalid:
        credentials = run_flow(flow, storage)


    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,http=credentials.authorize(httplib2.Http()))




    # Prepare video metadata
    request_body = {
        "snippet": {
            "title": "Psychology Insights #Shorts",
            "description": "Cool insights about psychology",
            "youTubeOptions": {
                    "shorts": True
            }
        },
        "status": {
            "privacyStatus": "public"
        }
    }

    # Upload the video
    media_file = "output.mp4"
    request = youtube.videos().insert(part="snippet,status", body=request_body, media_body=media_file)
    response = request.execute()

    # Print the video ID of the uploaded video
    print("Video uploaded. ID: %s" % response["id"])

def main():
    while True:
        conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password=""
        )

        # Create cursor
        cursor = conn.cursor()

        background_id, background_site_id, music_id, music_preview_link, quote_id, quote_text, quote_heading = load_info_from_database(cursor)
        download_video(background_site_id)
        download_audio(music_preview_link)
        video = assemble_video(quote_text, quote_heading)
        
        video.write_videofile("output.mp4")
        # video = video.without_audio()
        # while True:
        #     video.preview()


        post_to_youtube()
        update_data_bank(conn, cursor, quote_id, background_id, music_id)
        cursor.close()
        conn.close()


if __name__ == '__main__':
    main()

