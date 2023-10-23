import requests
import psycopg2
import base64
import time
# Spotify API credentials
CLIENT_ID = ''
CLIENT_SECRET = ''
QUERY = 'mood:sad'
offset = 0
limit = 50


# Get access token
def get_access_token():
    url = 'https://accounts.spotify.com/api/token'
    headers = {'Authorization': f'Basic {get_auth_header()}'}
    data = {'grant_type': 'client_credentials'}
    response = requests.post(url, headers=headers, data=data)
    response_data = response.json()
    return response_data['access_token']

# Generate base64-encoded authorization header
def get_auth_header():
    credentials = f'{CLIENT_ID}:{CLIENT_SECRET}'
    encoded_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')
    return encoded_credentials

# Search for popular sad songs
def search_sad_songs(access_token, params):
    
    url = 'https://api.spotify.com/v1/search'
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(url, headers=headers, params=params)
    response_data = response.json()
    return response_data['tracks']['items']

# Download track samples
def download_track_samples(preview_url, track_name, track_artist):

        if preview_url:
            response = requests.get(preview_url)
            with open(f'{track_name} - {track_artist}.mp3', 'wb') as f:
                f.write(response.content)
                print(f'Downloaded: {track_name} - {track_artist}.mp3')
        else:
            print(f'No preview available for: {track_name} - {track_artist}')

def save_to_database(tracks, cursor, conn):
      for track in tracks:
        track_name = track['name']
        track_artist = track['artists'][0]['name']
        track_preview_url = track['preview_url']
        track_id = track['id']


        insert_query = "INSERT INTO music (musicpreviewlink, musicsiteid, musictitle, musicartist, musicquery) VALUES (%s,%s,%s,%s,%s)"
        values = (track_preview_url, track_id, track_name, track_artist, QUERY)

        try:
            cursor.execute(insert_query, values)
        except Exception as e: print(e)
        conn.commit()



# Main function
def main():
    # Establish database connection
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password=""
    )
    cursor = conn.cursor()

    # Obtain access token
    access_token = get_access_token()
         
    # Search for popular sad songs

    params = {
        'q': QUERY,
        'type': 'track',
        'limit': limit,
        'offset': offset
    }
    while True:


        sad_songs = search_sad_songs(access_token, params)
    
        save_to_database(sad_songs, cursor, conn)

        if len(sad_songs) != params['limit']:
            break

        params['offset'] += params['limit']
        print(params['offset'])
        time.sleep(3)

    # Close cursor and connection
    cursor.close()
    conn.close()

# Run the script
if __name__ == '__main__':
    main()