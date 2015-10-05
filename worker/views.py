from django.shortcuts import render
from django.http import *
import time, urllib, urllib2
# Create your views here.
def worker(request):
    if request.method == 'GET':
        time.sleep(5)
        print "slept and deleted"
        id = request.GET.get('id')
        delete_model(id)
        return HttpResponse("Done deleting")
    else:
        return HttpResponseForbidden


def delete_model(id):

		a=Model.objects.get(pk=id)
		if (a.user_id == user.id):
			a.active = False
			a.save()
