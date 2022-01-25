from pytube import YouTube

#URL
url = input("URL: ")
video = YouTube(url)

#print(video.title)

#DOWNLOAD
video = video.streams.get_highest_resolution()
video.download()

