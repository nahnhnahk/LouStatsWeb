'''
Created on Jan 12, 2012

@author: Nhan
'''
import sys
import httplib, urllib, json, random, pprint, pickle, time
from datetime import datetime
from models import PlayerScore, Player, World

sessionId = '5642f1b8-8d80-4a00-ad96-bdb0c79c3bb3';

current_world = World.objects.get_or_create(name = "World 83", 
                                            host = "prodgame05.lordofultima.com", 
                                            ajax_end_point = "/197/Presentation/Service.svc/ajaxEndpoint/")[0]

header = {'Accept': '*/*',
          'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
          'Accept-Encoding': 'gzip,deflate,sdch',
          'Accept-Language': 'en-US,en;q=0.8',
          'Content-Type': 'application/json; charset=utf-8',
#           'Cache-Control': 'no-cache',
#           'Pragma': 'no-cache',
          'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
          'X-Qooxdoo-Response-Type': 'application/json'}

conn = False

def get_conn():
    return httplib.HTTPConnection(host = current_world.host, timeout = 1)
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
    conn.request("POST", current_world.ajax_end_point + endpoint, params, header)
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
        'end': 6000,
        'continent':-1,
        'sort': 0,
        'ascending': True,
        'type': 0})
    scores = json.loads(scores)
    
    translate_map = {
        'p_id': 'i',
        'name': 'n',
        'j': 'j',
        'alliance': 'a',
        'points': 'p',
        'rank': 'r',
        'cities': 'c'
    }
    
    for player_score in scores:
        p = Player.objects.get_or_create(index = player_score['i'],
                                         world = current_world)[0]
        ps = PlayerScore(
            player = p,
            points = player_score[translate_map['points']],
            rank = player_score[translate_map['rank']],
            timestamp = datetime.now())
        ps.save()
#conn.close()
