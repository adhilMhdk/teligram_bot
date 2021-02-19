from pytube import YouTube

def downloadVideo(link):
    link = link.replace(" ","")
    print(link)
    try:
        print("getting video")
        video = YouTube(link).streams.first()
        print("Got the video")
        video.download()
        print("downloaded")
        return "$FILE$/home/adhil/PycharmProjects/teligramBot/"+video.default_filename
    except:
        return "An error occurred"