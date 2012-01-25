'''
Created on Jan 12, 2012

@author: Nhan
'''
import sys
import httplib, urllib, json, random, pprint, pickle, time
from datetime import datetime
from models import PlayerScore

sessionId = '820c2f76-dfd7-4ba2-9180-f102798ab866';

header = {'Content-Type': 'application/json; charset=utf-8',
           'Cache-Control': 'no-cache',
           'Pragma': 'no-cache',
           'X-Qooxdoo-Response-Type': 'application/json'}

conn = False

def get_conn():
    return httplib.HTTPConnection(host = "prodgame13.lordofultima.com", timeout = 1)
#    global conn
#    print conn
#    if not conn:
#        import logging
#        logging.debug("Initialize connection!")
#        return httplib.HTTPConnection(host = "prodgame13.lordofultima.com", timeout = 1)
#    else:
#        import logging
#        logging.debug("CONN: " + str(conn))
#        return conn

def request(endpoint, params):
    time.sleep(1)
    conn = get_conn()
    conn.request("POST", "/91/Presentation/Service.svc/ajaxEndpoint/" + endpoint, params, header)
    response = conn.getresponse()
    print response.status
    if response.status != 200:
        print response.reason
        sys.exit(1)
    body = response.read()
    return body

def request_json(endpoint, params):
    return request(endpoint, json.dumps(params))

def import_stat():
    scores = request_json("PlayerGetRange", {
        'session': sessionId,
        'start': 0,
        'end': 5,
        'continent':-1,
        'sort': 0,
        'ascending': True,
        'type': 0})
    scores = json.loads(scores)
    pprint.pprint(scores)
    
    translate_map = {
        'index': 'i',
        'name': 'n',
        'j': 'j',
        'alliance': 'a',
        'points': 'p',
        'rank': 'r',
        'cities': 'c'
    }
    
    for player in scores:
        ps = PlayerScore( \
            index = player[translate_map['index']], \
            points = player[translate_map['points']])
        ps.save()

#conn = httplib.HTTPConnection("prodgame13.lordofultima.com")
#conn.set_debuglevel(1)
#import_stat()
#conn.close()
