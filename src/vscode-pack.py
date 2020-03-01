import os
import json
from sys import platform
from environment.vscode.src.utils.platform import checkPlatform
from environment.vscode.src.utils.download import download

scriptDir = os.path.dirname(__file__)
sourcePath = os.path.join(scriptDir, "./source.json")

with open(sourcePath) as jsonFile:
    source = json.load(jsonFile)

system = checkPlatform(platform)
url = source.get('vscode').get(system)
downloadFilePath = os.path.join(scriptDir, "./packages/vscode.exe")
download(url, downloadFilePath)
