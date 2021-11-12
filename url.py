import webbrowser

while True:
    old_url = input('Enter book url = ')

    uuid = old_url.split('/')[-1]

    new_url = fr"https://digital.darkhorse.com/api/v6/book/{uuid}"

    print('Opening the download adress...')
    webbrowser.open(new_url)
