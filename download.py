#!/usr/bin/env python

import os
import time
import requests
from bs4 import BeautifulSoup
import re
import urllib
from os.path import expanduser


def download(url):
    r = requests.get(url)
    filename = os.path.basename(url)
    print("filename: " + filename)
    with open(expanduser("~") + "/WorkDocs/black belt/" + filename, 'wb') as file:
        try:
            file.write(r.content)
        except:
            print("File writer error has occurred...")


def main():
    url = "https://aws.amazon.com/jp/aws-jp-introduction/"
    try:
        html = requests.get(url)
    except:
        print("GET requests error has occurred...")

    soup = BeautifulSoup(html.content)
    total_time = time.time()
    for a in soup.find_all("a", href=re.compile("pdf")):
        start_time = time.time()
        href = a.get('href')
        download_url = urllib.parse.unquote(href)
        if re.compile("^//").match(download_url):
            download_url = "http:" + download_url
        download(download_url)
        print("--- download time: %s seconds ---" % (time.time() - start_time))
    print("--- Total execution time: %s seconds ---" % (time.time() - total_time))


if __name__ == "__main__": main()
