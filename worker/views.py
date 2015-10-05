from django.shortcuts import render
from django.http import *
import time, urllib, urllib2
from main.models import *
from django.contrib.auth import *
# Create your views here.
def worker(request):

    if request.method == 'GET':
        time.sleep(5)
        print "slept and deleted"
        id = request.GET.get('id')
        user = request.GET.get('user')
        print id + user
        delete_model(id,user)
        return HttpResponse("Done deleting")
    else:
        return HttpResponseForbidden


def delete_model(id,user):

        a = ImgContainer.objects.get(pk=id)
        print a.user_id
        print user
        # print "b" + a.user_id + "b"
        # print "b" + user + "b"
        # print type(a.user_id)
        # print type(user)
        if (a.user_id == user):
            a.active = False
            a.save()
            return