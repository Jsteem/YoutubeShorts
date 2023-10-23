# Automated YouTube Channel  

Automated YouTube channels have gained prominence due to their ability to generate content without continuous human intervention. This project shows how easy it is to automatically create videos in the format of the popular channel [psychologyarcade](https://www.youtube.com/@PsychologyArcade) that puts simple psychology quotes on stockvideo backgrounds.

## Database

A PostgreSQL database stores the quotes and the download links for the music and videos. The database is initialized via the [createDatabase.sql](./createDatabase.sql) script.

- [video.py](./video.py) is responsible for populating the database with  video file details. It achieves this by sourcing videos from the popular free stock video platform, pexels.com, utilizing the [Pexels API](https://www.pexels.com/api/).


- [music.py](./music.py) Fills the database with music data sourced from the Spotify API.
- [quote.py](./quote.py) Populates the database with quotes that are generated with ChatGPT.



## Uploading
A simple daily chronjob calls the [youtube_short.py](./youtube_short.py) script that composes the video, audio and text quote using MoviePy, a Python library that utilizes the FFmpeg library for video manipulation. Once the composition is complete, the script seamlessly uploads the final video to YouTube.

