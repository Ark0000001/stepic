from pytube import YouTube

video_url = "https://www.youtube.com/watch?v=611-Tvmuudk&t=1s"

yt = YouTube(video_url)

print(yt.streams.filter(progressive=True))

download_stream = yt.streams.filter(progressive=True).first()

download_stream.download(output_path=".")

print("Видео успешно скачано!")

