# -*- coding: utf-8 -*-
import json
import sys
import urllib2

def make_response():
    # cloudflare blocks default python user-agent
    headers = { 'User-Agent' : 'Mozilla/5.0' }
    url = 'https://ethgasstation.info/json/ethgasAPI.json'
    req = urllib2.Request(url, None, headers)
    response = urllib2.urlopen(req).read()
    return json.loads(response)

def output(data):
    return {
            'items': [
                {
                    'title': u"Average: {}".format(data['average'] / 10),
                    #'subtitle': u"{}s".format(data['avgWait']),
                    'type': 'default',
                    'arg': data['average']/10
                },
                {
                    #'uid': coin['rank'],
                    'title': u"Fast: {}".format(data['fast'] / 10),
                    #'subtitle': u"{}s".format(data['fastWait']),
                    'type': 'default',
                    'arg': data['fast']/10
                },
                {
                    #'uid': coin['rank'],
                    'title': u"SafeLow: {}".format(data['safeLow'] / 10),
                    #'subtitle': u"{}s".format(data['safeLowWait']),
                    'type': 'default',
                    'arg': data['safeLow']/10
                }]
            }

data = make_response()
sys.stdout.write(json.dumps(output(data)))
