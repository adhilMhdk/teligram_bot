import YT_search as youtubeSearch
import YT_Download as youtubeDownloader
def generateResponse(question):

    if question == "hi":
        return 'Hello,\nYou can search youtube videos using the format\n/search keyword'
    elif "how are you" in question.lower():
        return "Fine"
    elif "/search" in question.lower():
        return youtubeSearch.search(question.replace("/search",""))
    elif "/download" in question:
        return youtubeDownloader.downloadVideo(question.replace("/download ",""))
    else:
        return "I can't get you"