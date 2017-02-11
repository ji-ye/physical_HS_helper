# Physical hearthstone project
#
# Ji, Ye
#
# Some functions that collects game data.

import json

def json_to_dict(json_filename):
    """
    Convert a json file to dictionary.

    Input: json_filename (string)

    Return: data (dictionary)
    """
    with open(json_filename) as data_file:
        data = json.load(data_file)

    return data


def extract_img(data, extract_key):
    """
    Extract the image links from data.

    Input:
        data: (dict)
        extract_key: (string) a key in data. e.g. 'img' or 'imgGold'
    Return:
        list_img: list of strings

    Output:
        list_img.txt: text file of all the image links.
    """
    list_img = []
    #list_imgGold = []

    for key in data:
        for card in data[key]:
            if extract_key in card:
                #print(card['img'])
                list_img.append(card[extract_key])

    text_filename = '{}'.format(extract_key)
    print(text_filename)
    text_file = open(text_filename, 'w')
    #for link in list_img:
    text_file.write("\n".join(list_img))

    return list_img

#from multiprocessing import Pool
from urllib import request
def download_url(url):
    """
    Download file from url.

    Input: url (string)

    Output: download file
    """
    file_name = str(url.split('/')[-1])
    u = request.urlopen(url)
    f = open(file_name, 'wb')
    f.write(u.read())
    f.close()

def batch_download(lst_links):
    """
    Download a bunch files from a list of links.

    Input: lst_links(list)

    Output: download files
    """
    for link in lst_links:
        download_url(link)
    return

    #from multiprocessing import Pool
