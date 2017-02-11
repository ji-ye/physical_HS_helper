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


def extract_img(data):
    """
    Extract the image links from data.

    Input:
        data: (dict)

    Return:
        list_img: list of strings

    Output:
        list_img.txt: text file of all the image links.
    """
    list_img = []
    #list_imgGold = []

    for key in data:
        for card in data[key]:
            if 'img' in card:
                #print(card['img'])
                list_img.append(card['img'])

    text_file = open('list_img.txt', 'w')
    #for link in list_img:
    text_file.write("\n".join(list_img))

    return list_img
