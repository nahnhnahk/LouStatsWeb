# Create your views here.
from django.http import HttpResponse
import import_stats
from models import PlayerScore, Player
import datetime, random, math
from django.shortcuts import render_to_response
import json

def index(request):
    player_list = PlayerScore.objects.all()
    output = ([("(index=%d, score=%d)<br />" % (p.player.index, p.points)) for p in player_list])
    return HttpResponse(output)

def refresh(request):
    print "refresh!"
    import_stats.import_stat()
    return HttpResponse("refreshed!")

def user(request, id):
    player = Player.objects.get(index=int(id))
    player_score = player.playerscore_set.all()
    series = [json.dumps([{'x': int((ps.timestamp - datetime.datetime(1970,1,1)).total_seconds()),
                           'y': ps.points} for ps in player_score])]
    return render_to_response('player.html', {'series_data': series})

def top10(request):
    top_players = Player.objects.all()[:10]
    series = []
    for player in top_players:
        player_score = player.playerscore_set.all()
        series.append(json.dumps([{'x': int((ps.timestamp - datetime.datetime(1970,1,1)).total_seconds()),
                                   'y': ps.points} for ps in player_score]))
    return render_to_response('player.html', { 'series_data': series })

conn = None
