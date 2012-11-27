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
    two_lists = zip(*[(ps.timestamp, ps.points) for ps in player_score])
    data = json.dumps([{'x': int((ps.timestamp - datetime.datetime(1970,1,1)).total_seconds()),
                        'y': ps.points} for ps in player_score])
    return render_to_response('player.html', {'data': data})

#print "ASDKFASDKFJASDLKFJALSDFJ"
#dt = datetime.timedelta(days=1)
#today = datetime.date.today()
#series = [i*0.1 for i in range(10)]
#timeSeries = map(str, [today - i*dt for i in reversed(range(10))])
#rand = [random.random() for i in range(10)]
#sqrt = [math.sqrt(i*0.1) for i in range(10)]
#data = {'x': series, 'y': rand}
#timeSeriesData = {'x': timeSeries, 'y': rand}
#return render_to_response('examples/line_chart.html', {'series': sqrt})

conn = None