import json
import csv
import os

from django.conf import settings
from django.db import connection


if __name__ == '__main__':

    my_file = open('/Users/williamliu/Desktop/data/smallSampleTweets.json')
    data = json.load(my_file)
    print data

    # settings.configure()
    cursor = connection.cursor()
    result = cursor.execute("SELECT COUNT(*) FROM twitterbot")
    print result[0]['count']
