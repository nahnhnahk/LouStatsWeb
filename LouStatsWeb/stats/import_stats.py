'''
Created on Jan 12, 2012

@author: Nhan
'''
import sys
import httplib, urllib, json, random, pprint, pickle, time
from datetime import datetime
from models import PlayerScore, Player, World

sessionId = '5f6ce529-39ca-4850-a8ff-4d1f99d92ac2';

current_world = World.objects.get_or_create(name = "World 83", 
                                            host = "prodgame05.lordofultima.com", 
                                            ajax_end_point = "/197/Presentation/Service.svc/ajaxEndpoint/")[0]

header = {'Content-Type': 'application/json; charset=utf-8',
           'Cache-Control': 'no-cache',
           'Pragma': 'no-cache',
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
    pprint.pprint(scores)
    
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
        print ps
        ps.save()
#conn.close()
