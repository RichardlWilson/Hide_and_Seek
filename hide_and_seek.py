'''
Hide and Seek Phone Number
'''

import os
import random
import string
import bs4
import requests
import shutil


def grab_text():
    '''
    Scrapes irum lipsum text from website.
    '''
    url = 'https://www.lipsum.com/feed/html'
    div_tag = '#lipsum'
    re = requests.get(url)
    soup = bs4.BeautifulSoup(re.text, 'lxml')

    text = soup.select(div_tag)

    clean_text = text[0].get_text()

    return clean_text


def make(random_text, path = os.getcwd()):
    '''
    Creates 10 randomly named folders with 20 randomly names text files inside
    each one.
    '''
    main_folder_name = 'Hide_and_Seek'

    os.mkdir(main_folder_name)
    os.chdir(os.getcwd() +'\\'+ main_folder_name)
    path = os.getcwd()

    alpha = list(string.ascii_lowercase)

    for _ in range(10):
        random_foldername = ''

        for num in range(10):
            random_foldername += random.choice(alpha).upper()

        os.mkdir(random_foldername)

    for folder, sub_folders, files in os.walk(path):
        for sub_folder in sub_folders:

            for num in range(20):
                random_filename = ''

                for num in range(10):
                    random_filename += random.choice(alpha).lower()

                sub_folder_dir = path +'\\'+sub_folder
                f = open(os.path.join(sub_folder_dir, random_filename +'.txt'), 'w+')
                f.write(random_text)
                f.close()


def inject_phone_num():
    '''
    injects a random phone number inside a random text file.
    '''
    dir_list = []
    file_dir_list = []

    random_num = random.choice(range(0,10))

    random_phone_num = f'({random_num}{random_num}{random_num})' \
    +f'{random_num}{random_num}{random_num}-{random_num}{random_num}' \
    +f'{random_num}{random_num}'

    for folder, sub_folders, files in os.walk(os.getcwd()):
        for sub_folder in sub_folders:
                dir_list.append(folder+'\\'+sub_folder)
    
    for directory in dir_list:
        for folder, sub_folders, files in os.walk(directory):
            for file in files:
                file_dir_list.append(directory+'\\'+file)


    with open(random.choice(file_dir_list), 'w+') as f:
        f.write(random_phone_num)


def zip_dir(starting_dir):
    '''
    Compresses Hide_and_Seek Directory into a zip format.
    '''
    os.chdir(starting_dir)
    shutil.make_archive('Hide_and_seek', 'zip', starting_dir+'\\'+'Hide_and_seek')
    shutil.rmtree(starting_dir+'\\'+'Hide_and_seek')


if __name__ == '__main__':
    starting_dir = os.getcwd()
    irum_lipsum = grab_text()
    make(irum_lipsum)
    inject_phone_num()
    zip_dir(starting_dir)


       
