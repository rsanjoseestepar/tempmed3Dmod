from django.shortcuts import render
from django.http import *
import time, urllib, urllib2
# Create your views here.
def worker(request):
    if request.method == 'GET':
        time.sleep(5)
        print "slept"
        return HttpResponse("Done")
    else:
        return HttpResponseForbidden


