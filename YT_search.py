from youtubesearchpython import VideosSearch

def search(keyword):
    print("searching...")

    returnData = ""
    videosSearch = VideosSearch(keyword, limit = 10).result().get('result')

    for i in range(len(videosSearch)):
        video = videosSearch[i]
        title = video['title']
        link = video['link']
        returnData = returnData + title+":\n"+link+"\n\n"

    return returnData
