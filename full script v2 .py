import os
import json
import tarfile
import zipfile
import shutil
import requests
from googlesearch import search
import bs4

print('This script will convert your dark horse comic to cbz\n')

while True:
    print('-'*25)
    tar_path = input('Enter path of tar file = ')
    folder_path = os.path.dirname(tar_path)
    new_path = fr"{folder_path}\book"

    #un-tar the file

    print('Extracting the tar file...')
    file1 = tarfile.open(tar_path)
    file1.extractall(new_path)

    file1.close()
    print('Done!')

    #rename files to jpg in correct order

    print('Converting files to jpg...')

    file = open(fr"{new_path}\manifest.json",)
    data = json.load(file)
    uuid = data["book_uuid"]

    for i in data['pages']:
        page_number = i["sort_order"]
        page_name = i["src_image"]
        os.rename(fr"{new_path}\{page_name}",fr"{new_path}\{page_number}.jpg")

    file.close()
    print('Done!')

    #zip it into a cbz

    print('Zipping it into a cbz....')

    zipped_file = zipfile.ZipFile(fr'{folder_path}\book.cbz','w')

    for folder_name, subfolders, file_names in os.walk(fr"{new_path}\\"):
        for file_name in file_names:
            file_complete = folder_name + file_name 

            if 'jpg' in file_complete:
                zipped_file.write(file_complete, arcname = file_name)

    zipped_file.close()
    print('Done!')

    print('Removing temp files...')       
    shutil.rmtree(new_path)
    print('Done!')

    #get title

    print('Getting Title of the book from the url.....')

    for url in search(uuid, stop=3):
        if "darkhorse" in url:
            lorl = url

    ff = requests.get(lorl)
    ffx = bs4.BeautifulSoup(ff.text, 'html.parser')
    str1 = ffx.title.text
    str2 = str1.split('|')
    str3 = str2[0].strip('\n ')
    str3 = str3.replace(':', '-')
    os.rename(fr'{folder_path}\book.cbz', fr'{folder_path}\{str3}.cbz')

    print('Done!')

    print('Operatin completed!')
    print('-'*25)


