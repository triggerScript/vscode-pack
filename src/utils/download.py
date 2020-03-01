import urllib.request


def download(url, path):
    urllib.request.urlretrieve(url, path)
