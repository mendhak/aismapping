import datetime
from django.http import HttpResponse
from django.shortcuts import render_to_response
import ais



def home(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    resp = HttpResponse()
    return render_to_response("map.html")
    #resp.write(ais.decode('15PIIv7P00D5i9HNn2Q3G?wB0t0I', 0))
    #return resp



    #return render_to_response("map.html")