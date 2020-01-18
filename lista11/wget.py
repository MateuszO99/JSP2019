import urllib.request, urllib.error, urllib.parse
from sys import argv, exit

if len(argv) > 1:
    url = argv[1]

    try:
        response = urllib.request.urlopen(url)
    except:
        print('Nie poprawny link')
        exit()

    webContent = response.read()

    if url.endswith('.html'):
        nameOfFile = url[url.rindex('/') + 1:]
    if url.endswith('.htm'):
        nameOfFile = url[url.rindex('/') + 1:]
    elif url.endswith('.php'):
        nameOfFile = url[url.rindex('/') + 1:]
    elif url.endswith('.js'):
        nameOfFile = url[url.rindex('/') + 1:]
    elif url.endswith('.txt'):
        nameOfFile = url[url.rindex('/') + 1:]
    else:
        nameOfFile = 'index.html'

    file = open(nameOfFile, 'w')
    file.write(str(webContent))
    file.close()
else:
    print('Nie podano linku')