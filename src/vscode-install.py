from os import listdir, system
from os.path import isfile, join, dirname

scriptDir = dirname(__file__)
dirPath = join(scriptDir, '../packages/extensions')
extensionFiles = [f for f in listdir(dirPath) if isfile(join(dirPath, f))]

for extensionFile in extensionFiles:
    system('cd {} && code --install-extension {}'.format(dirPath, extensionFile))
