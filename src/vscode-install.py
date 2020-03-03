from os import listdir, system
from os.path import isfile, join, dirname

scriptDir = dirname(__file__)
extensionsPath = '../packages/extensions'
dirPath = join(scriptDir, extensionsPath)
extensionFiles = [f for f in listdir(dirPath) if isfile(join(dirPath, f))]

for extensionFile in extensionFiles:
    system('code --install-extension {}/{}'.format(dirPath, extensionFile))
