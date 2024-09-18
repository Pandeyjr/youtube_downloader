# youtube_downloader.py
import yt_dlp as youtube_dl

def download_youtube_video(url, download_path="."):
    ydl_opts = {
        'outtmpl': f'{download_path}/%(title)s.%(ext)s',
        'format': 'best',  # Downloads the best available quality
    }
    
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            print("Downloading...")
            ydl.download([url])
            print("Download completed!")
    except Exception as e:
        print(f"Error: {e}")

def main():
    video_url = input("Enter the YouTube video URL: ")
    download_location = input("Enter the download path (default is current directory): ") or "."
    
    download_youtube_video(video_url, download_location)

if __name__ == "__main__":
    main()
