import urllib.request

def download_data():
    try:
        urllib.request.urlretrieve("https://ndownloader.figshare.com/files/7586326", "data.csv")
    except Exception as e:
        print(e)
        return 0
    return 1
