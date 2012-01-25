# Create your views here.
from django.http import HttpResponse
import import_stats
from models import PlayerScore

def index(request):
    player_list = PlayerScore.objects.all()
    output = ([("(index=%d, score=%d)<br />" % (p.index, p.points)) for p in player_list])
    return HttpResponse(output)

def refresh(request):
    print "refresh!"
    import_stats.import_stat()    
    return HttpResponse("refreshed!")

conn = None