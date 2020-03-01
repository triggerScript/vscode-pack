def checkPlatform(platform):
    if platform == 'linux' or platform == 'linux2':
        return 'linux'
    elif platform == 'darwin':
        return 'mac'
    elif platform == 'win32':
        return 'win'