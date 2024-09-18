import yt_dlp

def download_video(url):
    ydl_opts = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s',
        'socket_timeout': 30,  # Increase timeout to 30 seconds
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            print("Download completed!!")
    except yt_dlp.utils.DownloadError as e:
        print(f"An error occurred: {str(e)}")

url = input("Enter YouTube video URL: ")
download_video(url)
