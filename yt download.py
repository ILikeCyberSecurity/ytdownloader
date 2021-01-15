from pytube import YouTube
yt= YouTube('https://www.youtube.com/watch?v=bHtLSwi-0mQ')
print(yt.title)
print(yt.thumbnail_url)
print(yt.streams.all())
stream_1=yt.streams.first()
stream_1.download()
