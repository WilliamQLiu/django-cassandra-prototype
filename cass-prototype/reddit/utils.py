import json
import csv
import os
import uuid

from django.conf import settings
from django.db import connection


def load_json():
    my_file = open('/Users/williamliu/Desktop/data/smallSampleTweets.json')
    data = json.load(my_file)
    print data


def execute_raw_cql():
    # settings.configure()
    cursor = connection.cursor()
    result = cursor.execute("SELECT COUNT(*) FROM twitterbot")
    print result[0]['count']


def generate_uuid(times=10):
    """ Give some random UUIDs for testing """
    for item in xrange(times):
        print uuid.uuid4()


if __name__ == '__main__':
    generate_uuid()
