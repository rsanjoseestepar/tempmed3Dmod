from django.shortcuts import render
from django.http import *
import time, urllib, urllib2
from main.models import *
from django.contrib.auth import *
import os, subprocess
from med3Dmodel import settings

import tempfile

# Create your views here.
# def worker(request):
#
#     if request.method == 'GET':
#         time.sleep(5)
#         print "slept and deleted"
#         id = request.GET.get('id')
#         user = request.GET.get('user')
#         print id + user
#         delete_model(id,user)
#         return HttpResponse("Done deleting")
#     else:
#         return HttpResponseForbidden
#
#
# def delete_model(id,user):
#
#         a = ImgContainer.objects.get(pk=id)
#         print a.user_id
#         print user
#         user = int(user)
#         print type(a.user_id)
#         print type(user)
#         if (a.user_id == user):
#             a.active = False
#             a.save()
#             return



def worker(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        user = request.GET.get('user')
        a = ImgContainer.objects.get(pk=id)
        file = a.file
        print file
        user = int(user)
        if (a.user_id == user):
            print "workeando"
            ee = ExecutionEngine()

            #Get path to input files
            labelmap_file = os.path.join(MEDIA_ROOT,a.file)
            print " File to process " + labelmap_file

            #Generate temporary file output
            output_file = os.path.join(ee.tmp_dir,os.path.basename(a.file),"-model.vtk")

            ee.GenerateModel(labelmap_file,model_file)

            #Update Model with output result and move result to permanent location

        return HttpResponse("Done")

    else:
        return HttpResponseForbidden



class ExecutionEngine():

    def __init__(self):
        self.slicer_path=os.environ('SLICER_PATH')
        self.slicer_path="/Applications/Slicer.app/Contents/lib/Slicer-4.4/cli-modules/"
        self.unu_path=os.environ('UNU_PATH')

        self.tmp_dir=tempfile.mkdtemp()

        self.debug = True


    def GenerateModel(self,labelmap_file,output_model):


        tmp_cmd = "%(path)/unu 2op gte $(in_file)s 1 -o $(tmp_file)s"

        out1 = os.path.join(self.tmp_dir,'tmp.nrrd')
        tmp_cmd = tmp_cmd % {'path':self.unu_path,'in_file':labelmap_file,'tmp_file':out1}

        self.run(tmp_cmd)

        tmp_cmd = "%(path)s/ModelMaker %(in_file)s -l 1 -n %(out_file)s"

        tmp_cmd = tmp_cmd % {'path':self.slicer_path,'in_file':out1,'out_file':output_model}

        self.run(tmp_cmd)

        #Delete tmp files
        shutil.rm(out1)


    def run(self,tmp_cmd):

        if self.debug==True:
            print tmp_cmd
        else:
            res=subprocess.call(tmp_cmd, shell=True )
            if res == False:
                return False
        return True


# def script():
#     caseLists = `ls -1 *BWH.nrrd | cut -d "_labelmap.nrrd" -f1`
#
#     shellThickness=20
#
#     for cc in $caseLists; do
#
#
#     unu 2op gte ${cc}.nrrd 1 -o tmp.nrrd
#     ComputeDistanceMap -l tmp.nrrd -m Maurer -d tmp-dm.nrrd -p
#
#     unu 3op in_cl 0 tmp-dm.nrrd $shellThickness -t ushort -o tmp-lm.nrrd
#
#     #GenerateModel -i tmp-lm.nrrd -l 1 -o ${cc}.vtk
#     /Applications/Slicer.app/Contents/lib/Slicer-4.4/cli-modules/ModelMaker tmp-lm.nrrd -l 1 -n ${cc}
#
#     #Computing model from raw
#     #GenerateModel -i tmp.nrrd -l 1 -o cip-raw.vtk
#     #/Applications/Slicer.app/Contents/lib/Slicer-4.4/cli-modules/ModelMaker tmp.nrrd -l 1 -n slicer-raw
#
#     #Compute a downsampled model for quicker displayed
#     unu resample -k cubic:1,0 -i tmp-dm.nrrd -s x0.5 x0.5 = -o tmp-dm-ds.nrrd
#     unu 3op in_cl 0 tmp-dm-ds.nrrd $shellThickness -t ushort -o tmp-lm-ds.nrrd
#
#     #GenerateModel -i tmp-lm-ds.nrrd -l 1 -o cip-ds.vtk
#     /Applications/Slicer.app/Contents/lib/Slicer-4.4/cli-modules/ModelMaker tmp-lm-ds.nrrd -l 1 -n ${cc}_downsampled
#
#     done