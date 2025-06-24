import base64

def decodeSound(imgstring, fileName):
    with open(fileName, 'wb') as f:
        f.write(base64.b64decode(imgstring))
