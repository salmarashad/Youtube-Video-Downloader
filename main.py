import yt_dlp

def download_video(url):
    try:
        ydl_opts = {
            'format': 'best',
            'outtmpl': '%(title)s.%(ext)s',
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Searching for: {url}")
            ydl.download([url])
            print("\nDownload complete!")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    video_url = input("Enter the YouTube URL: ")
    download_video(video_url)