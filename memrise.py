#!/usr/bin/python
# -*- coding: utf-8 -*-

# Bitbar plugin showing the number of words to water on Memrise

# <bitbar.title>Memrise Button</bitbar.title>
# <bitbar.version>v0.1</bitbar.version>
# <bitbar.author>Jakeoid</bitbar.author>
# <bitbar.author.github>jakeoid</bitbar.author.github>
# <bitbar.desc>Displays the number of words you have to review.</bitbar.desc>
# <bitbar.dependencies>python</bitbar.dependencies>

# Makes use of API information from..
# https://github.com/carpiediem/memrise-enhancement-suite/wiki/Unofficial-Documentation-for-the-Memrise-API

import requests

# Define your CATEGORYID, CSRFTOKEN & COOKIE.

CATEGORYID = ""
CSRFTOKEN = ""
SESSIONID = ""


url = "http://www.memrise.com/ajax/courses/dashboard/"

querystring = {
    "courses_filter": "learning",
    "limit": "1",
    "get_review_count": "true",
    "category_id": CATEGORYID
}

cookie = {
    'csrftoken': CSRFTOKEN,
    'sessionid': SESSIONID
}

query = requests.request("GET", url, cookies=cookie, params=querystring)

if query.content == 'Login required.':
    print('Error')
    print('---')
    print(' ')
    print('We failed to login to the Memrise Service.')
    print('Often this is just due to you not setting')
    print('the sessionid and cookie.')
else:
    response = query.json()
    print(response['to_review_total'])
    print('---')
    print('Click here to open Memrise | bash=open param1=https://memrise.com/review')
