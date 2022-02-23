from pytube import YouTube
#link = input("Enter the youtube link")
#link = "https://www.youtube.com/watch?v=oFnTcDYcGcM&list=RDoFnTcDYcGcM&start_radio=1"
link = "https://www.youtube.com/watch?v=e51JUlvjUEI&list=RDMMe51JUlvjUEI&start_radio=1"
yt = YouTube(link)
#print("Title: ", yt.title)
print(yt.streams)
print(yt.streams.filter(only_audio=True))
ys = yt.streams.get_audio_only()
ys.download(r"C:\Users\fenghaox\Downloads")
#ys.download()
print("Download completed")