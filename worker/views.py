from django.shortcuts import render
from django.http import *
import time, urllib, urllib2
from main.models import *
from main.forms import *
from django.contrib.auth import *
import os, subprocess
from med3Dmodel.settings import MEDIA_ROOT, AWS_STORAGE_BUCKET_NAME
from django.contrib.auth.models import User
from django.db.models import FileField
from django.core.files import File
from django.core.files.storage import default_storage

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

class ExecutionEngine():

    def __init__(self):
        #self.slicer_path=os.environ('SLICER_PATH')
        self.slicer_path="/Applications/Slicer.app/Contents/lib/Slicer-4.4/cli-modules/"
        #self.unu_path=os.environ('UNU_PATH')
        self.unu_path="/Users/rubensanjose/src/ChestImagingPlatform-build/teem-build/bin"
        self.tmp_dir=tempfile.mkdtemp()

        self.debug = False


    def GenerateModel(self,labelmap_file,output_model):


        print "Here"
        tmp_cmd = "%(path)s/unu 2op gte %(in_file)s 1 -o %(tmp_file)s"

        out1 = os.path.join(self.tmp_dir,'tmp.nrrd')
        tmp_cmd = tmp_cmd % {'path':self.unu_path,'in_file':labelmap_file,'tmp_file':out1}

        self.run(tmp_cmd)

        tmp_cmd = "%(path)s/ModelMaker %(in_file)s -l 1 -n %(out_file)s"

        tmp_cmd = tmp_cmd % {'path':self.slicer_path,'in_file':out1,'out_file':output_model}

        self.run(tmp_cmd)

        #Delete tmp files
        # shutil.rm(out1)
        print "mojo" + output_model
        return output_model

    def run(self,tmp_cmd):

        if self.debug == True:
            print tmp_cmd
        else:
            print tmp_cmd
            res=subprocess.call(tmp_cmd, shell=True )
            if res == False:
                print "Falso"
                return False
        return True

    def file_manager(self, object):
        tmp_dir = tempfile.mkdtemp()
        file_path = object.file.url
        return file_path

    def erase_file_manager(self,tmp_dir):
        shutil.rmtree(tmp_dir)
        return

def worker(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        user = request.GET.get('user')
        id = int(id)
        user = int(user)
        a = ImgContainer.objects.get(pk=id)

        user_object = User.objects.get(pk=user)
        name = a.name
        file = a.file
        print file

        if (a.user_id == user):
            print "workeando"
            ee = ExecutionEngine()
            print type(file)
            filestr = str(file)
            #Get path to input files
            print default_storage
            labelmap_file = os.path.join(MEDIA_ROOT, filestr )
            print " File to process " + labelmap_file

            #Generate temporary file output
            output_file = os.path.join(ee.tmp_dir,os.path.basename(filestr)+"-model")
            print output_file
            print "Ready to call"
            print ee.slicer_path
            ee.GenerateModel(labelmap_file,output_file)

            #Update Model with output result and move result to permanent location
            # model = Model()
            #
            # f = open(output_file+'.vtk')
            #
            # ff = FileField()
            # ff.save("ProcessedModel",File(f))
            #
            # model.model_file = ff
            # model.user=user
            # model.name="Nuevo Modelo"
            #
            # model.save()

            model = Model()
            vtkfile = output_file + '.vtk'
            model.name = "Modelo del worker"
            model.user = user_object

            with open(vtkfile , 'rb') as doc_file:
                tt = File(doc_file)
                print "Hi"
                model.model_file.save('filename', File(doc_file), save=True)

            model.save()


        return HttpResponse("Done")

    else:
        return HttpResponseForbidden




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