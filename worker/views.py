from django.shortcuts import render
from django.http import *
import time, urllib, urllib2
# Create your views here.
def worker(request,id):
    if request.method == 'GET':
        time.sleep(5)
        delete_model(id)
        print "slept adn deleted"
        return HttpResponse("Done")
    else:
        return HttpResponseForbidden


def delete_model(id):

		a=Model.objects.get(pk=id)
		if (a.user_id == user.id):
			a.active = False
			a.save()
