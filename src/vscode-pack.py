import os
import json
from sys import platform
from utils.platform import checkPlatform
from utils.download import download

scriptDir = os.path.dirname(__file__)


def getSource():
    sourcePath = os.path.join(scriptDir, "./source.json")

    with open(sourcePath) as jsonFile:
        source = json.load(jsonFile)

    return source


source = getSource()
system = checkPlatform(platform)
url = source.get('vscode').get(system)
downloadFilePath = os.path.join(scriptDir, "../packages/vscode.exe")
download(url, downloadFilePath)
